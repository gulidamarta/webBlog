# Starting your Django project

You've installed Python and the other utilities (pip, virtualenv, and git) on
your computer, right? If not, [head here to
install](https://github.com/limedaring/HelloWebApp/tree/master/installation-instructions).

First thing you need to do is create a folder for your project. I personally use
a "projects" folder in my top level user folder on my computer, which contains
all my programming projects. If you'd like to do this as well, follow these
commands in your terminal to create the projects folder, and a folder within for
this individual project:

```
$ mkdir projects
$ cd projects
projects $ mkdir yourwebsite
projects $ cd yourwebsite
```

If you need a command line review, `mkdir` creates folders, and `cd` changes
directories into that folder. If you ever get lost, your terminal should show
which directory you're in, and running `ls` (on Mac or Linux, `dir` on Windows),
will list out the contents of the folder you're in. Use `cd ..` to back up out
of a folder.

### Start your virtual environment

Now that you're within your empty project folder, create your virtual
environment. We'll be using virtualenv.

```
projects/yourwebsite $ virtualenv evavenv
```

And then activate the environment:

```
projects/yourwebsite $ cd evavenv/Scripts/activate
```

You should see something like this in your command line before the folder
structure - the (evavenv) indicates you're in the virtual environment:

```
(evavenv)path_to_the_file> $
```

(path to the file, where you created the folder evavenv)

Now you're in your bubble, so we can start installing project-specific utilities.
If you ever need to deactivate your environment, run `deactivate`.

### Install Django

Finally, it's Django time! We'll use pip to install Django, so run this in your
command line, making sure you're in your project folder and the virtual
environment is activated:

```
(evavenv) path_to_the_file> pip install Django==2.2.4
```

We're telling pip to install a specific version of Django, in case Django
releases a new version that this tutorial doesn't cover.

### Start git

We also want to start our version control system. Now that we're in our project
folder, run this command to start git:

```
$ git init
```

Running this command in your project folder will make the entire folder and its
contents part of a new Git repository.

### Start your Django project

We installed Django, now we can use Django to build all the starting files we
need for our web app. In your command line (again, in your project folder with
your environment activated):

```
$ django-admin.py startproject hellowebapp .
```

This is going to start a Django project in your currect directory.

* django-admin.py: The script we'll be running.
* startproject: The specific utility we're using.
* evablog: The name we're giving the project.
* . : The location where we're starting the project, with `.` denoting the
  current directory.

`startproject` will create these files and folders:

```
evablog/
    manage.py
    evablog/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

The evablog folder is your top level folder.

* `manage.py`: We won't edit this file, but will use this file in the command line
  to interact with your project. You'll see it in action soon.
* The inner `evablog` folder holds your project.
* `__init__.py`: Ignorable - tells Python that this is a Python package.
* `settings.py`: Aptly named - contains your settings.
* `urls.py`: URL declarations for the project. 
* `wsgi.py`: Not needed at this point until you deploy your project.

### Create a Django app

A project can run many apps (all doing something distinct), but we're just going
to focus on having one for now, which is all you'll need for a very long
time.

In your top level folder (the one with *manage.py* in it), run this command:

```
$ django-admin.py startapp articles
```

Like before, `django-admin.py` is the script, `startapp` is the command, and
`articles` is the name we're giving the app, which you can change if you wish.

`startapp` will create an additional folder and a few files:

```
evablog/
    manage.py
    articles/
        __init__.py
        admin.py
        migrations/
        models.py
        tests.py
        views.py
    evablog/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

Note the additional "articles" folder in your project.

* `__init__.py`: Ignorable.
* `admin.py`: Contains admin codebits.
* `models.py`: Where you'll define the dynamic data that'll go in your database.
* `tests.py`: Tests you'll create to run to test your app automatically.
* `views.py`: Where the logic goes that powers your website.


### Add your new app to your settings file

We need to tell the project that we've added an app to it.  Open up your
`settings.py` file (which is under your `evablog` folder, see the directory
tree above).

Find the `INSTALLED_APPS` and add the name of your app to the beginning of the list
(don't forget the trailing comma):

``` python
INSTALLED_APPS = (
    'collection', # this is the app we added
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
```

## Set up your database

Django has some fancypants utilities built in to keep your database (where
all your dynamic information is stored) managable. We need to run the initial
migration before we start the app, so in your top level folder (the one with
*manage.py* in it), type this in:

```
$ python manage.py migrate
```

It's going to create your database automatically for you and port over some
information. 

## Start your Django web app

Want to see if everything worked? In your terminal, head over to your top level
evablog folder (make sure you're in the folder with *manage.py*) and run
this command:

```
$ python manage.py runserver
```

...and you'll see the local Django development server starting, which'll serve
your project to your computer.

```
Validating models...

0 errors found
Septermber 30, 2019 - 12:00:00
Django version 1.7.8, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Now just head to your favorite web browser and visit
[http://127.0.0.1:8000](http://127.0.0.1:8000), where you'll see a "Welcome to
Django" page. Congrats on starting Django!

