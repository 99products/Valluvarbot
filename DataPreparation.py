import json

# Opening JSON file
f = open('thirukural_git.json')

# returns JSON object as
# a dictionary
data = json.load(f)

en_translations=[]
# Iterating through the json
# list
for kural in data['kurals']:
    en_translations.append((kural['meaning']['en']))



# Closing file
f.close()