# Baptiste Colin - Etsy Data science homework - Data Science Internship Application
# Finding Significant Terms

Here is my answer to the data science homework I've been given as part of my application at Etsy for a Data Science Internship.
I hope you will like what you are going to read ! I really enjoyed doing this, and I'm not saying this to be toady.

# Running instructions

I've chosen to write this in Python, so running it shouldn't be a big problem.
Make sure the following files are in the same folder :
- datacollection.py
- functions.py
- datamining.py
- functions2.py
- listings_A.txt
- listings_B.txt

`datacollection.py` tackles the first part of the homework, and `datamining.py` tackles the second part.
On Linux, just run it using the usual command lines :
	`$ python datacollection.py`
	`$ python datamining.py`
and it should work just fine.

I also included the `results.txt` my program outputed, as you asked.
Please note my scripts will generate several other text files upon running. This is normal, I will explain what they are a bit later.

# Presentation of the scripts

The architecture I have chosen is the same for both parts. There's the main script, which contains all of the 'high-level' instructions. It imports a script containing low-level functions, that I have chosen to define separately either because they are going to be called many times, or for readability purpose, or for both.

I make a point of explaining what my algorithms do in an oral way in the comments, you should find more than enough of them and I hope they'll be as clear as possible !
I explicitely pointed out what parts seem flawed or incomplete in my scripts, using TODO statements. Make sure your IDE highlights them.

##### Data Collection

Step by step description :
- Files containing listing IDs are opened and their data are stored in lists.
- Making API requests, the titles corresponding to the listings IDs are retrieved
- A cleaning function is applied to all the titles in order to make them processable.
- The cleaned up titles are stored in the appropriate files.

It was a pain to wait for all the listings to be downloaded. That is why I chose to store the raw titles in a `save_X.txt` file, so that I could test modifications of the formatting part of the script without having to download all the data again.
As is, my scripts might miss some listings - it happens when an IOError occurs. However I kept track of which listing has been missed, using the `error_log.txt` file.

This part is the slowest and could be improved making better API requests, more on that in the comments.

##### Data Mining

Step by step description :
- Loads previously generated files and generates a list representing the whole dataset.
- Builds a list of all existing tokens
- Computes the information gain associated with each token
- Sorts tokens with respect to the information gain they are associated with.
- Extract the top 100 tokens and outputs it.

Resorting to sets made things much more simpler (when trying to find wether a token is in a title or not, for instance).
I believe they are some bad memory management going on in this part, however the output is quickly generated so it's ok as far as homeworks go.

# That's it

Thanks for reading ! If my work confirmed your interest in my application, please feel free to contact me at my email adress : baptiste.colin@outlook.com
As I said I enjoyed doing this homework, so if it's representative of what an internship at Etsy would be like, I'm 100% in !

I'm looking forward to hearing from you soon,
I wish you the best,

Baptiste Colin



