# UrbanPassApp
## Dependencies
- Django
- MySql

## Dev Commands
```bash
pip install django
pip install virtualenv
pip install mysqlclient
```

## Start
Write the following commands in the terminal to start the mock API server.
```bash
cd urbanpass
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
virtualenv urbanpassenv
urbanpassenv\Scripts\activate
python manage.py runserver
```