# blog-QA-Django
## Django project Blog and Q&amp;A vol.2
- python manage.py runserver 

Language: Python
Framework: Django
Database: SQLite3

#### _1 - API's_

`Blog`
- Blog api to post questions and store it to database.

`Question&Answer`
- Post questions and manage it the way you want.

`User`
-  User management. Register and Login.

#### _2. Following the order above, URLS:_

`Blog` (/blog)
- `blog/` 📰 will show the list of post made by people;
- `blog/<slug>/` will show the post detailed;

`Question&Answer` (/qna)
- `questions/` will return all questions made and their authors;
- `questions/<slug>/` Will return the question detailed to check or answer it;
- `create-question/` will render a page to create a question and post it in questions

`User` (--)
- `register/` will render and register user.
- `login/` this will authenticate user session
