#Write some lines to encode (sentences 0 and 2 are both ideltical):
sen = [
    "Three years later, the coffin was still full of Jello.",
    "The fish dreamed of escaping the fishbowl and into the toilet where he saw his friend go.",
    "The person box was packed with jelly many dozens of months later.",
    "He found a leprechaun in his walnut shell."
]

import json
import numpy
import os

# Opening JSON file
f = open('thirukural_git.json')

# returns JSON object as
# a dictionary
data = json.load(f)

en_translations=[]
kurals=[]
# Iterating through the json
# list
for kural in data['kurals']:
    en_translations.append((kural['meaning']['en'].lower()))
    kurals.append(kural['kural'])



# Closing file
f.close()
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
sen_embeddings = model.encode(en_translations)

def find_similarities(input:str):
    input_embeddings = model.encode([input.lower()])
    from sklearn.metrics.pairwise import cosine_similarity
    #let's calculate cosine similarity for sentence 0:
    similarity_matrix=cosine_similarity(
        [input_embeddings[0]],
        sen_embeddings[1:]
    )
    #Get only the top 3 matches
    indices=[numpy.argpartition(similarity_matrix[0],-3)[-3:]]
    response=''
    for index in indices[0]:
        print(similarity_matrix[0][index])
        response+=en_translations[index+1]
        print(en_translations[index+1])
        response += "\n".join(kurals[index+1])
        print("\n".join(kurals[index+1]))
    return response

while True:
    text=input('Ask valluvar: ')
    if( text == 'exit'):
        break
    find_similarities(text)