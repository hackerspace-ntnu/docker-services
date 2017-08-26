import sys


def generate_docker_compose(name):
    with open('docker-compose.yml', 'r') as f:
        content = f.read()
        content = content % (name, name, name)

    with open('docker-services/docker-compose.yml', 'f') as f:
        f.write(content)


if __name__ == '__main__':
    generate_docker_compose(sys.argv[1])
