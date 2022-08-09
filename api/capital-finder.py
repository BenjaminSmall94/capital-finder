from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        url_components = parse.urlsplit(self.path)
        query_strings = parse.parse_qsl(url_components.query)
        query_dict = dict(query_strings)
        message = ""
        if "country" in query_dict:
            url = f"https://restcountries.com/v2/name/"
            response = requests.get(url + query_dict['country'])
            data = response.json()
            message = f"The capital of {query_dict['country']} is {data[0]['capital']}"
        elif "capital" in query_dict:
            url = f"https://restcountries.com/v3.1/capital/{query_dict['capital']}"
            response = requests.get(url)
            data = response.json()
            message = f"{query_dict['capital']} is the capital of {data[0]['name']['common']}"

        self.wfile.write(message.encode())
        return
