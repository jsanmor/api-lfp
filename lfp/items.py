# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Teams(scrapy.Item):
	name = scrapy.Field()
	pos = scrapy.Field()
	score = scrapy.Field()

class Team(scrapy.Item):
	name = scrapy.Field()
	url = scrapy.Field()

class Player(scrapy.Item):
	name = scrapy.Field()
	team = scrapy.Field()
	pos = scrapy.Field()
	url = scrapy.Field()