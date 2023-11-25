# General description
drf_library is an API service for managing a library with books. \
Main stack: Django, Djangorestframework, MySQL, Celery, Redis, Docker, unittest.

# Install and usage
1. Clone the project from https://github.com/Marat-Shainurov/drf_library to your local machine.
2. Add .env file to the root directory (next to the docker-compose file) with the variables from the .env_sample file.

3. Build and run a new docker image from the project's root directory:
   - docker-compose up --build

4. After successful startup check out the project's endpoints (swagger or redoc documentation formats are available):
   - [Swagger Documentation] http://127.0.0.1:8000/docs/
   - [ReDoc Documentation] http://127.0.0.1:8000/redoc/

5. Start working with the app's endpoints:
    - [Books List] http://127.0.0.1:8000/library/books
    - [Create Book] http://127.0.0.1:8000/library/books/create
    - [Get Book by ID] http://127.0.0.1:8000/library/books/get/{id}
    - [Update Book by ID (both PATCH and PUT methods)]http://127.0.0.1:8000/library/books/update/{id}
    - [Delete Book by ID] http://127.0.0.1:8000/library/books/delete/{id}

    
# Testing
- All the endpoints are covered with unittests in /<app>/tests.py 
- Run tests from the running docker container: \
  docker-compose exec app python manage.py test

