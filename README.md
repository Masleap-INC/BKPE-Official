
# BKPE-Official

A Multi Vendor E-com shop build with Django REST Framework(DRF).

####  Dependencies
- Python 3.6+
- pip

#####  Getting Started

###  Installation
# Clone this repository:
```python
git clone git@github.com:Masleap-INC/BKPE-Official.git
```

# Create virtualenv and install all requirements in backend directory:
```commandline
cd BKPE-Official
py -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

# Set up database connection in bkpe/settings.py in DATABASES section:

For SQLite3:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

For MongoDB Atlas:
```python
DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'DB Name',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': 'host url'
            }
        }
}

```
# Make Migrations on DB:
```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Creating an admin user:
```python
python manage.py createsuperuser
```

# Fire up backend server:
```python
python manage.py runserver
```

