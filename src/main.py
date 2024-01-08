from fastapi import FastAPI
from utils.query import get_ditto_score, query_variant
import json

#  run me https://fastapi.tiangolo.com/#installation
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the world of DITTO!"}


@app.get("/var/{chromosome}-{position}-{ref}-{alt}")
def get_variant_score(chromosome, position, ref, alt):
    ref = ref.upper()
    alt = alt.upper()
    actual_ref = query_variant(str(chromosome), int(position), len(ref))["dna"].upper()
    if ref != actual_ref:
        return {
            "error": f"Provided reference nucleotide '{ref}' does not match the actual nucleotide '{actual_ref}' from reference genome. Please fix the variant info and try again."
        }
    elif ref == alt:
        return {
            "error": "Reference nucleotide and alternate nucleotide are the same. Please fix the variant info and try again."
        }
    else:
        scores = get_ditto_score(chrom=chromosome, pos=position, ref=ref, alt=alt)
        return {"scores_by_transcript": scores}


# @app.get("/hgvs/{hgvs_cdna}")
# def get_hgvs_score(hgvs_cdna):
#     # TODO call mapping API from VEP to convert to genomic coordinates
#     # https://rest.ensembl.org/documentation/info/vep_hgvs_get
#     # TODO call the lookup for a variant
#     # scores = get_variant_score( stuff from vep for variant info on genome build)
#     return {"variant": hgvs_cdna}
