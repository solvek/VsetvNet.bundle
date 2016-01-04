TITLE = 'VsetvNet'
WEB_PAGE = 'http://vsetv.net'


####################################################################################################
def Start():
    ObjectContainer.title1 = TITLE

####################################################################################################
@handler('/video/vsetvnet', TITLE)
def MainMenu():
  oc = ObjectContainer()

  for video in XML.ElementFromURL(WEB_PAGE).xpath('//html/body/div[@id="con"]/div[@class="con_tv"]/div[@class="left"]/div[@class="section"]/div[@class="box visible"]/div[@id="scrol"]/a')
  	url = WEB_PAGE + video.xpath('./@href')[0].text
  	span = video.xpath('./div/span')
  	title = span.xpath('./noindex/div[@class="kanal_title"]')[0].text
  	summary = span.xpath('./div[@class="kanal_trans"]')[0].text

  	oc.add(VideoClipObject(
      url = url,
      title = title,
      summary = summary
    ))

  return oc