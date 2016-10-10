# functions.py
# created on 2016-10-08 by Baptiste Colin
#
# collection of useful functions

import urllib
import json
import re
import HTMLParser

def getTitles(ID_list, keystring):
	# ID_list   : list of int
	# keystring : string
	#
	# output    : list of strings

	# Given a list of listing IDs, this function manages to get their titles,
	# stores them in a list and outputs it.

	res = []

	for ID in ID_list:
		
		rawTitle = getTitle(ID, keystring)

		# the getTitle function is built so that if the title couldn't
		# be retrieved, the output is -1.
		if (rawTitle == -1):
			# if the title couldn't be retrieved, well, too bad
			print("Listing #" + ID + " skipped")		
		else:
			# if it went ok, the title is stored in 'dirtyTitles.txt'
			res.append(rawTitle.encode('utf-8'))
			print(ID + " : " + rawTitle)

	return res
	
	# Ok, this part of the algorithm is taking forever because we are doing
	# one API request for each listing. That is not smart.
	# TODO : make it so we can retrieve as much listing titles at once
	#        each time we are making a request to the API. 


def getTitle (listing_id, keystring):
	# listing_id : int
	# keystring  : string
	#
	# output     : string / int
	
	# Given a listing ID and a key string, this function makes the necesary
	# HTTP calls and JSON exploitation in order to obtain the title of
	# the listing as it is outputed by the API.
	# If the title couldn't be retrieved, the function returns -1.
	# If the an error occured on the servr behalf, the ID is stored in
	# a file 'error_log.txt' for the user to make another download attempt.

	# first, we are defining the URL which is going to give us what we want
	url = "https://openapi.etsy.com/v2/listings/" + str(listing_id) + "?api_key=" + keystring

	# file in which failed downloads will be written down
	error_log = open('error_log.txt', 'a')

	# TODO : make it so this error log is processed, in order to make sure
	# 	 100% of listing IDs are retrieved


	# now we are accessing the API
	try:
		response = urllib.urlopen(url)
	except IOError:
		# sometimes an error occurs on the server behalf ...
		# if that's the case, we are writing down which ID couldn't
		# be retrieved in order to make another attempt later
		print('IO Error ! #' + listing_id)
		error_log.write(listing_id +'\n')
		return -1
		pass

	error_log.close()

	html = response.read()

	# at this point we have retrieved raw data about the listing.

	# let's load it as a dictionnary
	request_data = json.loads(html)	

	# here we're picking the information we are looking for
	try:
		listing_title = request_data['results'][0]['title']
	except KeyError:	
		# if the listing has no title, the function returns -1
		return -1
	
	# the outputed string is the title as it is outputed by the API.
	# please note that no cleaning has been performed at this point.
	return listing_title

def cleanList(title_list):
	# title_list : list of string
	#
	# output     : list of string

	# given a list of titles, this functions outputs a list of thoses same
	# titles after they've been cleaned up
	
	res = []

	for title in title_list:
		res.append(cleanTitle(title))

	return res


def cleanTitle(title):
	# title  : string
	#
	# output : string

	# given a title, this functions performs the necessary cleanup so that
	# it can be exploited later, then outputs the clean title.

	# here we define backslashed characters, for later removing purpose
	# unicode characters are *not* included in this list
	backslashed_characters = ['\n', '\t', '\r', '\b', '\'', '\"', '\\']

	res = title

	# the HTML parser input has to be only ASCII characters. Non-ASCII
	# characters will be replaced by single spaces.
	res = re.sub(r'[^\x00-\x7F]+',' ', res)
	

	# decoding HTML entities
	parser = HTMLParser.HTMLParser()
	res = parser.unescape(res)


	# converting all characters to lowercase
	res = res.lower()


	# replacing previously defined backslashed characters with single spaces
	for c in backslashed_characters:	
		res = res.replace(c,' ')

	
	#splitting the title into a token list
	word_list = res.split()

	new_word_list = []
	
	# let's process tokens one by one
	for w in word_list:
		# Removing leading or trailing non-alphanumerical characters.
		# The '\W' still lets a lot of non-alphanumerical characters
		# through, I had to add them by hand. There might be a better 
		# way to do it.
		a = w.strip('^\W,.~*%-()/!?+$')
			
		# the token is ignored if all characters are not alphanumerical
		if(not(re.match(r'^\W+$', a))):
			new_word_list.append(a)

	# now that tokens have been processed, a full string is re-built
	res = ' '.join(new_word_list)

	# replacing multiple spaces with a single space
	res = re.sub('\s+', ' ', res)

	return res

