clients = 'bryan, estiven, carlos, pedro'


def _add_coma():
    global clients
    if clients != '':
        clients += ', '


def create_clients(client_name):
    global clients
    if client_name.lower() not in clients:
        _add_coma()
        _print_message('Client save\n')
        clients += client_name.lower()
    else:
        _print_message(client_name + ' already is in the client\'s list')


def list_clients():
    global clients
    if clients != '':
        print(('-' * 20) + 'Clients list' + ('-' * 20))
        print(clients.title())
    else:
        print('Aún no existen clientes.')


def _print_welcome():
    print('WELCOME TO XXXX VENTAS')
    print('*' * 50)
    print('What would you like to do today? ')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')
    print('[L]ist client')


def _print_message(message):
    print(message)


def delete_client(client_name):
    global clients
    if client_name in clients:
        finish = clients.rfind(client_name) + len(client_name)

        if clients.find(client_name) == 0:
            clients = clients.replace(client_name + ', ', '')
        elif finish == len(clients):
            clients = clients.replace(', '+client_name, '')
        else:
            clients = clients.replace(', '+client_name, '')

    else:
        _client_not_found(client_name)


def _client_not_found(client_name):
    print('client' + client_name + ' does not exist in the list')


def update_client(client_name, update_client_name):
    global clients
    if client_name.lower() in clients:
        clients = clients.replace(client_name, update_client_name.lower())
        _print_message('update client')
    else:
        _client_not_found(client_name)


def set_client_name():
    client_name = None
    while not client_name or not client_name.isalpha():
        client_name = str.lower(input('What is the client name? '))

    return client_name


if __name__ == '__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = set_client_name()
        create_clients(client_name)
        list_clients()
    elif command == 'D':
        client_name = input('What is the client name? ')
        delete_client(client_name)
    elif command == 'U':
        client_name = set_client_name()
        update_client_name = input('What is the update client name? ')
        update_client(client_name, update_client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    else:
        print('Invalid command')
