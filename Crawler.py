# 找出照片板块

soup = BeautifulSoup(driver.page_source, 'lxml')
cons_li_list = soup.select('.cons_li')


#每一位MM的信息
# 昵称
name = cons_li.select('.item_name')[0].get_text()
# 照片链接
# 由于js图片延迟加载，img标签指向链接的属性有可能不是src，而是data-ks-lazyload
img = cons_li.select('.item_img img')[0]
img_src = img.get('src')
if img_src is None:
    img_src = img.get('data-ks-lazyload')
    
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-18 17:00:19
# @Author  : kk (zwk.patrick@foxmail.com)
# @Link    : blog.csdn.net/PatrickZheng
# @Version : $Id$

from selenium import webdriver
from bs4 import BeautifulSoup

# 如果在环境变量PATH中添加了phantomJS，此处不需要指明executable_path
driver = webdriver.PhantomJS(executable_path='D:\workplace\spider\phantomjs-2.1.1-windows\phantomjs.exe')
driver.get('https://www.taobao.com/markets/mm/mmku')

soup = BeautifulSoup(driver.page_source, 'lxml')

# 每个MM的展示是放在 属性class=cons_li的div中
cons_li_list = soup.select('.cons_li')
print len(cons_li_list)

try:
    f = open('mm_detail.txt', 'a')
    for cons_li in cons_li_list:
        name = cons_li.select('.item_name')[0].get_text()
        print name
        f.write((name+'\n').encode('utf-8'))
        img = cons_li.select('.item_img img')[0]
        img_src = img.get('src')
        if img_src is None:
            img_src = img.get('data-ks-lazyload')
        print img_src
        f.write(img_src.encode('utf-8'))
finally:
    if f:
        f.close()

driver.close()
print 'done.'
