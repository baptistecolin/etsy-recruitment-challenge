# datacollection.py
# created on 2016-10-08 by Baptiste Colin
#
# Main script.
# given two files named 'listings_A.txt' and 'listings_B.txt' containing listing
# IDs, this script will retrieve their titles, clean them up and store them in
# two files named 'class_A.txt' and 'class_B.txt'.
# It will also generate files containing raw titles, so that the user can process
# them without having to download them again.

import functions as f

keystring = <INSERT_KEYSTRING_HERE> # Nope, I'm not giving my keystring away :-)


# building clean lists of IDs from the files
IDs_A   = open('listings_A.txt', 'r').read().splitlines()
IDs_B   = open('listings_B.txt', 'r').read().splitlines()


# storing the raw titles in two lists
print('########## DOWNLOADING TITLES ##########')
class_A = f.getTitles(IDs_A, keystring)
class_B = f.getTitles(IDs_B, keystring)

# If an IOError has occured during the previous instruction, the title is 
# not retrieved.
# TODO : use 'error_log.txt' in order to make sur ALL listing titles are downloaded

# the download took a while, right ? Let's save the raw titles we just downloaded
# so we won't need to download them again later
print('########## CREATING SAVE FILES ##########')
save_A = open('save_A.txt', 'w')
save_B = open('save_B.txt', 'w')

for title in class_A:
	save_A.write(title + '\n')

for title in class_B:
	save_B.write(title + '\n')

save_A.close()
save_B.close()


# uncomment the two following lines and comment what is above if you want to 
# load the titles you downloaded previously instead of re-downloading them
#class_A = open('save_A.txt', 'r').read().splitlines()
#class_B = open('save_B.txt', 'r').read().splitlines()

# let's clean the titles up.
print('########## CLEANING TITLES ##########')
class_A = f.cleanList(class_A)
class_B = f.cleanList(class_B)

# nice, they're clean now. We can write them down in text files.
print('########## CREATING OUTPUT FILES ##########')
file_A = open('class_A.txt', 'w')
file_B = open('class_B.txt', 'w')

for title in class_A:
	file_A.write(title + '\n')

for title in class_B:
	file_B.write(title + '\n')

file_A.close()
file_B.close()

print('Done!')

# Thought : at each step of the script, we are making the same actions for
# A, then for B. All of this could have been wrapped in a function that would
# take a list of ID as an input, and then do it all. Then we could just have
# made 2 calls of this function : one for A, one for B. This would be
# especially useful if such a process were to be applied to a lot of
# different files. Well, TODO

