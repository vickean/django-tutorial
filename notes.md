# Notes

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
