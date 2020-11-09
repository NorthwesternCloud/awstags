"""res2csv

Usage: 
    res2csv -p <profile> <output>

Options:
    -p --profile <profile>      Name of aws profile e.g. "default" or "staging" 

Description:
Uses the resourcegroupstaggingapi to grab a list of resources with tags and outputs to a csv.
"""

import docopt
import awstags

def main():
    args = docopt.docopt(__doc__)
    resources = awstags.get_all_resources(args['--profile'])
    headers = awstags.get_headers(resources)
    awstags.save_as_csv(headers, awstags.to_normalized_list(resources, headers), args['<output>'])

if __name__ == '__main__':
    main()

