import os

def uwsgi_deploy(project,
                 project_directory,
                 uwsgi_dir):
    uwsgi_file_data = "[uwsgi]\n" \
                      "uid = www-data\n" \
                      "gid = www-data\n" \
                      "pythonpath = /usr/local/lib/python2.7/dist-packages\n" \
                      "pythonpath = /usr/lib/python2.7\n" \
                      "project = {0}\n" \
                      "base = {1}\n\n" \
                      "chdir = %(base)\n" \
                      "home = %(base)\n" \
                      "wsgi-file = %(base)/%(project)/wsgi.py\n\n" \
                      "master  true\n" \
                      "processes = 2\n" \
                      "socket = %(base)/%(project).sock\n" \
                      "chmod-socket = 664\nvacuum = true\n" \
                      "no-site = true\n" \
                      "logto = /tmp/%(project).uwsgi"


    if not os.path.exists(uwsgi_dir):
        return "Could not find uwsgi directory, is uwsgi installed?\n"
    uwsgi_sites_dir = uwsgi_dir+'sites/'
    os.makedirs(uwsgi_sites_dir, exist_ok=True)

    uwsgi_file_name = uwsgi_sites_dir+'{0}.ini'.format(project)

    if os.path.isfile(uwsgi_file_name):
        return "Uwsgi config file {0} already exists.\n".format(uwsgi_file_name)

    uwsgi_file = open(uwsgi_file_name, 'w')

    uwsgi_file.write(uwsgi_file_data.format(project, project_directory))
    uwsgi_file.close()
    return "Uwsgi configured for {0}\n".format(project)
