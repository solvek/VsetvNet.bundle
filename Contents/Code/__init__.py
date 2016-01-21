TITLE = 'VsetvNet'
WEB_PAGE = 'http://vsetv.net'
ART    = 'art-default.jpg'
ICON   = 'icon-default.png'

SUBSTITUTIONS = {'stbua' : '7'}

####################################################################################################
def Start():

	Plugin.AddViewGroup("List", viewMode="InfoList", mediaType="items")
	ObjectContainer.title1 = TITLE
	ObjectContainer.art = R(ART)
	DirectoryObject.art = R(ART)
	DirectoryObject.thumb = R(ICON)

####################################################################################################
@handler('/video/vsetvnet', TITLE)
def MainMenu():

	oc = ObjectContainer(view_group="List")

	for video in HTML.ElementFromURL(WEB_PAGE).xpath('//html/body/div[@id="con"]/div[@class="con_tv"]/div[@class="left"]/div[@class="section"]/div[@class="box visible"]/div[@id="scrol"]/a'):

		subpath = video.xpath('./@href')[0]
		url = WEB_PAGE + subpath
		file_name = subpath[1:-5]

		if file_name in SUBSTITUTIONS:
			file_name = SUBSTITUTIONS[file_name]

		thumb = WEB_PAGE + '/templates/tv/images/'+file_name+'.png'

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
