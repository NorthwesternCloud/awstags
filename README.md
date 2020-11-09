# awstags

A set of helpers and a cli that uses boto3's `resourcegroupstaggingapi` to grab all resources and associated tags. 

## Installation
install the library and related clis.

`pip install git+https://github.com/davidschober/awstags.git`


## res2csv 
```
res2csv --help 

Usage:
    res2csv -p <profile> <output>

Options:
    -p --profile <profile>      Name of aws profile e.g. "default" or "staging"
```

## Development
Developed with POETRY for package management.
