
1) Location of configuration files

```sql
SELECT name, setting FROM pg_settings WHERE category = 'File Locations';
```
2) See where data is stored

```sql 
show data_directory;
```

3) Get directory number for any database

```sql
SELECT oid as object_id, datname as database_name FROM pg_database;
```

Output is similar to this one:

```sql
 object_id | database_name 
-----------+---------------
     13018 | postgres
     16384 | test
         1 | template1
     13017 | template0
```
More info http://www.postgresql.fastware.com/blog/where-and-how-is-your-data-actually-stored-on-disk

4) Show info from pg_settings:

```sql
select unit from pg_settings where name='shared_buffers';
```
