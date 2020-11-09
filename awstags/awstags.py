def flatten_resource_to_dict(resource_dict):
    """ returns a list of dicts of resources. Easier to turn into a csv

    ## Example
    >>> r = sample_data().get('ResourceTagMappingList')[0] 
    >>> flattened = flatten_resource_to_dict(r)
    >>> flattened['key1']
    'value1'
    """

    resource = {}
    resource['_ResourceARN'] = resource_dict.get('ResourceARN')
    for tag in resource_dict.get('Tags'):
        resource[tag.get('Key')]= tag.get('Value')
    return resource

def get_headers(list_of_resources):
    """Returns a list of sorted keys from simplifeid dict of resources. These can be used as headers. 
    
    ## Example
    >>> res = [{'key':'1', 'key2':'2', 'key3':'3'}, 
    ...          {'key1':'1-2', 'key3':'1-3', 'key2':'1-2'}
    ...       ]
    >>> k = get_headers(res)
    >>> print(k)
    ['key', 'key1', 'key2', 'key3']
    """
     
    keys = list(set([key for resource in list_of_resources for key in resource.keys()]))
    keys.sort()
    return keys

def flatten_all_resources(resources):
    """ flattens resources into a simple list of dicts. This will allow for easier processing based
    on key name. 
    >>> flat_resources = flatten_all_resources(sample_data())
    >>> print(len(flat_resources))
    2
    >>> print(flat_resources[0])
    {'_ResourceARN': 'resourcevalue', 'key1': 'value1', 'key2': 'value2'}
    """
     
    return [flatten_resource_to_dict(resource) for resource in resources.get('ResourceTagMappingList')]

def get_all_resources(profile):
    """Uses boto3 to page through all results and create a list of dicts"""
    import boto3
    #setup the boto3 client (note this assumes you've authenticated via aws-adfs
    session = boto3.session.Session(profile_name=profile)
    client = session.client('resourcegroupstaggingapi')
    resources = client.get_resources(ResourcesPerPage=100)
    flat_resources = flatten_all_resources(resources) 
    #get the pagination token 
    pagination_token = resources.get('PaginationToken')

    p = 1
    while pagination_token:
        resources = client.get_resources(ResourcesPerPage=100, PaginationToken=pagination_token)
        flat_resources.extend(flatten_all_resources(resources))
        pagination_token = resources.get('PaginationToken')
        p = p+1
        print(p)
    return flat_resources
     

     

def to_normalized_list(resource_dict_list, headers):
    """saves as a csv
    >>> res_dict = flatten_all_resources(sample_data())
    >>> headers = get_headers(res_dict)
    >>> l = to_normalized_list(res_dict, headers)
    >>> print(l[1])
    ['resourcevalue', 'value1-2', 'value2-2', 'value3-2']
    >>> len(l[1])==len(l[0])
    True
    >>> len(l[1])==len(headers)
    True
    """

    resources = [[r.get(h) for h in headers] for r in resource_dict_list]
    return resources

def sample_data():
    """ sample data for testing"""
    data = {
            "ResourceTagMappingList": [
                { 
                    "ResourceARN": "resourcevalue",
                    "Tags": [
                        {"Key": "key1", "Value": "value1"}, 
                        {"Key": "key2", "Value": "value2"}
                        ]
                    },
               { 
                    "ResourceARN": "resourcevalue",
                    "Tags": [
                        {"Key": "key1", "Value": "value1-2"}, 
                        {"Key": "key2", "Value": "value2-2"},
                        {"Key": "key3", "Value": "value3-2"}
                    ]
                }
            ]
            }

    return data


