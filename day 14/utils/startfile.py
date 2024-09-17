import requests as rq
from bs4 import BeautifulSoup

def extractData(url='', header=None):
    if type(url) != str and url == '':
        return 'please enter website url'
    
    if type(header) != dict and header == None:
        return 'please check header for website'
    
    
    
    htmlpage = rq.get(url=url, headers=header)

    bSoup = BeautifulSoup(htmlpage.content, 'html.parser')

    return bSoup

