# news_reader

A Django project that fetches news from API.\
Users can choose to save posts without having an account.

## Requirements

- Api key from [newsapi](https://newsapi.org/).

## Installation

To install and run the project: 
 - Add your api key to a .env-file in news_reader/news_reader/.env like so `NEWS_API_KEY=<Your_api_key>`
 - Open a terminal in the project directory
 - (optional) create a virtual environment:
 - - run `python -m venv <name of virtual environment>`
 - - activate virtual environment:
 - - - Unix: `source <name of virtual environment>/bin/activate`
 - - - Windows: `<name of virtual environment>\Scripts\activate.bat`
 - run `pip install -r requirements.txt`
 - run `python manage.py migrate`
 - run `python manage.py runserver`

## Using the project

While the server is running, it should by default be running on `localhost:8000`.\
Open `localhost:8000/news` in a browser and the news should start showing up.\
To save a news post, simply press `Save article` and it should automatically show up in the top of the page.\
To delete a post, press `Delete from saved` and it should be removed from your saved posts.
