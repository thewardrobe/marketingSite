# The Wardrobe
Outfit recommendation app according to *your* wardrobe.

## Table of Contents

1. [Development](#development)
  1. [Setup](#setup)
  2. [Installing Dependencies](#installing-dependencies)
  3. [Running in Development](#running)
2. [Stack](#Stack)

## Development

### Setup
- Install Redis
  ```
  brew install redis
  ```
- Install [Postgres.app](http://postgresapp.com/)
- Run Postgres.app
- Open psql in command line and create wardrobe database
  ```
  CREATE DATABASE wardrobe
  \c wardrobe
  ```
- Create virtual environment for Python dependencies:
  ```
  virtualenv venv
  source venv/bin/activate
  ```

### Installing Dependencies
- Install python dependencies:
  ```
  pip install -r requirements.txt
  ```

### Running
```
redis-server
python run.py
``` 

## Stack

- Angular
- Python
- PostgreSQL
- SQLAlchemy