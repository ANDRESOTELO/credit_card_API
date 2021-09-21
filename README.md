# Credit card number validator API
I have been asked to create a web application with which the user can interact and validate if a credit card number is valid or not

# Technologies and tools
For the backend:
- Python
- Flask
- Git
- Docker

## To run application in console
### Virtual environment
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

    (env)$ pip3 install -r requirements.txt

Now we have to create environment variables

    (env)$ export FLASK_DEBUG=1
    (env)$ export FLASK_ENV=development

## Run server

To run server:

    (env)$ python3 -m api.v1.app
 

## Docker image
To pull docker container
```bash
docker pull andresotelo/creditcard_v1
```
To run docker container
```bash
docker run -p 5000:5000 creditcard_v1
```
## Interact with the App

Please open other terminal an run

To check the API status when server is running
```bash
curl http://localhost:5001/card_validator/api/v1.0/status
```

To retrieve all cards information
```bash
curl http://localhost:5001/card_validator/api/v1.0/cards 
```

To retrieve a brand information

```bash
curl http://localhost:5001/card_validator/api/v1.0/cards/visa
```

```bash
curl http://localhost:5001/card_validator/api/v1.0/cards/mastercard
```

To check if a credit card number is valid or not (example)

```bash
curl http://localhost:5001/card_validator/api/v1.0/cards/validate/377813010522325
```

## Author

Andrés Sotelo | Software Developer | Backend 
- [LinkedIn] (https://www.linkedin.com/in/andresotelo/)
Bogotá | Colombia
