# django-cms
django-cms installation and working files for MAB cms.

## installation

inside your project directory, run the following command that will build the docker image if one doesn't exist yet and then start a docker container with the name 'mab-cms'.  This command will also start a bash process in the newly created and started containter where you will run the other commands
```bash
docker-compose run -p 8000:8000 mab-cms bash
```

enter 'mab' directory inside 'opt'
```bash
cd /opt/mab
```

install virtualenv
```bash
pip install virtualenv
```

create a virtual environment to run your python commands in
```bash
virtualenv venv
```

activate your newly created virtual environment
```bash
source venv/bin/activate
```

install the required django-cms python packages
```bash
pip install -r requirements.pip
```

enter mab_cms directory
```bash
cd mab_cms
```

run the following commands to remove unused plugins
```bash
python manage.py cms list plugins
```
```bash
python manage.py cms delete-orphaned-plugins
```

check that the installation is ok
```bash
python manage.py cms check
```

if you have modified any database models/schemas, run db migration
```bash
python manage.py makemigrantions
python manage.py migrate
```

start the server
```bash
python manage.py runserver 0.0.0.0:8000
```
