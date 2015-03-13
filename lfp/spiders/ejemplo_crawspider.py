from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector

from lfp.items import Team

class TeamSpider(CrawlSpider):
	name = "ejemplo_crawSpider"
	allowed_domains = ["lfp.es"]
	start_urls = ["http://www.lfp.es/liga-bbva"]

	rules = ( Rule (LinkExtractor(allow=("liga-bbva", ),),callback="parse_team", follow= True),)

	def parse_team(self, response):
		sel = Selector(response)
		items = []
		team = Team()
		team["current_url"] = response.url
		team["name"] = sel.xpath('//h1/text()').extract()
		items.append(team)
		return items