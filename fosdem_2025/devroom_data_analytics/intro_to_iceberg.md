# Iceberg

* An open table format for large scala datasets in data lakes


## featuires
* ACID 
* Hidden partitions
* Schema evolution

## Basics
* Iceberg arch

get the picture from phone

* Iceberg catalogs
* how to choose the catalog
a. Which tools and envs an i using?
    Is it possible to have iceberg on the gcp?
* what are the benefits of iceberg


## Using iceberg: Compute engines
* built in
  * Spark and flink
* External

## Using Iceberg: Queries
* create table
* insert data
* queries


## How queries works?
1. Create table
    Get photo
2. Insert data
    Get pic
3. select
 get pic


## hidden partitions
1. what is it?
2. Can i have my own partition on the table
3. how is files will be stored in s3?
4. Partitions evolution


## Time travel capabilities
1. Its based on the snapshots of the manifest file
2. get pic

## Upsert(merge)
1. Copy on write
* make new files, fully-copies file
* Slowest performance in update but read is very efficient
2. Merge on read
* delete thern insert

## small files
1. A natural part in iceberg
2. more small file--> more file I/O
3. Solution(have few files)
* Copy on write
* Partition more optimally
* Compaction
* rewrite compaction file

## compaction

