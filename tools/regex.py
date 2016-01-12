import re

pattern = re.compile("^http://vsetv\.net/([^.]+)\.html$")
if pattern.match('http://vsetv.net/stbua.html'):
    print ('Yes!')
else:
    print('No')
