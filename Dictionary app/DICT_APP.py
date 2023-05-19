#Dictionary

import json                                                     #handling json files
from difflib import get_close_matches, SequenceMatcher          #get_close_matches returns list of words matching the word passed as parameter(with match ratio more than 0.6)

data = json.load(open("data.json", 'r'))

def dict(w):
    w = w.lower()
    if w in data.keys():
        return data[w]
    elif w.title() in data.keys():                              #for searching words like 'India'
        return data[w.title()]
    elif w.upper() in data.keys():                              #for searching words like "USA"
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys()))>0:              #get_close_matches returns a list, so if list isnt empty....
        mn = input("Did you mean to say %s ? Press Y if yes, N if no." % get_close_matches(w, data.keys())[0])
        if mn == 'Y' or mn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return "ok"
    else:
        return "Word not found"


word = input("Enter word: ")
output = dict(word)
if type(output) == list:                        #for printing word meanings of words having multiple meanings in the data
    for el in output:
        print(el)
else:
    print(output)