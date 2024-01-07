
import pandas as pd
import yaml
import json
from utils.parse import OCApiParser
from utils.predict import parse_and_predict
from tensorflow import keras
from pathlib import Path
import requests


# Function to open and load config file for filtering columns and rows
def get_col_configs(config_f):
    with open(config_f) as fh:
        config_dict = yaml.safe_load(fh)

    # print(config_dict)
    return config_dict


# Function to open and load data config file for parsing opencravat output
def get_parser(data_config):
    with data_config.open("rt") as dc_fp:
        data_config_dict = json.load(dc_fp)

    parser = OCApiParser(data_config_dict)
    return parser


# Function to load model and weights
def load_model(clf_path):
    # Load model and weights
    clf = keras.models.load_model(clf_path + "/Neural_network")
    clf.load_weights(clf_path + "/weights.h5")
    return clf

# Function to query variant reference allele based on posiiton from UCSC API
def query_variant(chrom: str, pos: int, allele_len: int) -> json:

    if not chrom.startswith("chr"):
        chrom = "chr" + chrom

    url = f"https://api.genome.ucsc.edu/getData/sequence?genome=hg38;chrom={chrom};start={pos-1};end={pos+allele_len-1}"

    get_fields = requests.get(url, timeout=20)

    if "statusCode" in get_fields.json().keys():
        print(
            f"Error {str(get_fields.json()['statusCode'])}: {get_fields.json()['statusMessage']}. Possibly invalid or out of range position."
        )

    # Check if the request was successful
    try:
        get_fields.raise_for_status()
    except requests.exceptions.RequestException as expt:
        print(
            f"Could not get UCSC Annotations for chrom={chrom} and pos={str(pos)}."
        )
        raise expt

    return get_fields.json()

def get_ditto_score(chrom: str, pos: int, ref: str, alt: str):
    repo_root = Path(__file__).parent.parent.parent
    # Load the col config file as dictionary
    config_f = repo_root / "configs" / "col_config.yaml"
    config_dict = get_col_configs(config_f)

    # Load the data config file as dictionary
    data_config = repo_root / "configs" / "opencravat_test_config.json"
    parser = get_parser(data_config)

    # Load the model and data
    clf_path = repo_root / "results"
    clf = load_model(str(clf_path))

    overall = parser.query_variant(chrom=str(chrom), pos=int(pos), ref=ref, alt=alt)
    # Check if variant annotations are found
    if overall.empty:
        return(
            "Could not get variant annotations from OpenCravat's API. Please check the variant info and try again."
        )
    else:
        score_dict = {}
        for transcript in overall["transcript"].unique():
            transcript_data = overall[overall["transcript"] == transcript].reset_index(
                drop=True
            )
            y_score = parse_and_predict(transcript_data, config_dict, clf)
            y_score = round(y_score[0][0], 2)
            score_dict[transcript] = str(y_score)
        return score_dict

