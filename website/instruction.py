# Inisialization
# 1. Create Django project using "django-admin startproject project_name" in Terminal (project_name: website)
# 2. Create the main app using "python manage.py startapp app_name" creating a main directory (app_name: main)
# 3. There will be 2 folder inside the project folder, the project folder (website) and the main folder (main)

# Website Directory
# 1. In settings.py we can adjust our settings for the project
# 1a. Add installed apps ad framework in "INSTALLED APPS"
# 1b. Add database informations in "DATABASES"
# 1c. Add "CRISPY_ALLOWED_TEMPLATE_PACKS" and "CRISPY_TEMPLATE_PACK" to activate crispy forms
# 1d. Add "LOGIN_REDIRECT_URL" and "LOGOUT_REDIRECT_URL" to redirect everytime you login or logout
# 2. In urls.py will connect the website.urls.py and main.urls.py
# 2a. Add "path('', include('main.urls'))" in urlpatterns to connect all to main.urls.py
# 2b. Add "path('', include('django.contrib.auth.urls'))" to use autentication template from Django

# Main Directory
# 1. Create a templates folder for bootstraps (*go to Bootstraps parts)
# 1. In urls.py will list all of the urls path in your websites
# 2. In views.py will manage the display for each urls and connect it with bootstrap
# 3. In models.py manage the model feature we wanted to add on our website that creates the tables in our database
# 3a. Add the model class which will specify all the data and data type
# 3b. To add the table into database, use the command "python manage.py makemigrations" and then "python manage.py migrate"
# 4. Create forms.py to handle all the category that should be filled in the forms
# 4a. The forms will be wrapped in crispy-forms in using "{{form|crispy}}"

# Bootstrap
# 1. Inside the template folder add two folder called "main" and "registration"
# 2. The main folder will manage the display for each urls
# 2a. Create a base template called "base.html" where we can extend the code
# 2a. To generate pre-build html code, change the language to HTML and type "html:5"
# 2a. On bootstrap website, copy CSS link inside header and bundle link inside the body
# 2a. Create a modify block using {% block title %}...{% endblock %} command
# 2b. Create a home page called "home.html" that extend from base template using "{% extends 'main/base.html' %}"
# 2c. Create a posting page called "post.html" that also extend from base template
# 3. The registration folder will manage the registration, sign-in, etc urls
# 3a. Create a login page called "login.html"
# 3a. Load the crispy forms using "{% load crispy_forms_tags %}" command and add the <form> tags
# 3a. Add "csrf token" with every method like 'post' or 'get' in the form using "{% csrf_token %}"
# 3a. Add the crispy forms template to the form that we will make "{{form|crispy}}"
# 3b. Create a sign up page called "sign-up.html" using the same method as login.html

# To run the apps use the command "python manage.py runserver" in cmd