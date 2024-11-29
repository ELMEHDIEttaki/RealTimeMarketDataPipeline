-- Crrate market keyspace

CREATE KEYSPACES IF NOT EXISTS market WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : '1' };

USE market;

-- Create trades, runing_averages_15_sec tables

CREATE TABLE IF NOT EXISTS market.trades(
    uuid uuid,
    symbol text,
    currency_base text,
    currency_quote text,
    type text,
    trade_timestamp timestamp,
    ingest_timestamp timestamp,
    price double,
    day_volume int,
    PRIMARY KEY((symbol), trade_timestamp)
)
WITH CLUSTERING ORDER BY (trade_timestamp DESC);

CREATE INDEX IF NOT EXISTS ON trades (uuid);

CREATE TABLE IF NOT EXISTS runing_averages_15_sec(
    uuid uuid,
    symbol text,
    price_volume_multiply double,
    ingest_timestamp timestamp,
    PRIMARY KEY((uuid), ingest_timestamp)
)
WITH CLUSTERING ORDER BY (ingest_timestamp DESC);

CREATE INDEX IF NOT EXISTS ON runing_averages_15_sec (symbol);