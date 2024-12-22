1. Batch analytics is most commonly used for business intelligence, whereas real-time analytics is most commonly used for customer-facing data.

2. Functionally, real-time data analytics is increasingly being utilized to automate decision-making or processes within applications and services, as oppos




### **Real time analytics databases**

1. **Ingestion Throughput**:

   Real-time analytics databases must scale write operations to support millions of events per second, whether from IoT sensors, user clickstreams, or any other streaming data system
2. Read Patterns

   Columnar databases excel here. Since columnar databases use a column-oriented storage pattern - meaning data in columns is stored sequentially on disk - they're generally able to reduce scan size on analytical queries. Analytical queries rarely need to use all of a table’s columns to answer a question, and since columnar databases store data in columns sequentially, they can read only the data needed to get the resul
3. Query Performance

   High-performance real-time analytics databases should return answers to complex queries in milliseconds.
   However, not all columnar storage is the same, and the specific DBMS might introduce delay to query responses. Snowflake, for example, uses columnar storage. But Snowflake seeks to distribute queries across compute, scaling horizontally to be able to handle a query of arbitrary complexity. This "result shuffling" tends to increase latency, as you'll have to bring all the distributed result sets back together to serve the query response. ClickHouse, on the other hand, seeks to stay as "vertical" as possible and attempts to minimize query distribution, which typically results in lower latency responses.

4. Concurrency

Real-time analytics is often (though not always) synonymous with "user-facing analytics." User-facing analytics differs from analytics for internal reporting in that queries to the database are driven not by internal reporting schedules, but by on-demand user requests. This means you won't have control over 1) how many users query your database, and 2) how often they query it.
Database queries in user-facing analytics are initiated by application users, which significantly limits your control over query concurrency.
A real-time analytics database needs to be able to support thousands of concurrent requests even on complex queries. Scaling to support this concurrency can be difficult regardless of your database.

5. Scalability

Every database, whether real-time or not, must be able to scale. Real-time analytics databases need to scale as each of the above factors remains. A real-time analytics database allows you to scale horizontally, vertically, or both to maintain high data freshness, low latency on queries, high query complexity, and high query concurrency.



### ****Major real time analytics databases****

1. ClickHouse
2. Apache Druid
3. Apache Pinot

All these databases are open-source, column-oriented, distributed, OLAP databases uniquely suited for real-time analytics. Your choice will depend on your use case, comfort level, and specific feature requirements. From a pure performance perspective, most won't notice a major difference between these three for most use cases (despite what various synthetic, vendor-centric benchmarks might suggest).


That said, each of these databases is relatively complex to deploy. They're niche databases, with much smaller communities than traditional OLTP databases and many more quirks that take time to understand.