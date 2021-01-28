# Installation
* Follow the instructions at [the django windows install page](https://docs.djangoproject.com/en/3.1/ref/contrib/gis/install/#windows) to install postgres, postgis, and OSGeo4W, then modify your windows environment.
* [Create an empty postgis database in pgadmin](https://postgis.net/workshops/postgis-intro/creating_db.html), call the database `hyperion`.
* [Create a user named hyperion in pgadmin](https://www.enterprisedb.com/postgres-tutorials/how-create-postgresql-database-and-users-using-psql-and-pgadmin).  Give him a password of `hyperion` and give him login, superuser, and create permissions.
* Run migrations `python manage.py migrate`
# Populating Country Data
* Run the django shell by typing `python manage.py shell`
* From the shell type `from world import load` and then `load.run()`
# Important
* Dont run makemigrations unless you're caught up with the latest version on git.
