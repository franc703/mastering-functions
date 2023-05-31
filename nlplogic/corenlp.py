from textblob import TextBlob
import wikipedia


def search_wiki(name):
    """Searches Wikipedia for a given name and returns a list of results"""
    print(f"Searching Wikipedia for {name}")
    return wikipedia.search(name)


def summary_wiki(name):
    """Returns the summary of a Wikipedia article for a given name"""
    print(f"Getting summary for {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    """Returns a TextBlob object for a given text"""
    print("Getting TextBlob object")
    return TextBlob(text)


def get_noun_phrases(name):
    """Returns a list of noun phrases for a given TextBlob object"""
    print("Getting noun phrases")
    text = summary_wiki(name)
    text_blob = get_text_blob(text)
    phrases = text_blob.noun_phrases
    return phrases
