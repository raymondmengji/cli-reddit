import requests
import app

# api request for relevant subreddits
def search(param):
    response = requests.get(app.API_URL + '/subreddits/search', headers=app.HEADER, params=param)
    return response.json()
# api request for posts in specified subreddit
def subreddit_search(subreddit, mode, param):
    url = subreddit + "/" + mode
    if 't' in param:
        url += "/?t=" + param['t']
    print("Searching: reddit.com/r/" + url + "...")
    response = requests.get(app.API_URL + '/r/' + subreddit + '/' + mode, headers=app.HEADER, params = param)
    return response.json()
    