TITLE = 'VsetvNet'
WEB_PAGE = 'http://vsetv.net'
ART    = 'art-default.jpg'
ICON   = 'icon-default.png'

PREFIX = '/video/vsetvnet'

SUBSTITUTIONS = {'stbua' : '7'}

####################################################################################################
def Start():

	Plugin.AddViewGroup("List", viewMode="InfoList", mediaType="items")
	ObjectContainer.title1 = TITLE
	ObjectContainer.art = R(ART)
	DirectoryObject.art = R(ART)
	DirectoryObject.thumb = R(ICON)

####################################################################################################
@handler(PREFIX, TITLE)
def MainMenu():

	oc = ObjectContainer()

	for group in HTML.ElementFromURL(WEB_PAGE).xpath('//select[@name="sel"]/option'):

		# title = group.text
		title = group.xpath('./a')[0].text
		group = int(group.get('value'))-1

		# Log.Debug("Title: %s, group: %s. Current group: %s" % (title, group, XML.StringFromElement(group)))

		oc.add(DirectoryObject(
		            key = Callback(Channels, group = group, title=title),
		            title = title
		        ))

	return oc

@route(PREFIX+'/channels/{group}/{title}')
def Channels(group, title):

	oc = ObjectContainer(title2 = title)

	query = "%s/tv/%s.php?_=%s" % (WEB_PAGE, group, Util.RandomInt(1000, 9999))

	for video in HTML.ElementFromURL(query).xpath('a'):

		subpath = video.get('href')
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
