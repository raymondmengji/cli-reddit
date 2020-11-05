from setuptools import setup, find_packages

setup(
	name="cli-reddit",
	description="A command line interface for Reddit!",
	author="Raymond Ji",
	version="0.01",
	packages=find_packages(),
	entry_points={
		'console_scripts': [
			'cli-reddit = '
		]
	}
)