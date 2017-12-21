# -*- coding: utf-8 -*-

import re
import urllib2
import os


# 此函数获取京东首页上各种不同分类商品的首页网址
def get_links_within_jd_portal(jd_url):
    page_obj = urllib2.urlopen(jd_url)
    page_src = page_obj.read()

    # 先用正则表达式匹配出京东首页的所有链接
    link_list = re.findall("(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", page_src)

    # 筛选出目标网址
    with open('tmp.csv', 'a') as fout:
        for url in link_list:
            # 筛选出所有.jd.com或者.jd.com/结尾的网址
            if url.find('jd.com', len(url) - 7, len(url)) > -1:
                # 去掉网址末尾的'/'
                if url.find('/', len(url) - 1, len(url)) > -1:
                    url = ''.join(list(url)[0:len(url) - 1])
                print url
                fout.write('https:' + url + '\n')
            # 筛选出channel.jd.com/*html的网址
            elif len(re.findall('channel\.jd\.com/.+\.html', url)) > 0:
                print url
                fout.write('https:' + url + '\n')

    # 去除重复行
    url_set = set()
    with open('www_jd_com.csv', 'a')as dst_file:
        for line in open('tmp.csv', 'r'):
            if line not in url_set:
                dst_file.write(line)
                url_set.add(line)

    # 删除临时文件
    os.remove('tmp.csv')


if __name__ == '__main__':
    get_links_within_jd_portal('https://www.jd.com')
