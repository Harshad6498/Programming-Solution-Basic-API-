from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key = "YOUR KEY")
val = int(input("Enter your choice.. 1: Query Search  2: Sources  "))
count = 1
if val == 1:
    query = input("Enter the query: ")
    top_headlines = newsapi.get_top_headlines(q = query, language = 'en')
    for article in top_headlines['articles']:
        print('Title:', article['title'])
        count+=1
        if count >10:
                    break
elif val ==2:
    source_name = input("Enter the source: ")
    news_sources = newsapi.get_sources()
    
    for source in news_sources['sources']:
        if source['name'] == source_name:
            top_headlines = newsapi.get_top_headlines(language = 'en')
            for article in top_headlines['articles']:
                print('Title:', article['title'])
                count+=1
                if count >10:
                    break
else:
    print("Wrong Choice")