# redis cheat sheet

start server: 
```
redis-server
```

start cli tool:

```
redis-cli
```
get info in cli: 
```
INFO
```

add/get key:name pair:
```
set/get
```

list all keys:
```keys *
redis-cli --scan --pattern '*'
redis-cli keys '*'
```
remove all keys:
```flushdb
flushall
```
monitor chages
```
monitor
```
