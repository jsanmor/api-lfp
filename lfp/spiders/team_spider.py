from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from lfp.items import Team
from lfp.items import Player
from scrapy import log

class TeamsSpider(Spider):
	
	name = "team"
	allowed_domains = ["lfp.es"]
	start_urls = ["http://www.lfp.es/liga-bbva"]

	def parse(self, response):
		sel = Selector(response)
		links = sel.select('//div[@id="liga_bbva_box1"]/div/div/a/@href')
		for link in links:
			href = link.extract()
			yield Request(href, self.parse_data)

	def parse_data(self, response):
		sel = Selector(response)
		team = sel.select('//h1/text()').extract()
		log.msg("Scrape players from ", level=log.INFO)
		players_a = sel.select('//*[@class="box_posiciones"]')
		for player_a in players_a:
			player = Player()
			player['name']= player_a.xpath('div/div[@class="nombre_perfil"]/text()').extract()
			player['team']= team
			player['url'] = player_a.xpath('@href').extract()
			yield player