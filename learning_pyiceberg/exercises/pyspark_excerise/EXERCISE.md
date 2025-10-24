## Exercise 1 — Environment Familiarization

1. Set up a local Nessie catalog and object store (e.g., MinIO or local FS).
2. Connect PySpark to Nessie as the Iceberg catalog.
3. List existing catalogs and branches in Nessie.
4. Create a new branch called dev from main.
5. Confirm that any new tables you create appear in dev branch.

Goal: Understand how Nessie tracks Iceberg table metadata.

## Exercise 2 — Create the Base Table

1. Use PySpark to create a small DataFrame of customer data (id, name, country, signup_date, spend).
2. Write it as an Iceberg table into the Nessie catalog.
3. Inspect the metadata in Nessie (commits, manifests, snapshots).
4. Query the table back from PySpark to verify it’s accessible.

Goal: Learn how DataFrames become Iceberg tables tracked in Nessie.

## Exercise 3 — Transformations and Updates

1. Create another DataFrame with updated spend values for some customers.
2. Merge or overwrite data into the Iceberg table (simulate incremental updates).
3. Perform a few transformations:
4. Calculate average spend per country
5. Add a new derived column (e.g., spend_category)
6. Save the transformed dataset back into a new Iceberg table (customer_summary)
7. Validate that changes appear as new commits in Nessie.

Goal: Practice ETL and incremental data management using Iceberg tables.

## Exercise 4 — Schema Evolution

1. Add a new column (e.g., email).
2. Rename an existing column (spend → total_spend).
3. Drop an unnecessary column (e.g., signup_date).
4. Query the table before and after each change.
5. Inspect the schema history and snapshots in Nessie.

Goal: Understand Iceberg’s schema evolution without breaking existing data.

## Exercise 5 — Time Travel and Branching

1. Identify previous snapshots of your table using Nessie history.
2. Query data as of an earlier snapshot to see old values.
3. Create a new Nessie branch (experiment), make some test updates there.
4. Switch back to main and confirm that changes aren’t visible.
5. Merge experiment back into main and validate results.
Goal: Experience version control and reproducibility in Iceberg + Nessie.

## Exercise 6 — Maintenance & Optimization

1. Observe how many data and metadata files exist after multiple updates.
2. Perform data compaction (rewrite/optimize files).
3. Expire older snapshots.
4. Inspect how file count and table size change after maintenance.

Goal: Learn how to manage small file issues and metadata bloat in Iceberg.

## Exercise 7 — Analytics Use Case

1. Join your customer_summary table with a new “transactions” table.
2. Perform aggregations (e.g., total spend per month per country).
3. Save results as a new Iceberg table (monthly_sales).
4. Visualize the result using PySpark or a BI tool connected to Iceberg.

Goal: Combine transformation + analytics workflow in a lakehouse pattern.

##  Advanced Tasks

1. Create and test partition evolution (e.g., switch from country to region partitioning).
2. Simulate CDC (change-data-capture) by applying inserts, updates, and deletes.
3. Compare Copy-on-Write vs Merge-on-Read table performance.
4. Automate periodic compaction and snapshot expiry.