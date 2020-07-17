from pynytimes import NYTAPI
nyt = NYTAPI("YOUR_API_KEY")
articles = nyt.article_search("https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=indigo&api-key=YOUR_API_KEY")
#print(articles)
news = []
for i in articles:
    dic = {}
    dic['url'] = i['web_url']
    news.append(dic)
#print(news)
urls=[]
for new in news:
    for key,url in new.items():
        urls.append(url)
for url in urls:
    print(url)
    

# article :indigo
"""
https://www.nytimes.com/1889/07/14/archives/no-robbery.html
https://www.nytimes.com/1858/10/29/archives/central-america-crops-and-contracts-in-costa-ricathe-proposed.html
https://www.nytimes.com/1898/08/20/archives/reviews-of-books-dialect-tales-justly-praised.html
https://www.nytimes.com/1890/10/19/archives/anne-bissell.html
https://www.nytimes.com/1859/10/27/archives/european-news-the-jason-at-st-johns-further-by-the-persia-the-great.html
https://www.nytimes.com/1859/06/27/archives/from-the-pacific-coast-nicaragua-rejects-the-american-ultimatum.html
"""