# BCard

## Documentation
 is deployed to Render.com, You can use it and find documentation on
[]()


## Technologies

- Python
- FastAPI
- MongoDB
- Render
- CRUD REST API


## Run Locally for Development

Clone the project

```
  git clone https://github.com/
  cd BCard-API
```

Create a .env file in /etc/secrets/
```
  DBUSER = MongoDB username
  DBPASS = MongoDB password
  DBNAME = MongoDB database name
  COLNAME = MongoDB collection name
```
Or just change the code in config/database.py to suit your needs

Create a python virtual environment and actiavte it
```
  python -m venv venv
  source venv/bin/activate
```
Install dependencies

```
  pip install -r requirements.txt
```

Start the server

```
  uvicorn BCard:app --reload
```

Access the server

  - http://localhost:8000