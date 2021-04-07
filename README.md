# Testing token based Authentication system with Django Rest Api

# URLS:

### /hello (for testing authorization output).
### /token/ (for requesting token).


# How to use:
1. Create migrations using ```python3 manage.py makemigrations```
2. Run migrations ```python3 manage.py migrate```
3. Create a user ```python3 manage.py createsuperuser```
4. Run server ```python3 manage.py runserver```
5. Request token by sending post request to /token/ with params (username="----" password="----")
6. test token by sending get request to /hello with param (Authorization = "token ---------")

