__version__ = '0.1.3'

import requests
import pandas as pd
from typing import Optional, Dict, Any
from simplejson import JSONDecodeError

DEFAULT_PREFIXES = """
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbr: <http://dbpedia.org/resource/>
PREFIX dbp: <http://dbpedia.org/property/>

PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX p: <http://www.wikidata.org/prop/>
PREFIX ps: <http://www.wikidata.org/prop/statement/>
PREFIX pq: <http://www.wikidata.org/prop/qualifier/>
PREFIX bd: <http://www.bigdata.com/rdf#>
"""


def dbpedia_query(sparql_query: str):
    url = 'http://dbpedia.org/sparql'
    return query(url, DEFAULT_PREFIXES + sparql_query)


def wikidata_query(sparql_query: str):
    url = 'https://query.wikidata.org/sparql'
    return query(url, DEFAULT_PREFIXES + sparql_query)


def query(url: str, sparql_query: str, headers: Optional[Dict[str, str]] = None):
    default_headers = {
        "accept": "application/sparql-results+json"
    }
    if headers:
        default_headers.update(headers)

    try:
        r = requests.get(
            url,
            params={
                'format': 'json',
                'query': sparql_query
            },
            headers=default_headers)
        r.raise_for_status()
        data = r.json()
    except JSONDecodeError:
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
