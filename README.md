# Deployer
A command line tool for deploying django projects using nginx and uwsgi

Accepts the following commands:
##### Required #####
- project
>- The project name (usually whatever was used when running django-admin startproject)
- projDir 
>- The root directory for the project
- url
>- The URL for the site
##### Optional #####
- nAvail
>- The directory for available nginx config files
>- Defaults to /etc/nginx/sites-available/
- nEn
>- The directory for enabled nginx config files
>- Defaults to /etc/nginx/sites-enabled/
- uwsgi
>- The uwsgi directory 
>- Defaults to /etc/uwsgi/

##### Example #####
~~~~
$ sudo python3 deploy.py --project Foo --projDir /var/www/foo --url www.foo.com
Nginx configured for Foo
Uwsgi configured for Foo
~~~~
