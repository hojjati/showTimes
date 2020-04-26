##How to Install
To install the project, make sure you have all the requirements in file
`requirements.txt` installed. Then navigate to the project's root folder
 and run the following commands:

- `python manage.py makemigrations`
- `python manage.py migrate` 
- `python manage.py runserver`

Then visit `http://localhost:8000/`. You should be able to run the app.

For testing run `python manage.py test`. 

##Documentation
This project uses Python/Django framework which is one of the best frameworks for creating
a data-driven web app. Another advantage of using Django is the simplicity and scalibility it provides.
To follow best practices, `Django REST framework` is chosen for API development.
To provide the best user experience possible, `Bootstrap` and `Materialize` frameworks are used for UX/UI design.
And finally to create a Single Page Application, `AngularJS` is used as the front-end framework which
makes the architecture simple and avoids the initial set-up overhead.

##Notes on scalability
In the current version of the app filtering is done in the front-end.
However, if we were dealing with a large database of movies, we would
have to move filtering to the API. Another consideration would be to 
add pagination in the back-end to avoid loading the entire database into
the front-end at once.   