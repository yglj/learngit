import gevent
import urllib.request
from gevent import monkey


def downloader(url, index):
    req = urllib.request.urlopen(url)
    img_content = req.read()
    with open('../test/img' + str(index) + '.jpg', 'wb') as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "http://img.hb.aicdn.com/d40efd78ea447140402c39808fd32b64b1c89a43d086b-Zp9sdj_fw236", 1),
        gevent.spawn(downloader, 'http://huaban.com/pins/1919781609/', 2),
        gevent.spawn(downloader, 'http://huaban.com/pins/1922523242/', 3)
    ])


if __name__ == '__main__':
    main()

