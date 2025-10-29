import urllib
import urllib.request

try:
    req = urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('deu erro')
else:
    print('Tudo ok')