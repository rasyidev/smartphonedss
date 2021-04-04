-- BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id"),
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "main_customuser" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"email"	varchar(254) NOT NULL UNIQUE,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"has_smartphone_preference"	bool NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "main_customuser_groups" (
	"id"	integer NOT NULL,
	"customuser_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id"),
	FOREIGN KEY("customuser_id") REFERENCES "main_customuser"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "main_customuser_user_permissions" (
	"id"	integer NOT NULL,
	"customuser_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id"),
	FOREIGN KEY("customuser_id") REFERENCES "main_customuser"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id"),
	FOREIGN KEY("user_id") REFERENCES "main_customuser"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "main_userpreference" (
	"id"	integer NOT NULL,
	"performance"	real NOT NULL,
	"price"	real NOT NULL,
	"camera"	real NOT NULL,
	"memory"	real NOT NULL,
	"battery"	real NOT NULL,
	"reputation"	real NOT NULL,
	"user_id"	integer NOT NULL,
	"is_choosen"	bool NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "main_customuser"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "main_smartphone" (
	"id"	integer NOT NULL,
	"name"	text NOT NULL,
	"ram"	varchar(255) NOT NULL,
	"cpu"	varchar(255) NOT NULL,
	"camera"	varchar(255) NOT NULL,
	"memory"	varchar(255) NOT NULL,
	"battery"	varchar(255) NOT NULL,
	"url"	varchar(255) NOT NULL,
	"img_url"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "django_migrations" VALUES (44,'contenttypes','0001_initial','2021-03-08 22:56:32.211013');
INSERT INTO "django_migrations" VALUES (45,'contenttypes','0002_remove_content_type_name','2021-03-08 22:56:32.665419');
INSERT INTO "django_migrations" VALUES (46,'auth','0001_initial','2021-03-08 22:56:32.922161');
INSERT INTO "django_migrations" VALUES (47,'auth','0002_alter_permission_name_max_length','2021-03-08 22:56:33.058171');
INSERT INTO "django_migrations" VALUES (48,'auth','0003_alter_user_email_max_length','2021-03-08 22:56:33.164816');
INSERT INTO "django_migrations" VALUES (49,'auth','0004_alter_user_username_opts','2021-03-08 22:56:33.283414');
INSERT INTO "django_migrations" VALUES (50,'auth','0005_alter_user_last_login_null','2021-03-08 22:56:33.534032');
INSERT INTO "django_migrations" VALUES (51,'auth','0006_require_contenttypes_0002','2021-03-08 22:56:33.657461');
INSERT INTO "django_migrations" VALUES (52,'auth','0007_alter_validators_add_error_messages','2021-03-08 22:56:33.787497');
INSERT INTO "django_migrations" VALUES (53,'auth','0008_alter_user_username_max_length','2021-03-08 22:56:33.972979');
INSERT INTO "django_migrations" VALUES (54,'auth','0009_alter_user_last_name_max_length','2021-03-08 22:56:34.082915');
INSERT INTO "django_migrations" VALUES (55,'auth','0010_alter_group_name_max_length','2021-03-08 22:56:34.193089');
INSERT INTO "django_migrations" VALUES (56,'auth','0011_update_proxy_permissions','2021-03-08 22:56:34.344946');
INSERT INTO "django_migrations" VALUES (57,'auth','0012_alter_user_first_name_max_length','2021-03-08 22:56:34.624335');
INSERT INTO "django_migrations" VALUES (58,'main','0001_initial','2021-03-08 22:56:34.758967');
INSERT INTO "django_migrations" VALUES (59,'admin','0001_initial','2021-03-08 22:56:35.059969');
INSERT INTO "django_migrations" VALUES (60,'admin','0002_logentry_remove_auto_add','2021-03-08 22:56:35.189004');
INSERT INTO "django_migrations" VALUES (61,'admin','0003_logentry_add_action_flag_choices','2021-03-08 22:56:35.363547');
INSERT INTO "django_migrations" VALUES (62,'sessions','0001_initial','2021-03-08 22:56:35.545776');
INSERT INTO "django_migrations" VALUES (63,'main','0002_userpreference','2021-03-10 01:16:15.803562');
INSERT INTO "django_migrations" VALUES (64,'main','0003_userpreference_is_choosen','2021-03-10 03:08:24.644567');
INSERT INTO "django_migrations" VALUES (65,'main','0004_smartphone','2021-03-26 06:12:24.925555');
INSERT INTO "django_migrations" VALUES (66,'main','0005_auto_20210326_2035','2021-03-26 14:00:36.277797');
INSERT INTO "django_migrations" VALUES (67,'main','0006_delete_smartphone','2021-03-26 14:06:59.615224');
INSERT INTO "django_migrations" VALUES (68,'main','0007_smartphone','2021-03-26 14:06:59.895280');
INSERT INTO "django_content_type" VALUES (1,'main','customuser');
INSERT INTO "django_content_type" VALUES (2,'admin','logentry');
INSERT INTO "django_content_type" VALUES (3,'auth','permission');
INSERT INTO "django_content_type" VALUES (4,'auth','group');
INSERT INTO "django_content_type" VALUES (5,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (6,'sessions','session');
INSERT INTO "django_content_type" VALUES (7,'main','userpreference');
INSERT INTO "django_content_type" VALUES (8,'main','smartphone');
INSERT INTO "auth_group_permissions" VALUES (1,1,17);
INSERT INTO "auth_group_permissions" VALUES (2,1,18);
INSERT INTO "auth_group_permissions" VALUES (3,1,19);
INSERT INTO "auth_group_permissions" VALUES (4,1,20);
INSERT INTO "auth_permission" VALUES (1,1,'add_customuser','Can add custom user');
INSERT INTO "auth_permission" VALUES (2,1,'change_customuser','Can change custom user');
INSERT INTO "auth_permission" VALUES (3,1,'delete_customuser','Can delete custom user');
INSERT INTO "auth_permission" VALUES (4,1,'view_customuser','Can view custom user');
INSERT INTO "auth_permission" VALUES (5,2,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (6,2,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (7,2,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (8,2,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (9,3,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (10,3,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (11,3,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (12,3,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (13,4,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (14,4,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (15,4,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (16,4,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (17,5,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (18,5,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (19,5,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (20,5,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (21,6,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (22,6,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (23,6,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (24,6,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES (25,7,'add_userpreference','Can add user preference');
INSERT INTO "auth_permission" VALUES (26,7,'change_userpreference','Can change user preference');
INSERT INTO "auth_permission" VALUES (27,7,'delete_userpreference','Can delete user preference');
INSERT INTO "auth_permission" VALUES (28,7,'view_userpreference','Can view user preference');
INSERT INTO "auth_permission" VALUES (29,8,'add_smartphone','Can add smartphone');
INSERT INTO "auth_permission" VALUES (30,8,'change_smartphone','Can change smartphone');
INSERT INTO "auth_permission" VALUES (31,8,'delete_smartphone','Can delete smartphone');
INSERT INTO "auth_permission" VALUES (32,8,'view_smartphone','Can view smartphone');
INSERT INTO "auth_group" VALUES (1,'Mahasiswa');
INSERT INTO "main_customuser" VALUES (1,'pbkdf2_sha256$216000$mgtiYOXu1xIQ$YGwNCFHUpJm74J6cOjJOsNrQ838M1/X7pvPXu9yoDfE=','2021-03-19 03:02:29.471398',1,'admin@rasyidev.id',1,1,'2021-03-08 22:57:08.972238',0);
INSERT INTO "main_customuser" VALUES (2,'pbkdf2_sha256$216000$SasnyagSOfMt$ZMGT7kldw3/bNhA8sfCDFvgcGDCRmGIUZWcrCPfoiYs=','2021-03-22 00:59:15.756055',0,'mhs1@student.itera.ac.id',0,1,'2021-03-08 22:59:40.009356',0);
INSERT INTO "main_customuser" VALUES (3,'pbkdf2_sha256$216000$dVZ5MuNxfy48$7Kq4FtIQIPza9/ApQUz3NQAM5Fq60/fG8AHKIlN9cSo=','2021-03-20 06:57:13.054101',0,'mhs2@student.itera.ac.id',0,1,'2021-03-09 02:12:44.664487',0);
INSERT INTO "main_customuser" VALUES (4,'pbkdf2_sha256$216000$tTShlxXOc6Wr$2AKcgHu4x15E+EyQSZQ0bwA2gvozugJVtGUDkDEwKaM=',NULL,0,'habib.rasyid11@gmail.com',0,1,'2021-03-09 05:00:32.226874',0);
INSERT INTO "main_customuser" VALUES (5,'pbkdf2_sha256$216000$OR6x8fg6ekAM$11v/yV/yU3NJnr2z6IkNBjGKCvSOwz1Jkk1wScOLGVg=',NULL,0,'penulis1@contoh.com',0,1,'2021-03-09 05:01:05.252337',0);
INSERT INTO "main_customuser_groups" VALUES (1,2,1);
INSERT INTO "django_admin_log" VALUES (1,'2021-03-08 22:58:27.434162','1','Mahasiswa','[{"added": {}}]',4,1,1);
INSERT INTO "django_admin_log" VALUES (2,'2021-03-08 22:59:40.189367','2','mhs1@student.itera.ac.id','[{"added": {}}]',1,1,1);
INSERT INTO "django_admin_log" VALUES (3,'2021-03-08 22:59:47.149104','2','mhs1@student.itera.ac.id','[]',1,1,2);
INSERT INTO "django_session" VALUES ('g41943fyzkfgu2n51ct62lee0e2yhkcd','.eJxVjDsOwjAQBe_iGlm7DlZiSnrOYK29zySAHCmfKuLuECkFtG9m3mairEsf1xlTHNRcDJvT75YkP1F3oA-p99HmsS7TkOyu2IPO9jYqXtfD_TvoZe6_dZOg1BJYvQfEhwBuUhs6ypRc48FJiah0RTIDoVBwkKIly9mBxbw_-u85Cg:1lM3rG:F-cw9tyCinIER4mErd3F0G142l9Pddv5TuWS5oWUCAk','2021-03-30 07:11:14.350766');
INSERT INTO "main_userpreference" VALUES (16,16.67,16.67,16.67,16.67,16.67,16.67,2,1);
INSERT INTO "main_userpreference" VALUES (17,16.67,16.67,16.67,16.67,16.67,16.67,3,1);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "main_customuser_groups_customuser_id_group_id_8a5023dd_uniq" ON "main_customuser_groups" (
	"customuser_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "main_customuser_groups_customuser_id_13869e25" ON "main_customuser_groups" (
	"customuser_id"
);
CREATE INDEX IF NOT EXISTS "main_customuser_groups_group_id_8149f607" ON "main_customuser_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "main_customuser_user_permissions_customuser_id_permission_id_06a652d8_uniq" ON "main_customuser_user_permissions" (
	"customuser_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "main_customuser_user_permissions_customuser_id_34d37f86" ON "main_customuser_user_permissions" (
	"customuser_id"
);
CREATE INDEX IF NOT EXISTS "main_customuser_user_permissions_permission_id_38e6f657" ON "main_customuser_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "main_userpreference_user_id_0a1dfd88" ON "main_userpreference" (
	"user_id"
);
COMMIT;
