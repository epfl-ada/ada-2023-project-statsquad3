import os

titles_path = "../data/wikispeedia_paths-and-graph/articles.tsv"
html_dir = "../data/plaintext_articles/"

def load_titles(file_path=titles_path):
    """
    Load the titles of Wikispeedia pages

    Input args:
        file_path: path to the text file which contains the list of wikipedia articles
    Output:
        titles: List, list of Wikipedia pages used in Wikispeedia
    """
    titles = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            # Skip comments and empty lines
            if line.startswith('#') or not line.strip():
                continue
            
            # URL decode the article name
            # title = urllib.parse.unquote(line.strip())
            title = line.strip()
            titles.append(title)
    
    return titles

def load_html(titles, dir=html_dir):
    """
    Load the text of Wikispeedia pages

    Input args:
        titles: list of wikipedia titles for which to retrieve html content
        dir: path to the directory containing the wikipedia articles' html content
    Output:
        content: Dict, dictionary of (title: html content) pairs
    """
    content = {}
    for title in titles:
        path = os.path.join(dir,title+".txt")
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as file:
                html_content = file.readlines()
                content[title] = "".join(html_content[1:])
        else:
            print("WARNING: file", path, "is missing")
    return content
