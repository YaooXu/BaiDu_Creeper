import bs4
import time
from bs4 import BeautifulSoup
import urllib
from functools import reduce
import lxml
import requests
import url2io
import re

api = url2io.API('HMTEF2G9SzySmZ7DAWN0Rw')


def getWebInfos(word):
    st = time.time()

    titles = []  # 文章标题
    abstracts = []  # 摘要
    links = []  # 链接
    contents = []  # 主要内容

    for pn in [0, 10]:
        # 搜两页确保数量够
        if len(links) >= 5:
            break

        url = 'http://www.baidu.com.cn/s?wd=' + urllib.parse.quote(word) + '&pn={:d}'.format(
            pn)  # word为关键词，pn是百度用来分页的..
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, compress',
            'Accept-Language': 'en-us;q=0.5,en;q=0.3',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
        }  # 定义头文件，伪装成浏览器
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page.read().decode('utf8'), 'html.parser')

        allNews = soup.find_all('div', {'class': re.compile('result c-container*')})
        BaiKe = soup.find_all('div', {"tpl": "bk_polysemy"})  # 加入百度百科的标签

        for news in [BaiKe, allNews]:
            for new in news:
                h3 = new.find(name="h3",
                                  attrs={
                                      "class": re.compile("t")
                                  }).find('a')
                div = new.find(
                    name="div",
                    attrs={"class": re.compile("c-abstract")})

                if div is None:
                    # 百度百科词条和其他的布局不太一样
                    div = new.find(name="div",
                                       attrs={"class": "c-span18 c-span-last"})

                a = new.find(
                    name="a",
                    attrs={"class": re.compile("c-showurl")})
                try:
                    detail_url = a.get('href')
                except:
                    detail_url = h3.get('href')

                print(detail_url)

                ret = None
                try:
                    ret = api.article(url=detail_url,
                                      fields=['text', 'next'])
                except:
                    try:
                        time.sleep(1)
                        ret = api.article(url=detail_url,
                                          fields=['text'])
                    except Exception as e:
                        print(e)
                        print(detail_url)
                        contents.append('')
                        pass
                if ret is None:
                    continue

                content = ret['text'].replace(
                    '\r', '').replace('\n', '')

                print(len(content), len(links))

                if len(content) >= 200:
                    contents.append(content)
                    titles.append(h3.text.replace("\"", ""))
                    abstracts.append(div.text.replace("\"", ""))
                    links.append(detail_url)
                    if len(links) >= 5:
                        break

    ed = time.time()
    print("Time cost: {:f}".format(ed - st))
    return titles, abstracts, links, contents


if __name__ == '__main__':
    titles, abstracts, links, contents = getWebInfos('北京理工大学校长是谁？')
    for i in links:
        print(i)
