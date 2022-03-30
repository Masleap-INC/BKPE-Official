
#######  BKPE-Official
A Multi Vendor E-com shop build with Django REST Framework(DRF).


####  Dependencies
- Python 3.6+
- PIP

#####  Getting Started

###  Installation
# Clone this repository:

git clone git@github.com:Masleap-INC/BKPE-Official.git

# Create virtualenv and install all requirements in backend directory:

cd BKPE-Official
py -m venv env
env\Scripts\activate
pip install -r requirements.txt

# Set up database connection in bkpe/settings.py in DATABASES section:

For SQLite3:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

For MongoDB Atlas:

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



