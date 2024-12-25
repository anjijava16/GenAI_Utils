http://localhost:5601/app/discover#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-15m,to:now))&_a=(columns:!(_source),filters:!(),index:'845e2e40-c27d-11ef-b442-79f69ef1e72b',interval:auto,query:(language:kuery,query:''),sort:!())


# search all
```
GET _search

{
  "query": {
    "match_all": {}
  }
}

```

# Get movies indices info 

```
GET /movies
{
  "query":{
    "match_all": {
      
    }
  }
}

```

# Get Movies Indices all data info

```
GET /movies/_search
{
  "query":{
    "match_all": {
      
    }
  }
}
```


<img width="1726" alt="image" src="https://github.com/user-attachments/assets/803850d3-dae7-4c3b-9037-d554db979600" />

