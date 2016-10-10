# datamining.py
# created on 2016-10-09 by Baptiste Colin
#
# main script.
# given two files 'class_A.txt' and 'class_B.txt' containing listing titles, 
# this script will create a list of tokens present in titles, mesure their
# discriminative power and output a sorted list of the 100 most discriminative
# tokens.

import functions2 as f

# first, let's create a list of titles for each class
class_A = open('class_A.txt', 'r').read().splitlines()
class_B = open('class_B.txt', 'r').read().splitlines()

# let's merge these two lists : this will be our actual dataset
dataset = open('class_A.txt', 'r').read().splitlines()
class_A.extend(class_B)

# we are going to work using a dictionary.
# keys will be the tokens, values will be the information gains
# ("dico" is short for dictionary in French)
dico = {}

# building the keys of the dictionary. 
tokens = f.createTokenList(dataset)

#The next step is to compute the corresponding values, i.e. information gains

# first, let's compute the entropy of our dataset
entropy_before = f.entropy(dataset, class_A, class_B)

for t in tokens :
	
	# now, for each token, we are splitting our dataset into two classes :
	#	- titles containing the token t (class_pos)
	#	- titles not containing the token t (class_neg)
	class_pos, class_neg = f.tokenSplit(dataset, t)

	# computing the entropy of each class
	entropy_pos = f.entropy(class_pos, class_A, class_B)
	entropy_neg = f.entropy(class_neg, class_A, class_B)

	# computing the entropy of our system after the split
	entropy_after = (float(len(class_pos))/float(len(dataset)))*entropy_pos + (float(len(class_neg))/float(len(dataset)))*entropy_neg

	# finally, computing the information gain
	information_gain = entropy_before - entropy_after

	# putting it in the dictionary
	dico[t] = information_gain


# now the dictionnary is fully built.
# in order to get the 100 most discriminative tokens, we are going to sort
# the keys of the dictionary (the tokens) with respect to their values (the
# information gain)

# sorting it
sortedTokens = sorted(dico, key=dico.__getitem__, reverse=True)
# only keeping the top 100
sortedTokens = sortedTokens[:100]

# now we can write it down in the result file
results = open('results.txt', 'w')
for t in sortedTokens:
	results.write(t + '\n')
	#results.write(t + ' - ' + str(dico[t]) +'\n') #uncomment this line if you want the information gains outputed

results.close()

print('Done!')

# The End !
# Thanks for reading :)

