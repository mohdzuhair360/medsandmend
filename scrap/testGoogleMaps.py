import requests
from Key_API import key

search_url ="https://maps.googleapis.com/maps/api/place/textsearch/json"
details_url ="https://maps.googleapis.com/maps/api/place/details/json"

userInput = 'noExit'
while userInput != 'exit':
    query = input('Enter search : ')
    #store = "guardian "+ query
    try:
        search_payload = {"key": key, "query": query}
        #print("search_payload : " + str(search_payload))
        search_req= requests.get(search_url, params=search_payload)
        #print("search_req : " + str(search_req))
        search_json = search_req.json()
        #print("search_json : " + str(search_json))
        place_id = search_json["results"][0]["place_id"]
        #print("place_id : " + str(place_id))
        details_payload = {"key": key,"place_id" : place_id}
        #print("details payload : " + str(details_payload))
        details_resp = requests.get(details_url, params=details_payload)
        #print("detail resp : " + str(details_resp))
        details_json = details_resp.json()
        #print("details json : " + str(details_json))

        url = details_json["result"]["url"]
        print("url : " + str(url))

    except IndexError:
        print ("No result")