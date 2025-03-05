### See the deployed version [here](https://news-aggregator-next.onrender.com/)

# For Backend
Fist clone the repository.  

Create and activate **virtual environment**.

Create a **Postgres** database and a user.

Create a **.env** file and add database configuration inside it: 

**DATABASE_ENGINE = yourdatabaseengine** <br>
**DATABASE_NAME = yourdatabasename** <br>
**DATABASE_USERNAME = yourdatabaseusername** <br>
**DATABASE_PASSWORD = yourdatabasepassword** <br>
**DATABASE_HOST = yourdatbasehost** <br>
**DATABASE_PORT = yourdatabaseport** <br>

Then install requirements:
**pip install -r requirements.txt** 

After that, run migrations:
**python manage.py migrate**

Next, make migrations:
**python manage.py makemigrations api**

Run migrations again:
**python manage.py migrate**

Create a superuser:
**python manage.py createsuperuser**

Then start server to get the API up and running:
**python manage.py runserver**

# For Crawler

Open a new terminal.

Switch to the **scraper** directory in the terminal:
**cd scraper**

Then run:
**python main.py**

# For Frontend

Install node js from: https://nodejs.org/en/download/package-manager

Switch to the **news-site** directory which is inside the **frontend** directory.

Then run:
**npm i**

After that run: 
**npm start** 


Make sure the Django server is running for the UI to show the news stored in database.

You can periodically run the crawler to update new news items.

You can also delete news from the database via the **Django admin panel**.


