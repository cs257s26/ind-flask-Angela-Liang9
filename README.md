# README

Individual Flask project.
Configure the port with the variable PORT in app.py

## How to Use: 

To display water data for all locations in a specific year, enter http://127.0.0.1:PORT/year/YEAR
For example: http://127.0.0.1:PORT/year/2005

To display water data for a specific location and year, enter http://127.0.0.1:PORT/LOCATION/YEAR
For example: http://127.0.0.1:PORT/France/2015

## To Run Individual Tests: 
run: 
python -m unittest discover -s Tests

