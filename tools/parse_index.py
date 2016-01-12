import os
from lxml import etree
from io import StringIO
import codecs

WEB_PAGE = 'http://vsetv.net'

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

filename = __location__ + "/html/index.html"

file = codecs.open(filename, 'r', 'utf-8')

content = file.read()
file.close()

parser =etree.HTMLParser()

tree = etree.parse(StringIO(content), parser)

r = tree.xpath('//html/body/div[@id="con"]/div[@class="con_tv"]/div[@class="left"]/div[@class="section"]/div[@class="box visible"]/div[@id="scrol"]/a')

for video in r:
    # result = etree.tostring(video, pretty_print=True, method="html")
    subpath = video.xpath('./@href')[0]
    url = WEB_PAGE + subpath
    thumb = WEB_PAGE + '/templates/tv/images'+subpath[:-4]+'png'

    path = './div/span/'
    titlePath = '/div[contains(@class, "kanal_title")]'

    title = video.xpath(path+titlePath)[0].text

    print ({k: v for k,v in locals().items() if k in ['url', 'thumb', 'title','summary']})
