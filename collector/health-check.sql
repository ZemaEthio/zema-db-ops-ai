/*
  ZEMA DB Operations AI - read-only lab health sample
  Review permissions and data-handling policy before running anywhere.
  This query does not access customer tables.
*/
SET NOCOUNT ON;

SELECT
    @@SERVERNAME AS instance_name,
    CAST(SERVERPROPERTY('ProductVersion') AS nvarchar(128)) AS product_version,
    CAST(SERVERPROPERTY('Edition') AS nvarchar(128)) AS edition,
    sqlserver_start_time,
    cpu_count,
    physical_memory_kb
FROM sys.dm_os_sys_info;

SELECT
    d.name AS database_name,
    d.state_desc,
    d.recovery_model_desc,
    d.user_access_desc
FROM sys.databases AS d
WHERE d.database_id > 4
ORDER BY d.name;

SELECT TOP (10)
    wait_type,
    waiting_tasks_count,
    wait_time_ms,
    signal_wait_time_ms
FROM sys.dm_os_wait_stats
WHERE wait_type NOT LIKE 'SLEEP%'
ORDER BY wait_time_ms DESC;
