import sys

server_name = "{}.hackerspace-ntnu.no www.{}.hackerspace-ntnu.no {}.idi.ntnu.no www.{}.idi.ntnu.no;"
TEMPLATE_PATH = './templates/site'


def generate_nginx_config(subdomain):
    """
    Reads in a file from templates and inserts the correct server_name according to the subdomain argument.
    """
    server_name_str = server_name.format(*[subdomain] * 4)
    with open(TEMPLATE_PATH) as file:
        config = file.read()
        final_config = config % {'server_name': server_name_str}

        with open('./sites-enabled/site', 'w') as config_file:
            config_file.write(final_config)


if __name__ == '__main__':
    generate_nginx_config(sys.argv[1])
