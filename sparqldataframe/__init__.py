__version__ = '0.1.1'

import pandas as pd
from simplejson import JSONDecodeError
import requests


def dbpedia_query(sparql_query):
    url = 'http://dbpedia.org/sparql'
    return query(url, sparql_query)


def wikidata_query(sparql_query):
    url = 'https://query.wikidata.org/sparql'
    return query(url, sparql_query)


def query(url, sparql_query):
    try:
        r = requests.get(
            url,
            params={
                'format': 'json',
                'query': sparql_query
            },
            headers={
                "accept": "application/sparql-results+json"
            })
        data = r.json()
    except JSONDecodeError as e:
        print(r.content)
        raise Exception('Invalid query')

    if ('results' in data) and ('bindings' in data['results']):
        columns = data['head']['vars']
        rows = [[binding[col]['value'] if col in binding else None
                for col in columns]
                for binding in data['results']['bindings']]
    else:
        raise Exception('No results')

    return pd.DataFrame(rows, columns=columns)
