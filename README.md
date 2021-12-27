
## Setup
This package developed using Python 3.9.

To set up this project on your local machine:
1. Clone this repository.
2. this package requires two directories to be created in your project dir: input and output
3. input directory contains input data file bmi.json
## Directory structure
bmicalc/
    ├── src/
    |    ├── bmicalc/
    |          ├── __init__.py
    |          ├── bmicalc.py
    |          └── mainapp.py
    └── bmicalctest/
    |    ├── input/
    |    |    └── bmi_test.json
    |    ├── output/
    |    ├── __init__.py
    |    ├── test_bmicalc.py
    |    ├── test_mainapp.py
    |    └── testdata.py
    └── testpackage.py
    ├── input/
    |     └── bmi.json
    └──output/
## Running tests
Run tests simply using the `pytest` command just above the 'bmicalctest'
Also `pytest` can be run from testpackage.py


