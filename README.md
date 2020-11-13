# awstags

A set of helpers and a cli that uses boto3's `resourcegroupstaggingapi` to grab all resources and associated tags. `res2csv` gets all resources and tags and outputs a csv. 

## Installation
install the library and related clis. Requires > python 3. 

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

Developed with POETRY for package management. There's some sanity checking doctests in the module. This is really just an example. Extend or augment at will.
