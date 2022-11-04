import json
from difflib import get_close_matches
data = json.load(open("dictionary.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn = input("Did you mean %s instead?Enter Y for yes and N for no" %get_close_matches(w,data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w,data.keys())]
        elif yn == "n":
            return "The word is not present.Please double check it"
    else:
        return "The word does not exist. Please double check it"
word = input("Enter the input: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
input("Press Enter to exit")
