# real-estate-analysis

## Overview
This package contains tools to analyze real estate property.

The analysis tools are broadly split into two segments:
1) Property Analysis - tools to understand the value of an individual property.
This includes:
- Mortage calculator
- Return on Investment estimation
- Return on Equity estimation

2) Exploratory Analysis
This segment contains tools to parse and explore real estate data sets.

## Setup
```
python -m virtualenv venv
source venv/bin/activate
python setup.py install
```

## Execution
### Scripts

### Flask applications
export FLASK\_APP=apps/current\_listings.py
flask run

## Teardown
```
deactivate
rm -rf venv
```
