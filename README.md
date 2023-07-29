# sparqldataframe

[![image](https://img.shields.io/pypi/v/sparqldataframe.svg)](https://pypi.python.org/pypi/sparqldataframe)

A Python library that can send
[SPARQL](https://en.wikipedia.org/wiki/SPARQL) queries to a SPARQL
endpoint and retrieve a [Pandas](http://pandas.pydata.org/) dataframe
from the result.

# Installation

``` bash
pip install sparqldataframe
```

# Usage

Here is an example how to run a SPARQL query on the
[Wikidata](http://wikidata.org/) endpoint:

``` python
import sparqldataframe

sparql_query = """
PREFIX wd: <http://www.wikidata.org/entity/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX bd: <http://www.bigdata.com/rdf#>

SELECT ?item ?itemLabel 
WHERE {
  ?item wdt:P31 wd:Q146.
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en".
  }
}
"""
df = sparqldataframe.query(
  "https://query.wikidata.org/sparql",
  sparql_query)
```

Wikidata and [DBPedia](http://dbpedia.org/) can be both used without
adding the SPARQL endpoint url by using the `wikidata_query()` and
`dbpedia_query()` functions respectively:

``` python
df = sparqldataframe.wikidata_query(sparql_query)
df = sparqldataframe.dbpedia_query(sparql_query)
```

# License

This project is licensed under the MIT license. See the
[LICENSE](LICENSE) for details.
