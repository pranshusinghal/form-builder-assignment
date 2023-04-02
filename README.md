## Built With
* Django - https://www.djangoproject.com/
* SQLite - https://www.sqlite.org/index.html


## GIT Configuration on Local
    - git clone https://github.com/<username>/form-builder-assignment.git
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
    
    - Handle static files in project
        - update PROJECT_DIR and STATIC_ROOT in settings.py file
        - python manage.py collectstatic 
    NOTE: It's a good practice to add the STATIC_ROOT directory to your .gitignore file to avoid committing the static files to your repository.

    - Create Superuser
        - python manage.py createsuperuser
    
    - Clear your Browser Cache (cmd + shift + R), if static changes not getting reflected

## Setup via. Docker    
    - If you want to rebuild the container after making changes to your Dockerfile or docker-compose.yml file, you can run the following command:
        - docker-compose up --build
    
    - Run Application inside Docker container
        - sudo docker-compose up -d

    - Optional command(this command would ignore cache and build from scratch again)
        - sudo docker-compose build --no-cache

    - Clear your Browser Cache (cmd + shift + R), if static changes not getting reflected

## Website Screenshots
![Login Page](https://github.com/pranshusinghal/form-builder-assignment/blob/main/formbuilder/login_page.png)
![Landing Page](https://github.com/pranshusinghal/form-builder-assignment/blob/main/formbuilder/landing_page.png)
![Form Fill Page](https://github.com/pranshusinghal/form-builder-assignment/blob/main/formbuilder/form_filling_page.png)

## Useful Links for Project
    - Signup - http://127.0.0.1:8000/signup/
    - Login - http://127.0.0.1:8000/account/login/?next=/
    - Landing Page - http://127.0.0.1:8000/

## Contact
Pranshu Singhal - singhalpranshu12@gmail.com
