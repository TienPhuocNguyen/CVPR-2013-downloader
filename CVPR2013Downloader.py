#!/usr/bin/python
import urllib,urllib2
from bs4 import *

#pre-created folder
paperpath = 'E:\\[2013][CVPR]\\'

print 'Start to download all CVPR 2013 papers...'
url = 'http://www.cv-foundation.org/openaccess/CVPR2013.py#'
req = urllib2.Request(url,headers={'User-Agent' : "Magic Browser"})
page = urllib2.urlopen(req)

#parse
soup = BeautifulSoup(page.read())

#content div
content_div = soup.find('div', {'id':'content'}) 

for item in content_div.findAll('dt',{'class':'ptitle'}):
    pdflink = item.findAll('br')[0].a
    url_paper = pdflink.get('href')
    url_paper = 'http://www.cv-foundation.org/openaccess/' + url_paper
    print url_paper
    
    name = pdflink.contents
    forbidden = '\\/:*?"<>|'
    for c  in name:
        for c in forbidden:
            name[0] = name[0].replace(c,'')   
    name = paperpath + name[0] + '.pdf'
 
    pdfpage = urllib2.urlopen(url_paper)
    f = open(name, 'wb')
    f.write(pdfpage.read())
    f.close()

print 'End.'
