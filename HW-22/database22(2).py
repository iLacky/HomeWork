#SELECT users.id, users.first_name, users.last_name, books.title FROM purchases p JOIN users on users.id = p.users_id join books on books.id = p.book_id ORDER BY users.id
