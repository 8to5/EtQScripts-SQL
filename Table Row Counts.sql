-- SQL Server
SELECT SCHEMA_NAME(schema_id) AS SchemaName,
T.name AS TableName,
SUM(P.rows) AS TotalRowCount
FROM sys.Tables AS T
JOIN sys.partitions AS P ON T.object_id = P.object_id AND P.index_id IN ( 0, 1 )
GROUP BY SCHEMA_NAME(schema_id), T.name
HAVING SUM(P.rows)>0
ORDER BY 1, 2, 3
