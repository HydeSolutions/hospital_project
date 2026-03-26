@echo off

curl -X POST http://localhost:8083/connectors ^
  -H "Content-Type: application/json" ^
  --data @connector.json

pause