import requests
import re

BASEURL = 'http://desk.zol.com.cn/meinv/hot_'
i = 0
for each in range(1, 21):
    url = BASEURL + str(each) + ".html"
    print(url)
    index = requests.get(url).text
    pic_url = re.findall(r'a\sclass="pic"\shref="(/bizhi/[0-9_]{10,12}.html)"', index)
    print(pic_url)
    for each in pic_url:
        html = requests.get('http://desk.zol.com.cn' + each).text
        pic_urls = re.findall(r'"imgsrc":"http:\\/\\/desk.fd.zol-img.com.cn\\/t_s##SIZE##\\(.*?.jpg)"', html)
        # print(pic_urls)
        for each in pic_urls:
            each = each.replace('\\', '')
            print(each)
            pic = requests.get('http://desk.fd.zol-img.com.cn/t_s1920x1080c2' + each)
            downloadAd = 'bgp/' + str(i) + '.jpg'
            fp = open(downloadAd, 'wb')
            fp.write(pic.content)
            fp.close()
            print(i)
            i += 1
