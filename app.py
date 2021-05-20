import requests
import html
from prompt_toolkit import prompt, PromptSession, print_formatted_text
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

def main_toolbar():
    return HTML('CLI for <b><style bg="ansired">Reddit</style></b>')

def search_toolbar():
    return HTML('Subreddit <b><style bg="ansired">Search</style></b>')

def subreddit_search_toolbar():
    return HTML('Subreddit <b><style bg="ansired">Search</style></b>')

if __name__ == "__main__":
	session = PromptSession()
	while True:
		# pre-process command
		command = session.prompt("> ", bottom_toolbar=main_toolbar)
		command = command.strip()
		if len(command) == 0:
			continue
		command_arr = command.split(" ")
		# search for subreddit
		if command_arr[0] == 's' or command_arr[0] == 'search':
			if len(command_arr) == 1:
				text = session.prompt("Subreddit search: ", bottom_toolbar=search_toolbar)
				param = {'q': text, 'limit': 15, 'sort': 'relevance'}
			else:
				param = {'q': ' '.join(command_arr[1:]), 'limit': 15, 'sort': 'relevance'}
			values = commands.search(param)
			data = values['data']['children']
			for i in range(len(data)):
				print(data[i]['data']['display_name'])
		# search within specified subreddit
		elif command_arr[0] == 'ss' or command_arr[0] == 'subreddit-search':
			if len(command_arr) == 1:
				subreddit = session.prompt("Search in subreddit: ", bottom_toolbar=subreddit_search_toolbar)
			else:
				subreddit = ' '.join(command_arr[1:])
			mode = session.prompt("Select mode (hot, new, top): ", bottom_toolbar=subreddit_search_toolbar)
			if mode != 'hot' and mode != 'new' and mode != 'top':
				print_formatted_text(HTML('<style bg="ansired">Default to hot</style>'))
				mode = 'hot'
			param = {'limit': 15}
			if mode == 'top':
				param['t'] = 'week'
			values = commands.subreddit_search(subreddit, mode, param)
			data = values['data']['children']
			for i in range(len(data)):
				print_formatted_text(HTML('<b><u><ansired>' + html.unescape(data[i]['data']['title']) + '</ansired></u></b>'))
				print(data[i]['data']['url'])
				print(html.unescape(data[i]['data']['selftext'].strip()))
		# help command
		elif command_arr[0] == 'h' or command_arr[0] == 'help':
			if len(command_arr) == 1:
				print('Type \'search\' or \'s\' to search for a subreddit.')
				print('Type \'subreddit-search\' or \'ss\' to search within a subreddit.')
				print('Type \'quit\' or \'q\' to quit the CLI.')
		# quit command
		elif command_arr[0] == 'q' or command_arr[0] == 'quit':
			break
		else:
			print("Invalid command.")



