from flask import Flask
import csv
from ProductionCode.command_line import *

app = Flask(__name__)
PORT = 5100
loadData()
data = []

@app.route('/')
def homepage():
    return "Hello, this is the homepage regarding the data of water around the world!"

@app.route('/<string:location>/<string:year>/')
def get_location_year(location: str, year: int) -> str:
    """Get and display the data from API for a specific location(country/region) and year"""
    inputted_location_year = getData(location.strip(), year)
    return str(inputted_location_year)

@app.route('/year/<string:year>/')
def get_year(year:str) -> str: 
    '''Get and display the data from API for all locations in specific year'''
    inputted_year_only = getData(None,year.strip())
    return str(inputted_year_only)

@app.errorhandler(404)
def page_not_found(e):
    """Display error message if route not found"""
    return "ERROR 404: Page not found. See README.md for details on route syntax."

if __name__ == '__main__':
    app.run(port=PORT)