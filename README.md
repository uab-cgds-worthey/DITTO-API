# DITTO-API

<!-- markdown-link-check-disable -->
[![Perform linting -
Markdown](https://github.com/uab-cgds-worthey/DITTO-API/actions/workflows/linting.yml/badge.svg)](https://github.com/uab-cgds-worthey/DITTO-API/actions/workflows/linting.yml)
<!-- markdown-link-check-enable -->

***!!! For research purposes only !!!***

Repo for querying DITTO predictions for variants using FastAPI.

## Requirements

Following are required:

- [git](https://git-scm.com/downloads)
- python3.7+
- [Docker](https://www.docker.com/products/docker-desktop)

## Installing

*1.* Clone the repository - change in to directory of your choice and run:

```sh
git clone https://github.com/uab-cgds-worthey/DITTO-API.git
```

*2.* Navigate to the project directory

```sh
cd DITTO-API
```

*3.* Build the Docker image

```sh
docker build -t ditto-api .
```

*4.* Run the Docker container

```sh
docker run -p 8000:8000 --name ditto-api ditto-api
```

*5.* Use this link in your browser to retrieve DITTO scores

<!-- markdown-link-check-disable -->
<http://localhost:8000/docs>
<!-- markdown-link-check-enable -->
 and use this variant as example: 1-2406483-C-G

## Expected result

DITTO will output deleterious score by Ensemble transcript. Below is the output for the above test variant. To verify
the scores, please query the variant in the [DITTO web app](https://cgds-ditto.streamlit.app/).

```sh
{
  "scores_by_transcript": {
    "ENST00000288774.7": {
      "gene": "PEX10",
      "consequence": "intron_variant,splice_site_variant",
      "chrom": "chr1",
      "pos": "2406483",
      "ref_base": "C",
      "alt_base": "G",
      "DITTO": "1.0"
    },
    "ENST00000447513.6": {
      "gene": "PEX10",
      "consequence": "intron_variant,splice_site_variant",
      "chrom": "chr1",
      "pos": "2406483",
      "ref_base": "C",
      "alt_base": "G",
      "DITTO": "1.0"
    },
    "ENST00000507596.5": {
      "gene": "PEX10",
      "consequence": "intron_variant,splice_site_variant",
      "chrom": "chr1",
      "pos": "2406483",
      "ref_base": "C",
      "alt_base": "G",
      "DITTO": "1.0"
    },
    "ENST00000510434.1": {
      "gene": "PEX10",
      "consequence": "2kb_downstream_variant,NMD_transcript_variant",
      "chrom": "chr1",
      "pos": "2406483",
      "ref_base": "C",
      "alt_base": "G",
      "DITTO": "1.0"
    },
    "ENST00000378513.7": {
      "gene": "RER1",
      "consequence": "2kb_downstream_variant",
      "chrom": "chr1",
      "pos": "2406483",
      "ref_base": "C",
      "alt_base": "G",
      "DITTO": "1.0"
    },
    "ENST00000605895.6": {
      "gene": "RER1",
      "consequence": "2kb_downstream_variant",
      "chrom": "chr1",
      "pos": "2406483",
      "ref_base": "C",
      "alt_base": "G",
      "DITTO": "1.0"
    }
  }
}
```

## Contributing

We welcome contributions! [See the docs for guidelines](./CONTRIBUTING.md).

## Contact information

For issues, please send an email with clear description to

|Name | Email |
|------|--------|
|Tarun Mamidi | <tmamidi@uab.edu>|
|Brandon Wilk | <bwilk777@uab.edu>|
