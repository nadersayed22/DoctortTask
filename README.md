# Doctor Task 
-- Doctor On Line API , project consists of 2 app , accout , doctorapp

# usage
-- To be able to make this app up and running follow along with me.
1. Go and clone wall app's repo.

2. Create & Run a virtual environment for this app.

--Open your terminal, go to the wall app's cloned repo's directory, and run this command
# Make sure you installed virtualenv
pip install --upgrade virtualenv

# Create a virtual environment for the wall app
virtualenv doctorproject

# Activate the wallvenv virtual environment
source doctorproject/bin/activate

3. Install all of the needed packages.

--From your terminal running your wallvenv, run the following command

cd src/
pip install -r requirements.txt


4. If you'll use my test db, you don't need this step.
--Run the migrations

python manage.py makemigrations
python manage.py migrate

5. Now, your configs are completed just run the application.

python manage.py runserver



