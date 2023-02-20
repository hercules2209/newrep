import requests
import sys
import argparse
API_KEY = '' #Use your own API key here you can get it after creating an account from https://newsapi.org

URL = ('https://newsapi.org/v2/top-headlines?')


def get_articles_by_category(category,country,sortBy):
    query_parameters = {
        "category": category,
        "sortBy": sortBy,
        "country": country,
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def get_articles_by_query(query,sortby):
    query_parameters = {
        "q": query,
        "sortBy": sortby,
        "apiKey": API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(URL, params=params)

    articles = response.json()['articles']

    results = []
        
    for article in articles:
        results.append({"title": article["title"], "url": article["url"]})

    for result in results:
        sys.stdout.write(result['title'])
        sys.stdout.write('\n')
        sys.stdout.write(result['url'])
        sys.stdout.write('\n\n\n')
    return

def get_sources_by_category(category):
    url = 'https://newsapi.org/v2/top-headlines/sources'
    query_parameters = {
        "category": category,
        "language": "en",
        "apiKey": API_KEY
    }

    response = requests.get(url, params=query_parameters)

    sources = response.json()['sources']

    for source in sources:
        sys.stdout.write(source['name'])
        sys.stdout.write(source['url'])


if __name__ == "__main__":


    parser = argparse.ArgumentParser(description="Get top news headlines for a given category")
    parser.add_argument("--category",default=None, help="The category of news you want to see")
    parser.add_argument("--sources", default="No", help="The query you want to search for")
    parser.add_argument("--query",default=None, help="The query you want to search for")
    parser.add_argument("--country",default=None, help="The country you want to see news from")
    parser.add_argument("--sortby",default="Top", help="The sort order of the news")
    args = parser.parse_args()

    if args.category!=None:
        print(f"Getting news for {args.category}...\n")
        get_articles_by_category(args.category,args.country,args.sortby)
        print(f"Successfully retrieved top {args.category} headlines")


        if args.sources=="Y":
            print(f"\nGetting sources for {args.category}...\n")
            get_sources_by_category(args.category,args.sortby)
            print(f"\nSuccessfully retrieved top {args.category} sources\n")


    if args.query!=None:
        print(f"Getting news for {args.query}...\n")
        get_articles_by_query(args.query,args.sortby)
        print(f"Successfully retrieved top {args.query} headlines")

        if args.sources=="Yes":
            print(f"\nGetting sources for {args.query}...\n")
            get_sources_by_category(args.query)
            print(f"\nSuccessfully retrieved top {args.query} sources")
