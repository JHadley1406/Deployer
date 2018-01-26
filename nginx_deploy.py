import os
from subprocess import call


def nginx_deploy(project,
                 url,
                 project_directory,
                 nginx_avail_dir,
                 nginx_enable_dir):

    nginx_file_data = "server {{\n\tlisten 80;\n" \
                      "\tserver_name {1};\n\n" \
                      "\tlocation /static/ {{\n" \
                      "\t\talias {2}static_root/;\n" \
                      "\t}}\n\n" \
                      "\tlocation / {{\n" \
                      "\t\tinclude uwsgi_params;\n" \
                      "\t\tuwsgi_pass unix:{2}{0}.sock;\n" \
                      "\t}}\n}}"

    nginx_file_name = nginx_avail_dir+'{0}.conf'.format(project)

    if not os.path.exists(nginx_avail_dir) or not os.path.exists(nginx_enable_dir):
        return "One of the nginx directories does not exist, is Nginx installed?\n"

    if os.path.isfile(nginx_file_name):
        return "Nginx config file {0} already exists.\n".format(nginx_file_name)

    nginx_file = open(nginx_file_name, 'w')
    nginx_file.write(nginx_file_data.format(project, url, project_directory))
    nginx_file.close()
    call(['ln', '-s', nginx_file_name, nginx_enable_dir+'{0}.conf'.format(project)])
    return "Nginx configured for {0}\n".format(project)
