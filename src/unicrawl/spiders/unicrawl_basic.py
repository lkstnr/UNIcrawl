from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from unicrawl.items import UnicrawlItem


class UnicrawlBasicSpider(CrawlSpider):
    name = "unicrawl_basic"
    allowed_domains = ["uni-potsdam.de"]
    start_urls = ["https://www.uni-potsdam.de/de/"]

    rules = (
        # follows all urls from allowed_domains, passes them to parse_item()
        Rule(LinkExtractor(), callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        self.logger.info("Got a response from %s." % response.url)

        if response.status == 200:
            # create item that will be send to item pipeline
            item = UnicrawlItem(url=response.url, html=self.strip_html(response.text))

            yield item
        else:
            self.logger.error("ERROR {:d}: A response from {:s} was unsuccessful".format(response.status, response.url))
            return

    def strip_html(self, html):
        html = html.strip()
        html = html.replace("\n", "")
        html = html.replace("\r", "")

        return html
