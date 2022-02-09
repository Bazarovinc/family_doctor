-- upgrade --
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
CREATE TABLE IF NOT EXISTS "weather" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "date" TIMESTAMPTZ NOT NULL,
    "country_code" VARCHAR(5) NOT NULL,
    "city" VARCHAR(20) NOT NULL,
    "response" TEXT NOT NULL
);
COMMENT ON COLUMN "weather"."id" IS 'id';
COMMENT ON COLUMN "weather"."date" IS 'Запрашиваемая дата';
COMMENT ON COLUMN "weather"."country_code" IS 'Код страны';
COMMENT ON COLUMN "weather"."city" IS 'Город';
COMMENT ON COLUMN "weather"."response" IS 'Ответ от https://openweathermap.org';
