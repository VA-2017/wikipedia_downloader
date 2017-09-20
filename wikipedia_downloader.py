# coding=utf-8
import os
import re
import wikipedia

articles_path = 'articles/'


def get_random_wikipedia_article():
    title = wikipedia.random()
    try:
        return wikipedia.page(title)
    except wikipedia.exceptions.DisambiguationError as err:
        print('⚠️  Randomly picked disambiguation page: ' + err.title + ', picking new one...')
        return get_random_wikipedia_article()
    except wikipedia.exceptions.PageError as err:
        print('⚠️  Failed to find page: ' + err.title + ', picking new one...')
        return get_random_wikipedia_article()
    except Exception:
        print('😐  Something unexpected happened, picking new one...')
        return get_random_wikipedia_article()


def create_articles_folder():
    if not os.path.exists(articles_path):
        os.makedirs(articles_path)


def clean_filename(filename):
    clean_name = re.sub('[^a-zA-Z0-9_()\s]', '', filename)
    clean_name = re.sub('\s+', ' ', clean_name)
    return clean_name


def save_article(article_name, content):
    filename = articles_path + article_name + '.txt'
    file = open(filename, "w")
    try:
        file.write(content)
    except:
        print('⛔  Failed to save article: ' + article_name)
        file.close()
        os.remove(filename)
    else:
        print('✔️  Saved article: ' + article_name)


if __name__ == '__main__':
    import warnings
    warnings.filterwarnings("ignore")

    create_articles_folder()
    wikipedia.set_lang('de')

    for i in range(0, 300):
        article = get_random_wikipedia_article()
        name = clean_filename(article.title)
        save_article(name, article.content)
