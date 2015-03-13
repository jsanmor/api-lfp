from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from lfp.items import Teams

class TeamsSpider(BaseSpider):
	
	name = "teams"
	allowed_domains = ["lfp.es"]
	start_urls = ["http://www.lfp.es/liga-bbva"]

	def parse(self, response):
		sel = Selector(response)
		#Todos los elementos tr de la pagina excepto el
		results = sel.select('//tr[position()>1]')
		for result in results:
			team = Teams()
			#En cada tr, el elemento cuya clase coincida con ...
			team['name'] = result.xpath('.//*[@class="nombre_equipo_clasificacion"]/text()').extract()
			#En cada tr, el primer hijo de tipo td
			team['pos'] = result.xpath('td[1]/text()').extract()
			team['score'] = result.xpath('td[4]/text()').extract()
			yield team