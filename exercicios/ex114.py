from urllib.request import urlopen
from urllib.error import *


try:
    s = urlopen("http://pudim.com.br")
except:
    print('Esse site não está funcionando.')
else:
    print('O site está funcionando!')