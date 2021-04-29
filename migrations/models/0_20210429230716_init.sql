-- upgrade --
CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "email" VARCHAR(50) NOT NULL UNIQUE,
    "hashed_password" VARCHAR(100) NOT NULL,
    "is_active" BOOL NOT NULL  DEFAULT False,
    "is_superuser" BOOL NOT NULL  DEFAULT False
);
COMMENT ON TABLE "user" IS 'Model user ';
CREATE TABLE IF NOT EXISTS "socialaccount" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "account_id" INT NOT NULL,
    "username" VARCHAR(50) NOT NULL,
    "email" VARCHAR(50),
    "provider" VARCHAR(50) NOT NULL,
    "user_id" INT REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "socialaccount" IS 'Model for social account ';
CREATE TABLE IF NOT EXISTS "uid" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "uid" VARCHAR(100) NOT NULL,
    "user_id" INT REFERENCES "user" ("id") ON DELETE CASCADE,
    "social_user_id" INT REFERENCES "socialaccount" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "uid" IS 'Model uid for future verification of user';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
