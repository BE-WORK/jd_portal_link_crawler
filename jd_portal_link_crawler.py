# -*- coding: utf-8 -*-

import re
import urllib2


# 此函数获取京东首页上各种不同分类商品的首页网址
def get_links_within_jd_portal(jd_url):
    page_obj = urllib2.urlopen(jd_url)
    page_src = page_obj.read()

    # 先用正则表达式匹配出京东首页的所有链接
    link_list = re.findall("(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", page_src)

    # 筛选出所有.jd.com或者.jd.com/结尾的网址
    with open('www_jd_com.csv', 'a') as fout:
        for url in link_list:
            if url.find('jd.com', len(url) - 7, len(url)) > -1:
                # print url
                fout.write('https:' + url + '\n')


if __name__ == '__main__':
    get_links_within_jd_portal('https://www.jd.com')
