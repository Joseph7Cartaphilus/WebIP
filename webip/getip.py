import socket


def get_ip_by_hostname():
    hostname = input("Enter a website address(URL): ")

    try:
        return f'Hostname: {hostname}\n Ip address: {socket.gethostbyname(hostname)}'

    except socket.gaierror as error:
        return f'Invalid Hostname - {error}'


def main():
    print(get_ip_by_hostname())


if __name__ == '__main__':
    main()
