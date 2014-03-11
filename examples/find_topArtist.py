import json
import requests

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    url='http://ws.audioscrobbler.com/2.0/?method=geo.getTopArtist&api_key=195b7d1161093ce8038a32673aa42460&country=spain&limit=1'
    data = requests.get(url).text
    data = json.loads(data)
    #print type(data)
    #print(data['topartists']['artist'][0]['name'])
    return (data['topartists']['artist'][0]['name'])  # return the top artist in Spain
