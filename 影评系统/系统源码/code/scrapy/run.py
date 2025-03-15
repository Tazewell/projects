# -*- codeing = utf-8 -*-
# @File: run.py



from scrapy.cmdline import execute

# execute(['scrapy', 'crawl', 'movie_subject'])
# execute(['scrapy', 'crawl', 'movie_meta'])
execute(['scrapy', 'crawl', 'movie_comment'])

