mysqlslap --password=password --user=root --concurrency=5  --iterations=5 --query=stress_test.sql --create-schema=cs_capstone --delimiter=";"