#!/usr/bin/env python

import argparse
import sys

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


if __name__ == "__main__":
	main()
