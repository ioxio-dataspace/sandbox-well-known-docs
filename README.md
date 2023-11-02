# Documentation for .well-known endpoints on dataspaces

This repository is used to document the different .well-known URLs and data objects
used on dataspaces and to convert and host those as a human friendly web page.

Documentation hosted on [docs.ioxio.dev/schemas/](https://docs.ioxio.dev/schemas/)

## Structure

- [`./src/`](./src/) - Source files containing
  Python/[Pydantic](https://pydantic-docs.helpmanual.io/) models describing the
  different .well-known URLs and the data they contain.
- [`./schemas/`](./schemas/) - Intermediate JSON Schema files generated from the above
  by the tooling provided in this repo.
- [`./html/`](./html/) - Final static files generated by the tooling that are hosted
  using GitHub pages.
- [`./main.py`](./main.py) - The converter used to convert the source files to JSON
  Schema and HTML + CSS + JS.
- [`./.github/workflows/deploy.yaml`](./.github/workflows/deploy.yaml) - GitHub Action
  to build and deploy to GitHub Pages.

## Development

Generic pre-requisites for development

- [Pre-commit](https://pre-commit.com/#install)
- [Python >= 3.9](https://python.org)
- [Poetry](https://python-poetry.org/docs/#installation)

Install dependencies with:

```shell
poetry install
```

## Usage

These source files can be converted to HTML files by running:

```shell
poetry run convert-src-to-html
```

## Testing locally

```shell
cd html
python -m http.server
```

Then check the files at: http://localhost:8000/

## Adding new files

In order to add new files to the documentation:

1. Add a new `.py` file in [./src](./src).
2. Define Python/pydantic model(s) in the file.
3. Assign the class you want to be documented to the `ROOT` variable.
