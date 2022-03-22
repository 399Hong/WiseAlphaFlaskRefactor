CREATE TABLE widget
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text
);

CREATE TABLE widget_option
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    widget_id INTEGER,
    name text,
    value text,
    FOREIGN KEY(widget_id) REFERENCES widget(id)
    -- foreign key constraint is not enforced.
);
