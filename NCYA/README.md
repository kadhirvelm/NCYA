# NCYA Website - Django and React

## Before Everything

We'll need to first activate the virtual environment that has all the dependencies installed.

```
cd into the directory
source env/bin/activate (quit using deactivate)
```

### Testing entire application

We'll need to simply start the server, though we'll need to compile the React application first.

```
cd into NCYA/
./node_modules/.bin/webpack --config webpack.config.js
python manage.py runserver
```
Make sure to handle any errors through by the babel-loader. *Note: The babel loader does not like CSS files. Will fix this later.*

### Testing just React

```
cd ./assets/js/ncya-website
npm start
```

### General Notes

Website is the main Django application that stores the models, etc. The React application gets access through Website/templates/index.html. Don't forget there's some convention over configuration going on, so don't change any of the names without thoroughly testing. Django does a lot of this under the hood for us. Do all the db migrations using Website.

NCYA is a django app that the babel and webpack loaders were initiated into, not to mention all the urls for the app. Ideally using React this should be an entirely single page application, so there shouldn't be any need to touch the NCYA folder.

The assets folder also has some convention over configuration. Was not able to easily change the name to be more descriptive without breaking the application - currently a work in progress. The asset folder houses the React application inside the js folder, keep all react related items in there. Don't forget to recompile the React app using the webpack whenever you want to load it into the main application. JQuery should work, it was installed, will make sure it can interact with the django DB later.

Install all dependencies using `npm install {PACKAGE} --save` in the main root folder. It'll help keep all the dependencies in a single place, making launching the website signficantly easier.

### Sources
-http://www.django-rest-framework.org/tutorial/1-serialization/
-http://geezhawk.github.io/using-react-with-django-rest-framework