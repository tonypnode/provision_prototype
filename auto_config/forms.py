from django import forms
from os import listdir as ls

class NewProvision(forms.Form):

    # TODO: Need to find a different way (prolly db) to get the sites,
    #       because each time a new file is added, the web needs to be restarted... not good
    sites = [[x, x.strip(' site data . json')] for x in ls('data_files/sites') if 'site_' in x]

    # TODO: Should this be in a DB somewhere?
    dev_functs = [
        ['AS', 'Access Switch', ],
        ['DS', 'Distro Switch'],
        ['R', 'Router']
        ]
    # TODO: The device function choice should also have the ability to modify the template
    #       that is chosen. Switches don't need routing config

    site = forms.ChoiceField(choices=sites)
    device_function = forms.ChoiceField(choices=dev_functs)
    device_function_count = forms.IntegerField(max_value=99, min_value=1)
