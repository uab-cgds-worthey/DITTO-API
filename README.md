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
- python3.7+  & [python virtual environment](https://docs.python.org/3/tutorial/venv.html)
- pip3

## How to install

Installation simply requires fetching the source code.

To fetch source code, change in to directory of your choice and run:

```sh
git clone https://github.com/uab-cgds-worthey/DITTO-API.git
```

Change in to root directory and run the command below to install environment:

```sh
# Create an environment. Needed only the first time.
python3 -m venv ditto-api-env
source ditto-api-env/bin/activate
pip3 install -r requirements.txt
```

## How to run

Run the below command to activate the API

```sh
cd src
uvicorn main:app --reload
```

Test the app using this example as web address - <http://127.0.0.1:8000/docs>
 and use this variant as example: 1-2406483-C-G

## Contributing

We welcome contributions! [See the docs for guidelines](./CONTRIBUTING.md).

## Contact information

For issues, please send an email with clear description to

|Name | Email |
------|--------|
Tarun Mamidi | <tmamidi@uab.edu>
Brandon Wilk | <bwilk777@uab.edu>
