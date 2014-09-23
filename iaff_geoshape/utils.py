import json
import requests

def get_json_response(url):
    """
    Makes a GET request to the URL and returns a dict of the response.
    """
    response = requests.get(url)
    return json.loads(response.content)
