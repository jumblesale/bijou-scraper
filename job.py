#!/usr/bin/env python3
import scraper.generate_data as generate_data
import pprint


categories = generate_data.scrape_data()
json = generate_data.categories_to_json(categories)
print(pprint.pformat(json))
