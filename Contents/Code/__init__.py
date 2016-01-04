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

		url = WEB_PAGE + video.xpath('./@href')[0]		

		path = './div/span/'
		titlePath = 'div[contains(@class, "kanal_title")]'

		title = video.xpath(path+titlePath)

		if len(title) < 1:
			title = video.xpath(path+'noindex/'+titlePath)

		title = title[0].text

		summary = video.xpath(path+'div[contains(@class,"kanal_trans")]')[0].text

		Log.Debug("Clip url: %s, title: %s, summary: %s" % (url, title, summary, ))

		oc.add(VideoClipObject(
			url = url,
			title = title,
			summary = summary
		))

	return oc