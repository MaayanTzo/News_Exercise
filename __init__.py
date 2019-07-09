from bottle import *
import feedparser
import json


@route('/')
def index():
    return static_file("star2.html", root='')

@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='')

@route('/getArticles')
def get_articles():
    feed = feedparser.parse("http://www.fifa.com/rss/index.xml")
    articles=[]
    for i in range(1,20):
        article = {"title": feed["entries"][i]["title"], "link": feed["entries"][i]["link"]}
        articles.append(article)
    return json.dumps(articles)

if __name__ == '__main__':
    run(host='localhost',port=7000, debug=True)