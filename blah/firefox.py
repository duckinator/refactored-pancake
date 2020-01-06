import http.client
import tarfile
from urllib.parse import urlparse


def download(url):
    url = urlparse(url)
    conn = http.client.HTTPConnection(url.netloc)
    conn.request('GET', url.path + '?' + url.query)
    res = conn.getresponse()
    #return res.read()
    return res


def download_firefox():
    data = download('https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US')
    #with open('firefox.tar.bz2', 'wb') as f:
    #    f.write(bzip2_data)
    #tar = tarfile.open("firefox.tar.bz2", "r:bz2")  
    tar = tarfile.open(mode='r', fileobj=data)
    tar.extractall('firefox')
    tar.close()

download_firefox()
