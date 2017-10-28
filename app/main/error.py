from flask import render_template
from . import main 

'''
To use application-wide error handler
 we must use the app_errorhandler() decorator.
'''
@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404