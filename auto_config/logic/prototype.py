import json
from os import listdir as ls

# universal_data = json.load(open('data_files/universal_data.json'))
# site_data = json.load(open('../../data_files/sites/site_aaa_data.json'))
# region_data = json.load(open('../../data_files/regions/region_1_data.json'))


def site_selection():
    """
    Selection method to get the site information

    :return:

    """
    files = [x.strip(' site data . json') for x in ls('data_files/sites') if 'site_' in x]
    return files


"""
data = {
    'universal_data': {
        'username': universal_data['data']['username'],
        'password': universal_data['data']['password'],
        'snmp_username': universal_data['data']['snmp_username'],
        'snmp_authpass': universal_data['data']['snmp_authpass'],
        'snmp_privpass': universal_data['data']['snmp_privpass'],
        'domain_name': universal_data['data']['domain_name']
    },
    'device_data': {
        'enclave': 'G',
        'function': '[FUNCTION_ID]',
        'function_count': '[COUNT]',
        'management_interface': {
            'name': 'MGMT_INT_NAME',
            'ip_addr': 'X.X.X.X',
            'subnet_mask': 'X.X.X.X',
        }
    },
    'region_data': {
        'id': region_data['data']['ID'],
        'logging': region_data['data']['Logging_Server'],
        'aaa_servers': region_data['data']['AAA_Servers'],
    },
    'site_data': {
        'id': site_data['data']['ID'],
        'local_acl_subnets': {
            'data': site_data['data']['data_subnets'],
            'management': site_data['data']['mgmt_subnets'],
        }
    }
}

"""