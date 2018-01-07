from django.shortcuts import render, HttpResponse
from .forms import NewProvision
import json
# Create your views here.


def home(request):
    form = NewProvision()
    return render(request, 'home.html', {'provision_form': form})


def new_provision(request):
    universal_data = json.load(open('data_files/universal_data.json'))
    site_data = json.load(open('data_files/sites/' + request.POST['site']))
    region_data = json.load(open('data_files/regions/region_' + str(site_data['data']['RegionID']) + '_data.json'))
    hostname_calc = str(site_data['data']['ID'] + region_data['data']['ID'])
    funct_count = str(request.POST['device_function_count'])
    dev_funct = str(request.POST['device_function'])
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
            'function': dev_funct,
            'function_count': funct_count,
            'hostname': hostname_calc,
            'management_interface': {
                'name': 'MGMT_INT_NAME',
                'ip_addr': 'X.X.X.X',
                'subnet_mask': 'X.X.X.X',
            }
        },
        'region_data': {
            'ID': region_data['data']['ID'],
            'logging': region_data['data']['Logging_Server'],
            'aaa_servers': region_data['data']['AAA_Servers'],
        },
        'site_data': {
            'ID': site_data['data']['ID'],
            'local_acl_subnets': {
                'data': site_data['data']['data_subnets'],
                'management': site_data['data']['mgmt_subnets'],
            }
        }
    }

    return render(request, 'universal_base.j2', context=data, content_type='text/plain')
