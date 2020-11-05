import requests
from prompt_toolkit import prompt, PromptSession
from prompt_toolkit.formatted_text import HTML
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

def search_toolbar():
    return HTML('Subreddit <b><style bg="ansired">Search</style></b>')

def main_toolbar():
    return HTML('CLI for <b><style bg="ansired">Reddit</style></b>')

if __name__ == "__main__":
	session = PromptSession()
	while True:
		command = session.prompt("> ", bottom_toolbar=main_toolbar)
		# print("command entered:", command)
		if command == 's' or command == 'search':
			text = session.prompt("Subreddit search: ", bottom_toolbar=search_toolbar)
			param = {'q': text, 'limit': 5, 'sort': 'relevance'}
			# print(param)
			commands.search(param)
		elif command == 'h' or command == 'help':
			print('Type \'search\' or \'s\' to search for a subreddit.')
			print('Type \'quit\' or \'q\' to quit the CLI.')
		elif command == 'q' or command == 'quit':
			break
		else:
			print("Invalid command.")



