--  Create csle db if not exists --
SELECT 'CREATE DATABASE csle' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'csle')\gexec

-- Create csle user --
DROP USER IF EXISTS csle;
CREATE USER csle WITH ENCRYPTED PASSWORD 'csle';
REASSIGN OWNED BY csle TO postgres;
DROP OWNED BY csle;

-- Grant priviliges to csle user for the csle db --
GRANT ALL PRIVILEGES ON DATABASE csle TO csle;

-- Create CITUS extension --
CREATE EXTENSION citus;