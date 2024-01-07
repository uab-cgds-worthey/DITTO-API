from typing import Union
from fastapi import FastAPI
from utils.query import get_ditto_score

#  run me https://fastapi.tiangolo.com/#installation
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/loc/{chromosome}/{start}/{end}")
def get_scores(chromosome: str, start: int, end: int):
    # TODO create interface to tabix to query range for DITTO scores
    return {"loc": f"{chromosome}:{start}-{end}"}


@app.get("/var/{chromosome}/{position}/{ref}/{alt}")
def get_variant_score(chromosome, position, ref, alt):
    # TODO call the get_scores function to perform look up, if score not precomputed then call dynamic generation
    scores = get_ditto_score(chrom=chromosome, pos=position, ref=ref, alt=alt)
    # return {"variant": f"chr{chromosome}:g.{position}{ref}>{alt}"}
    return {"scores": scores}


@app.get("/hgvs/{hgvs_cdna}")
def get_hgvs_score(hgvs_cdna):
    # TODO call mapping API from VEP to convert to genomic coordinates
    # https://rest.ensembl.org/documentation/info/vep_hgvs_get
    # TODO call the lookup for a variant
    # scores = get_variant_score( stuff from vep for variant info on genome build)
    return {"variant": hgvs_cdna}
