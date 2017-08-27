import sys


def generate_docker_compose(subdomain, port):
    with open('docker-compose.yml', 'r') as f:
        content = f.read()
        compose = content % {'subdomain': subdomain, 'website_port': int(port) + 1, 'proxy_port': port}

    with open('docker-compose.yml', 'w') as f:
        f.write(compose)


if __name__ == '__main__':
    generate_docker_compose(*sys.argv[1:3])
