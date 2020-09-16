# Notes

## Django files and what they do

- `__init__.py`
  - to tell python that this is an app.
- `admin.py`
  - for admin panel stuff
- `apps.py`
  - for this apps settings. Main app has to link to this in settings.py to work.
- `models.py`
  - models for data defined as classes.
- `tests.py`
  - test cases for this app.
- `urls.py`
  - defines urls that are linked to views.
- `views.py`
  - defines logic for views/api endpoints for this app.

## When Changing Anything in Models

1. make changes in `models.py`.
2. run `python manage.py makemigrations` to crate migrations.
3. run `python manage.py migrate` to actually effect changes to database.
4. optional: run `python manage.py check` to see if there are any problems in project without making changes in database.
5. optional: run `python manage.py sqlmigrate <app_name> <migration_file_number>`.

## To run interactive python shell in Django project context

run `python manage.py shell`.

## Date time handling in python

Django is timezone aware.

To get current time run

```python
from django.utils import timezone

# returns current time in timezone aware datetime
timezone.now()
```

To get one day duration

```python
import datetime

# returns a duration of 1 day
datetime.timedelta(days=1)
```

## To get all Choices with FK of a Question and create new Choices for a Question

reference: [Playing with Django DB API](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#playing-with-the-api)

```python
from polls.models import Question, Choices

q = Question.objects.get(pk=1)

# will retrun all choices related to 'q'
q.choice_set.all()

q.choice_set.create(choice_text="Not much", votes=0)
q.choice_set.create(choice_text="The sky", votes=0)
c = q.choice_set.create(choice_text="Just hacking again", votes=0)
```

## To get count of Choices for a given Question 'q'

```python
q.choice_set.count()
```

## Generic views

Generic views expect the data being passed to them be named 'pk' instead of any other user defined name like that of a regular view.

### `DetailView`

`template_name` is used to define the template that the view is supposed to use instead of the default.

### `ListView`

`template_name` is used to define the template that the view is supposed to use instead of the default.
`context_object_name` is used to define the name that will be used in the template to reference and display the queried data instead of the default name that Django automatically provides.
