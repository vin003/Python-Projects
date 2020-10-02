import requests , sys,bs4, webbrowser
import os 

url="http://www.xkcd.com"
os.makedirs("xkcd",exist_ok=True)
'''If the target directory already
exists, raise an OSError if exist_ok is False. Otherwise no exception is
raised.  This is recursive.'''

while not url.endswith('#'):
        
    ##TODO: download the page
    print('Downloadin the page {}'.format(url))
    res=requests.get(url)
    c=res.content
    try:
        res.raise_for_status
    except Exception as exec:
        print("Incorrect data",exec)
    soup=bs4.BeautifulSoup(c,"html.parser")
    comicElem=soup.find_all(id = "comic")

    ###the selector '#comic img' will get you the correct <img> element from the BeautifulSoup object.
    if comicElem ==[]:
        print("Could not find the image")
    else:

        comicUrl=comicElem[0].get('src')
        print("Downloading the image {}".format(comicUrl))
        res.requests.get(comicUrl)
        try : 
            res.raise_for_status()
        except Exception as e:
            print("no url found",e)
        
    ##TODO : Find  and download  the comic image
    ###TODO: Save the image to ./xkcd

    imgFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),"wb") 
    for chunk in res.iter_content(100000):
        imgFile.write(chunk)
    imgFile.close()    

    ###TODO Grt the previous button url


    prevLink=soup.select('a[rel="prev]')[0]
    url='http://xkcd.com'+prevLink.get("href")


print('Done.')