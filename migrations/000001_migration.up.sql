create table if not exists "users" (
  "id" bigserial PRIMARY KEY,
  "telegram_id" bigint not null unique,
  "telegram_chat_id" bigint not null unique,
  "created_at" timestamp default now(),
  "is_deleted" boolean default false
);

create unique index if not exists  "idx_telegram_unique" on "users" ("telegram_id", "telegram_chat_id");