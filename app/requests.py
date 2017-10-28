import urllib.request,json
##import a class from models eg from .models import Movie

# Getting api key
api_key = None

# Getting the  base url
base_url = None

def configure_request(app):
    global api_key,base_url
    '''
    Here we can import  below and below is just but an example 
    if u dont need them you can remove them
    '''
     api_key = app.config['API_KEY']
    base_url = app.config['BASE_UL']
