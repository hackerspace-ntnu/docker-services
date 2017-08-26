from os.path import join, split
import sys

server_name = "{}.hackerspace-ntnu.no www.{}.hackerspace-ntnu.no {}.idi.ntnu.no www.{}.idi.ntnu.no;"
TEMPLATE_PATH = './templates/site'

ROOT_PATH = split(__file__)[0]


def generate_nginx_config(subdomain):
    """
    Reads in a file from templates and inserts the correct server_name according to the subdomain argument.
    """
    server_name_str = server_name.format(*[subdomain] * 4)
    with open(join(ROOT_PATH, TEMPLATE_PATH)) as file:
        config = file.read()
        final_config = config % {'server_name': server_name_str}

        with open(join(ROOT_PATH, 'sites-enabled/site'), 'w') as config_file:
            config_file.write(final_config)


if __name__ == '__main__':
    generate_nginx_config(sys.argv[1])
