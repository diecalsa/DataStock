!['Logo'](https://github.com/diecalsa/DataStock/blob/main/src/DataStockLogo.png)

Data stock is an automatic document classifier that has been developed to take care of your documents and to improve your work by reducing the time spent in searching for documentation.

It's an open source tool developed in Apache NiFi, Ludwig, Elasticsearch and Kibana. 

## Datastock's architecture

!['Arquitectura](https://github.com/diecalsa/DataStock/blob/main/src/arquitectura.png)

- [Apache Nifi](https://nifi.apache.org/) is used for data ingestion.
- [Ludwig](https://ludwig-ai.github.io/ludwig-docs/) is an open source tool developed by Uber which helps training Machine Learning models.
- [Elasticsearch](https://www.elastic.co/es/) is a distributed noSQL database integrated in ELK stack.
- [Kibana](https://www.elastic.co/es/) is a visualization tool which is integrated in ELK stack.


## Datastocks Dashboard

A dashboard has beed developed in order to visualize the data. It enables the user to:

- Visualize all the documents classified by it's content.
- Visualize the location where de documents have been generated.
- Visualize the most common tags.
- Visualize the time series when the documents have been loaded to the database.

!['Visualizacion'](https://github.com/diecalsa/DataStock/blob/main/src/visualizacion.gif)