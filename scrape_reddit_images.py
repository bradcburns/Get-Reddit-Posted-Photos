#!/usr/bin/env python

import argparse
import sys
import requests

def get_comments(user):
	StrRequestHeaders = {'user-agent':'https://github.com/bradcburns/Get-Reddit-Posted-Photos/'}
	StrCommentsAPIURL = ("http://reddit.com/" +
		"user/" + user + "/comments.json")

	r = requests.get(StrCommentsAPIURL,headers=StrRequestHeaders)

	if r.status_code == 404:
		raise Exception('user ' + user + ' was not found in Reddit. ' +
			'Verify the spelling and try again.')

	JsonResponse = r.json()

	#Yes, Reddit calls it a "thing", the following variable name isn't just a
	#lazy naming convention on my part.

	JsonResponseNextThing = JsonResponse['data']['after']

	while JsonResponseNextThing:
		r = requests.get(StrCommentsAPIURL,headers=StrRequestHeaders,params={'after':JsonResponseNextThing})

		print r.text

		JsonResponse = r.json()

		JsonResponseNextThing = JsonResponse['data']['after']

	print 'done'


def verify_args(args):
	return True

def parse_args():
	
	StrProgramDescrip = ("scrape_reddit_images is a script "
		"which will return the images a reddit user has posted "
		"in both comments and submissions. It can output as an "
		"HTML page or a csv of links. Append the --help "
		"argument to see usage.\n \n"
		"scrape_reddit_images was written by Brad Burns and is "
		"released under the MIT License.\n\n"
		"https://github.com/bradcburns\n"
		"https://www.linkedin.com/in/bradleycburns\n")

	StrUsageExample = ("example:"
		"scrape_reddit_images.py -u Karmanaut "
		"--output html")

	parser = argparse.ArgumentParser(
		description=StrProgramDescrip,
		epilog=StrUsageExample)

	parser.add_argument(
		'--user',
		'-u',
		help='full name of the user whose images you want to scrape.',
		required=True)

	parser.add_argument(
		'--output',
		'-o',
		help='format in which to output images. defaults to html.',
		default='html',
		choices=['html','csv'])

	ret = parser.parse_args()

	return ret

def main():
	args = parse_args()
	if not verify_args(args):
		raise Exception('A command-line argument is missing or '
			'improperly entered. Use the --help argument and '
			'verify your usage.')

	get_comments(args.user)


if __name__ == "__main__":
	main()
