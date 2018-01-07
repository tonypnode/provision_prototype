from django import forms
from os import listdir as ls

class NewProvision(forms.Form):

    # TODO: Need to find a different way (prolly db) to get the sites,
    #       because each time a new file is added, the web needs to be restarted... not good
    sites = [[x, x.strip(' site data . json')] for x in ls('data_files/sites') if 'site_' in x]
    dev_functs = [
        ['AS', 'Access Switch', ],
        ['DS', 'Distro Switch'],
        ['R', 'Router']
        ]

    site = forms.ChoiceField(choices=sites)
    device_function = forms.ChoiceField(choices=dev_functs)
    device_function_count = forms.IntegerField(max_value=99, min_value=1)
