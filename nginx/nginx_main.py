import sys

TEMPLATE_PATH = '/tmp/docker-services/nginx/templates/outer_main.conf'
DESTINATION_PATH = '/etc/nginx/sites-enabled/main.conf'

def generate_main_nginx_config(server_name, domain):
    with open(TEMPLATE_PATH, 'r') as f:
        content = f.read()
        config = content % {'server_name': server_name.replace('__', ' '), 'domain': domain}
        with open(DESTINATION_PATH, 'w') as f:
            f.write(config)


if __name__ == '__main__':
    generate_main_nginx_config(*sys.argv[1:3])
