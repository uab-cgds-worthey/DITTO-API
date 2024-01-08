from typing import Union
from fastapi import FastAPI
from utils.query import get_ditto_score

#  run me https://fastapi.tiangolo.com/#installation
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/var/{chromosome}-{position}-{ref}-{alt}")
def get_variant_score(chromosome, position, ref, alt):
    scores = get_ditto_score(chrom=chromosome, pos=position, ref=ref, alt=alt)
    return {"scores_by_transcript": scores}


@app.get("/hgvs/{hgvs_cdna}")
def get_hgvs_score(hgvs_cdna):
    # TODO call mapping API from VEP to convert to genomic coordinates
    # https://rest.ensembl.org/documentation/info/vep_hgvs_get
    # TODO call the lookup for a variant
    # scores = get_variant_score( stuff from vep for variant info on genome build)
    return {"variant": hgvs_cdna}
