'''
A starter file for testing a Flask app
Run with:
python -m unittest Tests/flask_tests.py
'''
from app import*
import unittest


class TestSOMETHING(unittest.TestCase):
    def test_route(self):
        #sets up a special test app
        self.app = app.test_client() 
        #test app returns TestResponse object
        response = self.app.get('/', follow_redirects=True) 
        #TestResponse has webpage in .data
        self.assertEqual(b'Hello, this is the homepage regarding the data of water around the world!', response.data) 

    def test_valid_country_valid_year(self):
        """Test that for a valid country and valid year it returns the correct information for the specific country and year"""
        self.app = app.test_client() 
        response = self.app.get('/France/2015/', follow_redirects=True) 
        #TestResponse has correct information for specific country and year in .data
        expected = b"[['France', '2015', '1826', '64 916', '80', '>99', '<1', '<1', '<1', '0.00', '>99', '<1', '<1', '<1', '0.00', '>99', '<1', '<1', '<1', '0.00', '', '98', '>99', '-', '98', '0.00', '>99', '<1', '99', '>99', '-', '99', '0.12', '>99', '<1', '99', '>99', '-', '99', '0.10', '>99', '<1', 'Europe and Northern America', '-', '-', '-', '-', 'High income']]"
        self.assertEqual(expected, response.data)

    def test_valid_region_valid_year(self):
        """Test that for a valid region and valid year it returns the correct information for the specific region and year"""
        self.app = app.test_client()
        response = self.app.get('/Sub-Saharan Africa/2019/', follow_redirects=True) 
        #TestResponse has correct information for specific region and year in .data 
        self.assertEqual(b"[['Sub-Saharan Africa', '2019', '1 096 034', '41', '48', '16', '24', '12', '0.95', '85', '9', '5', '1', '0.35', '63', '13', '16', '8', '0.93', '', 'Sub-Saharan Africa', '2019', '14', '14', '46', '22', '0.43', '21', '43', '51', '52', '66', '51', '0.40', '58', '35', '29', '29', '54', '34', '0.60', '36', '40', '195']]", response.data)

    def test_invalid_location(self): 
        """Tests that for an invalid location it returns an appropriate error"""
        self.app = app.test_client() 
        response = self.app.get('/notalocation/2015/', follow_redirects=True) 
        #TestResponse has the correct error message in .data
        self.assertEqual(b'Error: Country or region not found, please try again.', response.data)

    def test_invalid_year(self):
        """Tests that for an invalid year it returns an appropriate error"""
        self.app = app.test_client() 
        response = self.app.get('/France/10/', follow_redirects=True) 
        #TestResponse has the correct error message in .data
        self.assertEqual(b'Year outside range, please specify a year in the range 2000-2024', response.data)

    def test_valid_year(self):
        """Tests that for a valid year it returns the correct information for that specific year"""
        self.app = app.test_client() 
        response = self.app.get('/year/2015', follow_redirects=True)
        #TestResponse has correct information for specific year in .data
        self.assertIn("2015", response.get_data(as_text=True))