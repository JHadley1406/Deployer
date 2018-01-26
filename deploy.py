import argparse
from nginx_deploy import nginx_deploy
from uwsgi_deploy import uwsgi_deploy

# required input:
#   project
#   project_directory
#   project_url
# optional input:
#   nginx_avail_dir # default = /etc/nginx/sites-available/
#   nginx_enable_dir # default = /etc/nginx/sites-enabled/
#   uwsgi_dir # default = /etc/uwsgi/

parser = argparse.ArgumentParser(description='Deployment tool for uwsgi sites on nginx')
parser.add_argument('--nAvail',
                    dest='nginx_avail_dir',
                    default='/etc/nginx/sites-available/',
                    help='The directory where Nginx looks for available sites.  Default is /etc/nginx/sites-available/')
parser.add_argument('--nEn',
                    dest='nginx_enable_dir',
                    default='/etc/nginx/sites-enabled/',
                    help='The directory where Nginx looks for enabled sites.  Default is /etc/nginx/sites-enabled/')
parser.add_argument('--uwsgi',
                    dest='uwsgi_dir',
                    default='/etc/uwsgi/',
                    help='The default uwsgi install directory.  Default is /etc/uwsgi')
parser.add_argument('--project', dest='project', required=True, help='REQUIRED The name of the project to deploy')
parser.add_argument('--projDir', dest='project_directory', required=True, help='REQUIRED The root directory of the project')
parser.add_argument('--url', dest='project_url', required=True, help='REQUIRED The url for the project')

args = parser.parse_args()
response = ''
response += nginx_deploy(args.project, args.project_url, args.project_directory, args.nginx_avail_dir, args.nginx_enable_dir)
response += uwsgi_deploy(args.project, args.project_directory, args.uwsgi_dir)
print(response)
