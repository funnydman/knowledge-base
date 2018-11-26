
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
Change settings and reload server:

```sql
ALTER SYSTEM set work_mem = 8192;
SELECT pg_reload_conf();
```
PostgreSQL records changes made through ALTER SYSTEM in an override file called
postgresql.auto.conf, not directly into postgresql.conf.

5) Working with users:

* List all the existing users
```sql
SELECT usename FROM pg_user;
```
* Create new user
```sql
CREATE USER librarian;
```
* Viewing Existing User Permissions
```sql
\du
```
* Altering Existing User Permissions
```sql
ALTER USER role_specification WITH OPTION1 OPTION2 OPTION3;
-- These options range from CREATEDB, CREATEROLE, CREATEUSER, and even SUPERUSER.
-- Most options also have a negative counterpart - e.g. NOCREATEDB
-- (CREATE USER is the same as CREATE ROLE except that it implies LOGIN.)
```
6) Backuping 

* Using pg_dump db_name > dump.sql

```sql
pg_dump -h localhost -d <db_name> -U <user_name> > sump.sql
```
* With Point-in-Time Database Restoration
Great article: https://severalnines.com/blog/become-postgresql-dba-point-time-database-restoration
