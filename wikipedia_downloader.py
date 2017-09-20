# coding=utf-8
import wikipedia, re, os

articles_path = 'articles/'

def get_random_wikipedia_article():
    title = wikipedia.random()
    try:
        content = wikipedia.page(title)
    except wikipedia.exceptions.DisambiguationError as err:
        print('⚠️  Randomly picked disambiguation page: ' + err.title + ', picking new one...')
        return get_random_wikipedia_article()
    except wikipedia.exceptions.PageError as err:
        print('⚠️  Failed to find page: ' + err.title + ', picking new one...')
        return get_random_wikipedia_article()
    except Exception:
        print('😐  Something unexpected happened, picking new one...')
        return get_random_wikipedia_article()
    return wikipedia.page(title)

def create_articles_folder():
    if not os.path.exists(articles_path):
        os.makedirs(articles_path)

def clean_filename(name):
    clean_name = re.sub('[^a-zA-Z0-9_\(\)\s]', '', name)
    clean_name = re.sub('\s+', ' ', clean_name)
    return clean_name

def save_article(name, content):
    filename = articles_path + name + '.txt'
    file = open(filename, "w")
    try:
        file.write(content)
    except:
        print('⛔  Failed to save article: ' + name)
        file.close()
        os.remove(filename)
    else:
        print('✔️  Saved article: ' + name)

if __name__ == '__main__':
    import warnings
    warnings.filterwarnings("ignore")

    create_articles_folder()
    wikipedia.set_lang('de')

    for i in range(0, 300):
        article = get_random_wikipedia_article()
        name = clean_filename(article.title)
        save_article(name, article.content)
