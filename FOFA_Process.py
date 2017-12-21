# -*- coding: utf_8 -*-

from selenium import webdriver
from time import sleep
from multiprocessing import Pool


def fofa(keyword):
    options = webdriver.ChromeOptions()
    options.add_argument('lang=zh_CN.UTF-8')
    options.add_argument(
        'user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get('https://i.nosec.org/login')
    sleep(3)
    #填充账号
    browser.find_element_by_xpath(".//*[@id='username']").send_keys('915348696@qq.com')
    sleep(3)
    #填充密码
    browser.find_element_by_xpath(".//*[@id='password']").send_keys('915348696Lll')
    sleep(3)
    browser.find_element_by_css_selector('#rememberMe').click()
    sleep(3)
    browser.find_element_by_css_selector('.mod_but').click()
    sleep(3)
    browser.get('https://fofa.so/')
    sleep(3)
    browser.get('http://www.fofa.so')
    try:
        browser.find_element_by_css_selector('#q').send_keys(keyword)
    except:
        browser.find_element_by_css_selector()
        browser.find_element_by_css_selector('#q').send_keys(keyword)
    try:
        browser.find_element_by_css_selector('.search_tj').click()
    except:
        browser.find_element_by_css_selector('#search_form').click()
    page = browser.find_element_by_xpath(".//*[@id='will_page']/a[7]").text
    page = int(page)
    try:
        for j in range(1,page):
            sleep(3)
            if j ==2:
                browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/a').click()
                sleep(3)
            try:
                URLS = browser.find_elements_by_css_selector('.list_mod_t>a')

                for url in URLS:
                    #输出到fofa.txt文件，和当前项目在同一目录
                    f = open('fofa.txt', 'a')
                    url = url.get_attribute('href')
                    sleep(1)
                    print >> f, '%s' % url
                    f.close()
            except :
                print 'there is no url'
            try:
                no_urls = browser.find_elements_by_css_selector('.ip-no-url')
                for no_url in no_urls:
                    f = open('fofa.txt', 'a')
                    no_url = no_url.text
                    sleep(1)
                    print >> f, '%s' % no_url
                    f.close()
            except:
                pass
            sleep(3)
            href = browser.find_element_by_css_selector('.next_page').get_attribute('href')
            sleep(1)
            browser.get(href)
    except:
        browser.close()

if __name__ == '__main__':
    #批量添加需要查找的关键词
    keywords = [u'title="北京PK10" && port=80 && country=US', u'title="北京PK10" && port=80 && country=HK', u'title="蚂蚁金服"', u'title="python"', u'title="公司"', u'title="java"', u'title="百度"']
    p = Pool(2)
    for keyword in keywords:
        p.apply_async(fofa, args=(keyword,))
    p.close()
    p.join()
    print 'all subprocesses done'

# if __name__ =='__main__':
#     #最好每次只添加两个关键词
#     keywords = ['c#','php']
#     threads = []
#     for keyword in keywords:
#         t = Thread(target=fofa,args=(keyword,))
#         threads.append(t)
#
#     for thr in threads:
#         thr.start()