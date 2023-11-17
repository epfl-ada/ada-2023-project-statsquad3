import os
import pandas as pd

titles_path = "../validation_titles.csv"
html_dir = "../data/plaintext_articles/"

def load_titles_3(file_path=titles_path):
    """
    Load the titles of Wikispeedia pages

    Input args:
        file_path: path to the text file which contains the list of wikipedia articles
    Output:
        titles: List, list of Wikipedia pages used in Wikispeedia
    """
    titles = pd.read_csv(file_path, header=None)
    titles.columns = ['title']
    return titles

def load_html_3(titles, dir=html_dir):
    """
    Load the text of Wikispeedia pages

    Input args:
        titles: pandas Dataframe of wikipedia titles for which to retrieve html content
        dir: path to the directory containing the wikipedia articles' html content
    Output:
        content: Dict, dictionary of (title: html content) pairs
    """
    content = []
    for title in titles.title:
        path = os.path.join(dir,title+".txt")
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                html_content = file.readlines()
                content.append("".join(html_content[1:]))
        else:
            print("WARNING: file", path, "is missing")
    titles['content'] = content
    return titles