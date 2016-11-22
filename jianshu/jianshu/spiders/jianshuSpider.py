from parsel import Selector
from scrapy.contrib.spiders import CrawlSpider

from jianshu.items import JianshuItem


class Jianshu(CrawlSpider):
    name='jianshu'   # 运行时这个爬虫的名字
    start_urls=['http://www.jianshu.com']
    url = 'http://www.jianshu.com'

    def parse(self, response):
        selector = Selector(response)
        #....
        # response就是返回的网页数据
        # 处理好的数据放在items中，在items.py设置好你要处理哪些数据字段，这里我们抓取文章标题，url，作者，阅读数，喜欢，打赏数
        ## 解析处理数据的地方，用xpath解析处理数据
        articles = selector.xpath('//ul[@class="article-list thumbnails"]/li')

        for article in articles:
            title = article.xpath('div/h4/a/text()').extract()
            url = article.xpath('div/h4/a/@href').extract()
            author = article.xpath('div/p/a/text()').extract()
            JianshuItem.item['title'] = title
            JianshuItem.item['url'] = 'http://www.jianshu.com/' + url[0]
            JianshuItem.item['author'] = author
            yield JianshuItem