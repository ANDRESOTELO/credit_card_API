# Whale & Jaguar Backend Test
For this technical test, I have been asked to create a web application with which the user can interact and validate if a credit card number is valid or not

# Technologies and tools
For the backend:
- Python
- Flask
- Git
- Docker

## Virtual environment
To install virtualenv
```bash
sudo pip3 install virtualenv
```
To create a new virtual environment with Python 3.7
```bash
virtualenv env python=python3.7
```
Activate vitual environment

    source env/bin/activate

## Virtual environment Configuration
Please run:

    (venv)$ pip3 install -r requirements.txt

Now we have to create environment variables

    (venv)$ export FLASK_APP=api.v1.app.py
    (venv)$ export FLASK_DEBUG=1
    (venv)$ export FLASK_ENV=development

## Run server

To run server:

    (venv)$ python3 -m api.v1.app
 
 

## Interact with the App

To check the API status when server is running

> http://localhost:5001/card_validator/api/v1.0/status

To retrieve all cards information

> http://localhost:5001/card_validator/api/v1.0/cards 
 
To retrieve a brand information
> http://localhost:5001/card_validator/api/v1.0/cards/visa
> http://localhost:5001/card_validator/api/v1.0/cards/mastercard

To check if a credit card number is valid or not (example)

> http://localhost:5001/card_validator/api/v1.0/cards/validate/377813010522325


## Author

Andrés Sotelo | Software Developer 
- [LinkedIn] (https://www.linkedin.com/in/andresotelo/)
Bogotá | Colombia