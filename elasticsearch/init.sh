curl -X PUT "http://localhost:9200/myindex" -H "Content-Type: application/json" -d '{
  "mappings": {
    "properties": {
      "id": {"type": "keyword"},
      "text": {"type": "text"}
    }
  }
}'