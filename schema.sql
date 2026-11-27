CREATE TABLE IF NOT EXISTS owner_sessions (
  id TEXT PRIMARY KEY,
  token_hash TEXT NOT NULL UNIQUE,
  owner TEXT NOT NULL,
  label TEXT NOT NULL,
  created INTEGER NOT NULL,
  expires INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS owner_sessions_owner ON owner_sessions(owner);
CREATE TABLE IF NOT EXISTS owner_vault (
  owner TEXT PRIMARY KEY,
  envelope TEXT NOT NULL,
  revision INTEGER NOT NULL,
  updated INTEGER NOT NULL
);
