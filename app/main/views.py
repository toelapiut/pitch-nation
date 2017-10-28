from flask import render_template,request,redirect,url_for
from . import main
##remember to import classes from ..requests
from .forms import ReviewForm

'''
We then define our route decorators using the 
main blueprint instance instead of the app instance
'''
@main.route('/')
def index():
    #.......