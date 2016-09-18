#!/usr/bin/python

# Lists shelves for a user 
# URL: https://www.goodreads.com/shelf/list.xml    (sample url) 
# HTTP method: GET 
# Parameters: 
# key: Developer key (required).
# user_id: Goodreads user id (required)
# page: 1-N (default 1)

import keys
from goodreads import client

gc = client.GoodreadsClient(keys.key, keys.secret)

res = gc.session.get('shelf/list.xml', params={'page':'1', 'user_id':'some id here'})
for item in res['shelves']['user_shelf'][0]:
    print item['name']
