# functions2.py
# created on 2016-10-09 by Baptiste Colin
#
# collection of useful functions

from math import log

def createTokenList(title_list):
	# title_list : list of strings
	# 
	# output     : list of strings

	# Given a list containing all the titles, this functions will build
	# a list containing all the tokens appearing at least once in a title.
	# A token present in several titles would appear only once in the
	# outputed list.

	res = set([])

	# titles are being processed one by one
	for title in title_list:
		
		# each title is splitted into a list of its tokens
		tokens = title.split()

		# each token is added to the set. If it's already in the set,
		# it won't be added a second time.
		for t in tokens:
			res.add(t)

	# the set is converted back into a list
	res = list(res)

	return res


def entropy(dataset, class_A, class_B):
	# dataset : set of strings
	# class_A : set of strings
	# class_B : set of strings
	#
	# output  : float

	# Given a dataset (listing titles) and 2 sets of values corresponding to 
	# class A and class B, this function computes the entropy of the dataset 
	# with respect to class A and class B
	# TODO : modifications could be performed in order to compute entropy
	#	 when there are more than 2 outcomes
	
	# computing the proportion of elements of A (a) and elements of B (b)
	dataset_A = set(dataset).intersection(class_A)
	dataset_B = set(dataset).intersection(class_B)
	
	a = float(len(dataset_A))/float(len(dataset))
	#b = len(dataset_B)./len(dataset)
	b = 1-a # in our particular case, an element is either part of class A
		# or part of class B, so this simpler formula is correct

	# This is all the information we need to compute the entropy.
	# We must avoid cases where a=0 or b=0, or be punished with MathErrors ...
	if (a==0 or b==0):
		res = 0
	else:
		res = -a*log(a,2) -b*log(b,2)

	return res


def tokenSplit(dataset, token):
	# dataset : set of strings
	# token   : string
	#
	# output  : 2 lists of strings

	# given a dataset of titles and a token, this functions splits the
	# titles into two subsets :
	#	- those containing the token t (class_pos)
	#	- those not containing the token t (class_neg)

	class_pos = []
	class_neg = []

	# we are processing titles from the dataset one by one
	for title in dataset :
		
		# it is more convenient to split the title into a set than to
		# try and make substring considerations which could get complicated
		token_set = set(title.split())

		# depending on if the token is contained by the title or not,
		# the title is put in one class or another
		if (token in token_set):
			class_pos.append(title)
		else:
			class_neg.append(title)

	return class_pos, class_neg

