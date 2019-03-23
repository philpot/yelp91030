#!/usr/bin/ennv python

import json


with open('../data/categories.json', 'r') as f:
    categories = json.load(f)

top_level_categories = [c for c in categories
                        if (c['parents'] == []) and ('US' in c.get('country_whitelist', ['US']))]
