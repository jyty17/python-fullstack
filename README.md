# Python Full Stack

## Objective
- Create task queuing service for custom engine
- Users can create their own custom engine for system to run
- System return analysis of engine execution

## Usage

Install Requirements
``` pip install requirements.txt```

To run application go to Frontend directory and run
```python manage.py runserver```

Then start celery scheduler
```celery -A frontend beat -l info```

Then start celery worker to get tasks
```celery -A frontend worker -l info```

## Insipiration

<!-- [Science Flask](https://github.com/danielhomola/science_flask "Science Flaks Web App Template") -->