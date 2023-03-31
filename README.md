## Built With
* Django - https://www.djangoproject.com/
* SQLite - https://www.sqlite.org/index.html


## GIT Configuration on Local
    - git clone 
    - git config remote.origin.url "https://github.com/<username>/form-builder-assignment.git"
    - git config user.name <your_username>
    - git config user.email <your_email>

## Normal Setup 
    - Create VirtualEnv
        - python3 -m venv venv
        - source venv/bin/activate
        - pip install django djangorestframework django-cors-headers

    - Handle DB Migrations
        - python manage.py migrate
        - python manage.py runserver <optional_port_number>

    - Create Superuser
        - python manage.py createsuperuser

## Setup via. Docker
    - Run Application inside Docker container
        - sudo docker-compose build --no-cache
        - sudo docker-compose up -d
    
    - If you want to rebuild the container after making changes to your Dockerfile or docker-compose.yml file, you can run the following command:
        - docker-compose up --build

## Useful Links for Project
    - Signup - http://127.0.0.1:8000/signup/
    - Login - http://127.0.0.1:8000/account/login/?next=/
    - Landing Page - http://127.0.0.1:8000/

## Contact
Pranshu Singhal - singhalpranshu12@gmail.com
