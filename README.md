# Django Book Reviews 


Technologies used in this Project:

- Django
- Django ORM
- Django Debug Toolbar
- Bootstrap
- Faker

## Run
___

Run with builtin Django Server 

```bash
$ pip install -r requirements.txt
$ python manage.py runserver
```
**Media files are not provided**

## Data

All Data downloaded and cleaned from [Kaggle](https://www.kaggle.com/zygmunt/goodbooks-10k?select=books.csv)

## Populate

App includes a [jupyter notebook](Populate.ipynb) and a [script](populate.py) for populating database with authors and books from Kaggle Dataset as well as fake data about users, reviews and comments.