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

## Contributing

We welcome contributions! [See the docs for guidelines](./CONTRIBUTING.md).

## Contact information

For issues, please send an email with clear description to

|Name | Email |
|------|--------|
|Tarun Mamidi | <tmamidi@uab.edu>|
|Brandon Wilk | <bwilk777@uab.edu>|
