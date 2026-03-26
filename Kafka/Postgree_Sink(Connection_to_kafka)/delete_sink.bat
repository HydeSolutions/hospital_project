@echo off

echo Deleting Kafka Connect connector: postgres-sink...

curl -X DELETE http://localhost:8083/connectors/postgres-sink

echo.
echo Done.
pause