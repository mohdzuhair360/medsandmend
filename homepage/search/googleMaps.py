from bs4 import BeautifulSoup as soup
import requests
from .mapsAPIKey import key
from django.shortcuts import render,get_object_or_404
from homepage import models
#from HTMLParser import HTMLParser
from . import guardianDescription
import csv
from datetime import datetime

class guardianMapsEngine:

    def locateIt(self, user_location):

        search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        details_url = "https://maps.googleapis.com/maps/api/place/details/json"
        page = get_object_or_404(models.PageSource, pk=1)
        print()
        print ("Page = " + str(page))
        print()

        query ="guardian " + user_location
        try:
            search_payload = {"key": key, "query": query}
            # print("search_payload : " + str(search_payload))
            search_req = requests.get(search_url, params=search_payload)
            # print("search_req : " + str(search_req))
            search_json = search_req.json()
            # print("search_json : " + str(search_json))
            place_id = search_json["results"][0]["place_id"]
            # print("place_id : " + str(place_id))
            details_payload = {"key": key, "place_id": place_id}
            # print("details payload : " + str(details_payload))
            details_resp = requests.get(details_url, params=details_payload)
            # print("detail resp : " + str(details_resp))
            details_json = details_resp.json()
            # print("details json : " + str(details_json))

            store_location = details_json["result"]["url"]
            print("url : " + str(store_location))

            #item_instance = models.Location.objects.create(page = page,
                                                            #store_location = store_location)

        except IndexError:
            print("No result")

        return str(store_location)
