alter table "users" drop column if exists "shikimori";

drop table if exists "genres";
drop table if exists "anime_list";
drop table if exists "evaluations";

drop index if exists "idx_unique_evaluations";
