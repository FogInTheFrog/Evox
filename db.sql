DROP TABLE IF EXISTS messages;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS next_msg_id;

CREATE TABLE messages (
    "MessageID" integer NOT NULL,
    "Body" character varying(160) NOT NULL,
    "Views" integer DEFAULT 0
);

ALTER TABLE messages
    ADD CONSTRAINT pk_messages PRIMARY KEY ("MessageID");

ALTER TABLE messages
    ADD CONSTRAINT check_max_length CHECK (length("Body") <= 160);

ALTER TABLE messages
    ADD CONSTRAINT check_min_length CHECK (length("Body") > 0);

CREATE SEQUENCE next_msg_id INCREMENT BY 1 NO MINVALUE NO MAXVALUE START WITH 1;

CREATE TABLE users (
    "Username" character varying(20) NOT NULL,
    "Fullname" character varying(30),
    "Hashed_password" character varying(256) NOT NULL
);

ALTER TABLE users
    ADD CONSTRAINT pk_users PRIMARY KEY ("Username");

BEGIN;
INSERT INTO users VALUES ('admin', 'Ad Min', '$2b$12$XOtmREW71ehXGhiukqAaT.iMH/yejJ6z4OVrq/wyCjd.vqQR.oqsu');
INSERT INTO users VALUES ('daft', 'Daft Code', '$2b$12$s6H.45LxwuEY4neA7/q4MOwDbfIo77wpD1d6OpTOEyvIDoNITd02q');
INSERT INTO messages VALUES (0, 'Hello World!');
COMMIT;