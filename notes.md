# Notes

## When Changing Anything in Models

1. make changes in `models.py`.
2. run `python manage.py makemigrations` to crate migrations.
3. run `python manage.py migrate` to actually effect changes to database.
4. optional: run `python manage.py check` to see if there are any problems in project without making changes in database.
5. optional: run `python manage.py sqlmigrate <app_name> <migration_file_number>`.
