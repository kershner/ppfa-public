# Required software
- python3
- pip
- virtualenv
- sqlite3

# Installation
    $ virtualenv -p python3 venv
    $ source virtualenv/bin/activate
    $ pip install -e .
    $ pip install -r

# Run migrations and start app
    $ manage.py migrate
    $ manage.py runserver

    In a seperate terminal from the server:
    $ manage.py test

    You should see an error in the server terminal after running tests.

# Project requirements

## Part 1: Appointments REST endpoints
- create a new git branch called appoinments
- complete the serializers for appointments (in pp.appointments.serializers)
- write some tests for the endpoints (pp.appointments.tests). You should fill out the existing ones, and add 2-3 tests for edge cases.
- add the ability to filter appointments by date for the list view. the filtering should be done in the querystring. i.e. (urlencoded of course) GET /api/v1/appointments/?start_date=07-11-2020&end_date=09-20-2020

## Part 2

Create a new branch from appointments (not master) called doctors

Create a new app called 'doctors'
    $ manage.py startapp doctors

The doctor model should contain the following data:
- Name
- Specialization (you can limit it to 5 options. e.g. podiatrist, cardiologist, etc...)
- Rating

Also, you need to create a many-to-many relationship between the doctors model and the appointments model.

Next, modify the appointments serializer and tests. You should now be able to add a doctor when you create an appointment. You should add logic to check that a doctor does not have an existing appointment in the slot you are creating.

For the purpose of this exercise, you can assume all appointments start on the hour, and only run for one hour.