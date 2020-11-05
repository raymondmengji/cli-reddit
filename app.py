import requests
from prompt_toolkit import prompt, PromptSession
from auth import SECRET_ID, SECRET_KEY
import commands

# Reddit API Authentication/Setup
base_url= 'https://www.reddit.com'
data = {'grant_type': 'https://oauth.reddit.com/grants/installed_client', 'device_id': 'DO_NOT_TRACK_THIS_DEVICE'}
header = {'User-agent': 'your bot 0.1'}
auth = requests.auth.HTTPBasicAuth(SECRET_ID, SECRET_KEY)
r = requests.post(base_url + '/api/v1/access_token', 
                    data=data,
                    headers = header,
                    auth=auth)
d = r.json()

token = 'bearer ' + d['access_token']
API_URL = 'https://oauth.reddit.com'
HEADER = {'Authorization': token, 'User-agent': 'your bot 0.1'}


if __name__ == "__main__":
	session = PromptSession()
	while True:
		command = session.prompt(">")
		# print("command entered:", command)
		if command == 's':
			text = session.prompt("Subreddit search: ")
			param = {'q': text, 'limit': 5, 'sort': 'relevance'}
			# print(param)
			commands.search(param)
		elif command == 'q':
			break


