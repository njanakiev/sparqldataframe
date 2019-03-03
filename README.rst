sparqldataframe
===============

A Python library that can send `SPARQL`_ queries to an endpoint and retrieve a `Pandas`_ dataframe from the result.


Installation
------------

.. code-block:: bash
	
	pip install sparqldataframe


Usage
-----

Here is an example how to run a SPARQL query on the `Wikidata`_ endpoint:

.. code-block:: python
	
	import sparqldataframe

	sparql_query = """
		SELECT ?item ?itemLabel 
		WHERE {
		  ?item wdt:P31 wd:Q146.
		  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
		}
	"""
	df = sparqldataframe.query("https://query.wikidata.org/sparql", sparql_query)

Wikidata and `DBPedia`_ can be both used without adding the SPARQL endpoint url by using the wikidata_query and dbpedia_query functions respectively:

.. code-block:: python

	df = sparqldataframe.wikidata_query(sparql_query)
	df = sparqldataframe.dbpedia_query(sparql_query)


License 
-------

This project is licensed under the MIT license. See the `LICENSE`_ for details.


.. _SPARQL: https://en.wikipedia.org/wiki/SPARQL
.. _Wikidata: http://wikidata.org/
.. _DBPedia: http://dbpedia.org/
.. _Pandas: http://pandas.pydata.org/
.. _LICENSE: LICENSE
