"""
    小爬虫
"""
import re

from urllib import request


class Spider:
    url = 'https://www.panda.tv/cate/hwzb'
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    # 获取整体html字符串转为utf8格式
    def __fetch_content(self):
        r = request.urlopen(self.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    # 截取网页中需要的内容，并以字典的格式返回
    def __analysis(self, htmls):
        root_html = re.findall(self.root_pattern, htmls)

        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)

        return anchors

    # 对内容进行编排(例如去除空格，换行等)
    @staticmethod
    def __refine(anchors):
        filter_lambda = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0].strip()
        }
        return map(filter_lambda, anchors)

    # 排序
    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    # 排序种子(排序时传入的计算函数)
    @staticmethod
    def __sort_seed(anchor):
        r = re.findall('\d.*\d', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    # 展示
    @staticmethod
    def __show(anchors):
        for rank in range(0, len(anchors)):
            print('rank  ' + str(rank + 1) +
                  ':' + anchors[rank]['name'] +
                  '   人气:' + anchors[rank]['number'])

    # 入口
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()
