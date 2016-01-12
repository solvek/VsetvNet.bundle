import os
from lxml import etree
from io import StringIO
import codecs

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

filename = __location__ + "/html/pixel.html"

file = codecs.open(filename, 'r', 'utf-8')

content = file.read()
file.close()

parser =etree.HTMLParser()

page = etree.parse(StringIO(content), parser).getroot()

if True:
##############################
    tv_node = page.xpath('//html/body/div[@id="con"]/div[@class="con_tv"]/div[@class="tv"]')[0]

    title = tv_node.xpath('./h1')[0].text
    description = tv_node.xpath('./div[@id="o_kan"]//strong')[0].tail
    thumb = 'http://vsetv.net/'+tv_node.xpath('./div[@id="o_kan"]/img')[0].get('src')

##############################

##############################
    print ({k: v for k,v in locals().items() if k in ['title', 'description', 'thumb', 'url']})


import re
##############################
RE_VIDEO_URL = Regex('m=video&file=(?P<video_url>[^"]+)"')
##############################

if True:
    url = RE_VIDEO_URL.search(content).group('video_url')

    print("url: "+url)
