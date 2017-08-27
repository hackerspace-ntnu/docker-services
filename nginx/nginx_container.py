from os.path import join, split
import sys

TEMPLATE_PATH = './templates/outer_container.conf'
DESTINATION_PATH = '/etc/nginx/sites-enabled/container_%(subdomain)s.conf'

ROOT_PATH = split(__file__)[0]


def generate_nginx_config(server_name, domain, subdomain, port):
    """
    Reads in a file from templates and inserts the correct server_name according to the subdomain argument.
    """
    with open(join(ROOT_PATH, TEMPLATE_PATH), 'r') as file:
        config = file.read()
        final_config = config % {'server_name': server_name.replace('__', ' '), 'port': port, 'domain': domain}

        with open(DESTINATION_PATH % {'subdomain': subdomain}, 'w') as config_file:
            config_file.write(final_config)


if __name__ == '__main__':
    generate_nginx_config(*sys.argv[1:5])
