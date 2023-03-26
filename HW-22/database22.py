# CREATE TABLE IF NOT EXISTS users(
#                id integer primary key autoincrement,
#                first_name TEXT,
#                last_name TEXT,
#                age INTEGER NOT NULL);
# CREATE TABLE IF NOT EXISTS publishing_house(
#                           id integer primary key autoincrement,
#                           name TEXT,
#                           rating default 5);
# CREATE TABLE IF NOT EXISTS books(
#                id integer primary key autoincrement,
#                title TEXT,
#                author TEXT,
#                year INTEGER NOT NULL,
#                price INTEGER NOT NULL,
#                publishing_house_id INTEGER NOT NULL,
#                FOREIGN KEY (publishing_house_id) references publishing_house(id));
# CREATE TABLE IF NOT EXISTS purchases(
#                    id integer primary key autoincrement,
#                    user_id INTEGER NOT NULL,
#                    books_id INTEGER NOT NULL,
#                    date TEXT,
#                    FOREIGN KEY (books_id) references books(id),
#                    FOREIGN KEY (user_id) references users(id));