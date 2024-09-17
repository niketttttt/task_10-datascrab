from utils.startfile import extractData


if __name__ =='__main__':
    
    qurl = 'https://books.toscrape.com/'
    
    qheader = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    
    }
    
    htmldata = extractData(url=qurl, header=qheader)
    
    #print(htmldata)
   
    title = htmldata.select('div.h1 > small')[0].text
    
    #print('title',title)
    
    titlestag = htmldata.select('article.product_pod > h3 > a')
    
    #print(titles)
    
    titles = [elem.attrs['title'] for elem in titlestag]
    
    #print(titles)
    
    category = htmldata.select('div.side_categories > ul > li > ul > li')
    
    
    #for category in bookcategory:
    #    print(category.get_text())
        
    B1 = htmldata.select('div.side_categories > ul > li > ul > li:nth-of-type(3)')
    
    #print(bookcategory)
    
    
    B2 = htmldata.select('div.side_categories > ul > li > ul > li:nth-of-type(3n+0)')
    
    print(B2)
    
    
    
    
    
    
    
    
     
    
    
    
    
    
    
    
    
    
       

    
