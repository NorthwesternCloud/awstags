"""s3tags

Usage: 
    s3tags -b <bucket> -p <prefix> [-missing-tags]

Options:
    -b <bucket>     Bucket
    -p <prefix>     Prefix 
    -m --missing-tags  only show missing tags

Description:
stitches together s3 object and object tags

"""

import docopt
import boto3
import json

def main():
    args = docopt.docopt(__doc__)
    session= boto3.Session()
    s3 = session.resource('s3')
    client = boto3.client('s3')
    bucket=s3.Bucket(args['-b'])

    resources = [
            {"s3key":o.key, "tags": client.get_object_tagging(Bucket=args['-b'], Key=o.key)['TagSet']} 
            for o in bucket.objects.filter(Prefix=args['-p']) 
            if "." in o.key]

    # if missing tags is flipped, filter  
    if args['--missing-tags']:
        resources = [r for r in resources if len(r['tags'])==0]

    print(json.dumps(resources))
if __name__ == '__main__':
    main()

