# Install Flask
pipenv --python python3.7 install flask
mkdir templates static

# Start Flask on the webserver
pipenv shell
source .env
flask run --host=0.0.0.0 --port=3000

# Hit the webserver from a browser
http://webserver1c.mylabserver.com:3000/

# Install Postgres on the database server and Docker if needed.
https://raw.githubusercontent.com/linuxacademy/content-python-for-sys-admins/master/helpers/db_setup.sh

# Create a new database on the database server
sudo docker exec -i postgres psql postgres -U cloud_user -c "CREATE DATABASE notes;"

# Test connection to the database
psql postgres://cloud_user@dbserver1c.mylabserver.com:80/sample -c "SELECT count(*) FROM note;"

# Add support for the .env file as a development dependency
pipenv install --dev python-dotenv

# Providing the --dev argument will put the dependency in a special [dev-packages] location in the Pipfile.
# These development packages only get installed if you specify the --dev argument with pipenv install.

# Register the database with the application from the webserver
flask db init
flask db migrate
flask db upgrade

# Install SQLAlchemy on the webserver
pipenv install psycopg2-binary Flask-SQLAlchemy Flask-Migrate
