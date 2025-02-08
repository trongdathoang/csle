-- Connect to the csle db --
\connect csle

-- Setup citus coordinator node --
SELECT citus_set_coordinator_host('127.0.0.1', 5432);
