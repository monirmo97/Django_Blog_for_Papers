# Blog for Papers
Blog for Papers is a Django app that allows users to publish and read  papers on various topics. Users can also comment on the papers and interact with the authors.

## Features
•  Papers are stored in a SQLite database using Django models and serializers
•  Papers have the following fields: title, content, topic, authors, publish time, and abstract
•  Users can perform (create, read, delete) operations on papers 
•  Users can filter papers by topic using a path parameter
•  Users can submit comments on the papers 
•  Users can create authors 
•  Users can view the JSON response of the API using Postman

## Installation
To install Blog for Papers, you need to have Python 3 and Django 4.2 installed on your system. You can use pip to install Django:

pip install django==4.2

Then, you need to clone this repository or download the zip file and extract it. Navigate to the project directory and run the following commands to set up the database and start the server:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

The server will run on http://127.0.0.1:8000/ by default. You can access the web interface by visiting http://127.0.0.1:8000/posts/

## Usage
To use the API, you can send HTTP requests to the following endpoints:

•  POST http://127.0.0.1:8000/api/posts/ to create a new paper. You need to provide the paper data in JSON format in the request body. For example:
{
"title": "A Survey on Machine Learning",
"content": "Machine learning is a branch of artificial intelligence that.",
"topic": "Machine Learning",
"authors": [1, 2],
"abstract": "This paper provides a comprehensive overview of machine learning."
}

•  DELETE http://127.0.0.1:8000/api/posts/<pk>/ to delete an existing paper. You need to provide the paper ID in the URL.


•  GET http://127.0.0.1:8000/api/posts/ to get a list of all papers. You can also use a path parameter to filter papers by topic. 

For example: http://127.0.0.1:8000/api/posts/Machine Learning/

•  GET http://127.0.0.1:8000/api/posts/details/<pk>/ to get the details of a paper. You need to provide the paper ID in the URL.

•  POST http://127.0.0.1:8000/api/comments/submit/ to submit a comment on a paper. You need to provide the comment data in JSON format in the request body. For example:

{
"post": 1,
"user_name": "Ali",
"content": "Great paper, very informative!"
}

•  DELETE http://127.0.0.1:8000/api/comments/delete/<comment_id>/ to delete a comment on a paper. 
You need to provide the comment ID in the URL.

•  POST http://127.0.0.1:8000/api/authors/create/ to create a new author. You need to provide the author data in JSON format in the request body. For example:
{
"name": "Ali",
"email": "Ali@gmail.com",
"bio": "Ali is a researcher in machine learning."
}

You can use a web browser or a tool like Postman to view the JSON response of the API.