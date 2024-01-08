import requests
from fastapi import FastAPI
from utils.query import get_ditto_score
import json

#  run me https://fastapi.tiangolo.com/#installation
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the world of DITTO!"}


@app.get("/var/{chromosome}-{position}-{ref}-{alt}")
def get_variant_score(chromosome, position, ref, alt):
    scores = get_ditto_score(chrom=chromosome, pos=position, ref=ref, alt=alt)
    return {"scores_by_transcript": scores}


# @app.get("/hgvs/{hgvs_cdna}")
# def get_hgvs_score(hgvs_cdna):
#     # TODO call mapping API from VEP to convert to genomic coordinates
#     # https://rest.ensembl.org/documentation/info/vep_hgvs_get
#     # TODO call the lookup for a variant
#     # scores = get_variant_score( stuff from vep for variant info on genome build)
#     return {"variant": hgvs_cdna}


# # Function to query variant reference allele based on posiiton from UCSC API
# def query_variant(chrom: str, pos: int, allele_len: int) -> json:

#     if not chrom.startswith("chr"):
#         chrom = "chr" + chrom

#     url = f"https://api.genome.ucsc.edu/getData/sequence?genome=hg38;chrom={chrom};start={pos-1};end={pos+allele_len-1}"

#     get_fields = requests.get(url, timeout=20)

#     if "statusCode" in get_fields.json().keys():
#         print(
#             f"Error {str(get_fields.json()['statusCode'])}: {get_fields.json()['statusMessage']}. Possibly invalid or out of range position."
#         )

#     # Check if the request was successful
#     try:
#         get_fields.raise_for_status()
#     except requests.exceptions.RequestException as expt:
#         print(
#             f"Could not get UCSC Annotations for chrom={chrom} and pos={str(pos)}."
#         )
#         raise expt

#     return get_fields.json()
