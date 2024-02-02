

CREATE TABLE IF NOT EXISTS artik_article (
    id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title varchar(200) NOT NULL,
    content text NOT NULL,
    created_at datetime NOT NULL,
    updated_at datetime NOT NULL,
    author_id integer NOT NULL,
    FOREIGN KEY (author_id) REFERENCES auth_user (id)
);