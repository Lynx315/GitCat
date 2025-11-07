import json
import urllib.request

def fetch_json(url):
    with urllib.request.urlopen(url) as response:
        return json.load(response)



def fetch_activity(username):
    events = fetch_json(f"https://api.github.com/users/{username}/events")
    for event in events[:10]:  # maximal 10 Events
        print(f"- {event['type']} at {event['repo']['name']}")
    

COMMAND_LIST = {
    "activity": fetch_activity
}
