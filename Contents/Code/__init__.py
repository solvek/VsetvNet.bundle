TITLE = 'VsetvNet'
WEB_PAGE = 'http://vsetv.net'
ART    = 'art-default.jpg'
ICON   = 'icon-default.png'


####################################################################################################
def Start():

	Plugin.AddViewGroup("List", viewMode="List", mediaType="items")
	ObjectContainer.title1 = TITLE
	ObjectContainer.art = R(ART)
	DirectoryObject.art = R(ART)
	DirectoryObject.thumb = R(ICON)

####################################################################################################
@handler('/video/vsetvnet', TITLE)
def MainMenu():

	oc = ObjectContainer()

	for video in HTML.ElementFromURL(WEB_PAGE).xpath('//html/body/div[@id="con"]/div[@class="con_tv"]/div[@class="left"]/div[@class="section"]/div[@class="box visible"]/div[@id="scrol"]/a'):

		subpath = video.xpath('./@href')[0]
		url = WEB_PAGE + subpath
		thumb = WEB_PAGE + '/templates/tv/images'+subpath[:-4]+'png'

		path = './div/span/'
		titlePath = '/div[contains(@class, "kanal_title")]'

		title = video.xpath(path+titlePath)[0].text

		Log.Debug("Clip url: %s, title: %s, thumb url: %s" % (url, title, thumb))

		oc.add(VideoClipObject(
			url = url,
			title = title,
			thumb = Callback(Thumb, url=thumb)
		))

	return oc

def Thumb(url):

  try:
    data = HTTP.Request(url, cacheTime = CACHE_1MONTH).content
    return DataObject(data, 'image/jpeg')
  except:
    return Redirect(R(ICON))
