# Valluvarbot
Ask valluvar queries, he will reply back with relevant thirukkurals.

This code is hosted in deta.space and also the semantic search is hosted in huggingface.co space.

The code (main.py), hosted in deta.space acts as an interface to the telegram bot, t.me/@askvalluvar_bot, 
The queries from telegram bot, are delegated to huggingface, space ['thamizh' ](https://huggingface.co/spaces/thiyagab/Thamizh)

The file 'semanticsearch.py' uses the huggingface hosted Sentencetransformer model, 'all-MiniLM-L6-v2', to train the thirukkural texts,
the trained model is then used to find the similarities with the given input query and return the top 3 matches.

The project is still progress, and still a lot more to do, including formatting this README file.
