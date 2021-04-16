# Doctor Task 
-- Doctor On Line API , project consists of 2 app , accout , doctorapp

# usage
-- To be able to make this app up and running follow along with me.

1. Go and clone DoctorTask app's repo.

2. Create & Run a virtual environment for this app.

--Open your terminal, go to the wall app's cloned repo's directory, and run this command
      pip install --upgrade virtualenv

      virtualenv doctorproject

      source doctorproject/bin/activate

3. Install all of the needed packages.

--From your terminal running your wallvenv, run the following command

      pip install -r requirements.txt


4. If you'll use my test db, you don't need this step.
--Run the migrations

        python manage.py makemigrations
        python manage.py migrate

5. Now, your configs are completed just run the application.

       python manage.py runserver

# urls to route 
to list users 
http://127.0.0.1:8000/

to get single user 
http://127.0.0.1:8000/id

to login
http://127.0.0.1:8000/login/

to sinup
http://127.0.0.1:8000/signup/

to list doctor reservations
http://127.0.0.1:8000/reservations/

to get singl one reservion
http://127.0.0.1:8000/reservations/id

to get admin 
http://127.0.0.1:8000/admin

to list doctor
http://127.0.0.1:8000/reservations/doctors/

to get detail doctor
http://127.0.0.1:8000/reservations/doctors/id

to list patents
http://127.0.0.1:8000/reservations/patients/

to git detail patient
http://127.0.0.1:8000/reservations/patients/id







