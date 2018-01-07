from django import forms
from os import listdir as ls

class NewProvision(forms.Form):

    # TODO: Need to find a different way (prolly db) to get the sites,
    #       because each time a new file is added, the web needs to be restarted... not good
    sites = [[x, x.strip(' site data . json')] for x in ls('data_files/sites') if 'site_' in x]
    your_name = forms.CharField(label='Your name', max_length=100)
    site = forms.ChoiceField(choices=sites)
