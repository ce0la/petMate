# petMate's BE (Django Rest Framework API endpoints)


## Getting Started

Fork then clone the `petdev` branch into your local machine using `git clone -b petdev https://github.com/ce0la/petMate.git`

### Prerequisites / Installing

It is strongly advised for contributors/users to setup a virtual environment to run this app. The following commands will setup a deployment environment on the local machine:

```
cd petMate # That is, cd into the project's root directory

virtualenv your-chosen-env-name # This creates your virtual environment

source your-chosen-env-name/bin/activate # This activates the virtual environment; use "deactivate" (without quotes) to exit the environment

pip install -r requirements.txt # This installs all project requirements

python manage.py runserver 0.0.0.0:8080 # This starts up the development server at your localhost's port 8000

```

Press `Ctrl+C` to exit out of the server.

Go to `localhost:8000` or `127.0.0.1:8000` to confirm that the server is up and running on the referenced host and port



## API endpoints and respective URLs

### User APIs

/accounts/api/v1/users/ - To list users

/accounts/api/v1/create_user/ - To create a user


### Pet APIs

/api/v1/pets/ - To list pets

/api/v1/create_pet/ - To create pet

/api/v1/edit_pet/<int:pk>/ - To edit pet details

/api/v1/upload_pet_image/ - To upload a pet image to cloudinary

**Ensure you are signed in to access the create, edit and delete APIs.**
Sign up at `/accounts/signup/`
Sign in at `/accounts/login/`



## Built With

* [Django](http://docs.djangoproject.com) - The web framework used

## To deploy on a remote server

Run:

```
docker build -t your-chosen-docker-container-name .   # Do not ommit the period

docker run -p 8000:8000 your-chosen-docker-container-name
```
