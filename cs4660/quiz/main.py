"""
quiz2!

Use path finding algorithm to find your way through dark dungeon!
"""

import json

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(state_id):
    """
    get state and its neighbor
    """
    body = {'id': state_id}
    return json_request(GET_STATE_URL, body)

def transition_state(state_id, action):
    """
    transition from the state_id with action (display event)
    """
    body = {'id': state_id, 'action': action}
    return json_request(STATE_TRANSITION_URL, body)

def json_request(target_url, body):
    """
    helper method to send json request and parse response json
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = json.load(urlopen(req, jsondataasbytes))
    return response

if __name__ == "__main__":
    empty_room = get_state('10a5461773e8fd60940a56d2e9ef7bf4')
    print(empty_room)
    print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))
