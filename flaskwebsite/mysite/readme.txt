Install flask module  :
pip install Flask

Install virtual env  module so you only use module needed
pip install virtualenv

to view only module Install
pip freeze

//create a virtual environment name virtual
python -m venv virtual

//to install a module in the the virtual environment
./virtual/Scripts/pip install flask
./virtual/scripts/python
 ./virtual/Scripts/pip freeze

Download 'heroku toolbelt' so you can push to heroku and manage your server
heroku auth:login or login

create an app on heroku name app
heroku create app

view list of app on heroku
heroku app

// heroku server need to run python
pip install gunicorn

//view status of heroku server
heroku info
