#!/usr/bin/python3

# Name Ditah K
# Program name & Version: Manage hostnames
# Date: 29/10/2021
# Version: 1.0


def show_menu():
    """Displays the menu options
    """
    print('~ Hostnames Menu: ~')
    print('\tD - Display hosts')
    print('\tS - Search hosts')
    print('\tA - Add hosts')
    print('\tQ - Quit')

def get_menu_option(prompt='Enter menu selection: '):
    """Prompt user for menu option
    """
    user_option = input(prompt)
    return user_option

def get_hostinfo(prompt='Enter hostname & IP address: '):
    """Prompts the user for the hostname and IP address till the entries are validated
    """
    host_info = input(prompt)
    host_info = host_info.split(' ')
    if (host_info[-1] == ''):
        host_info = host_info[:-1]
    while (len(host_info) != 2):
        print('Input error: 2 arguments required')
        host_info = input(prompt)
        host_info = host_info.split(' ')
        if (host_info[-1] == ''):
            host_info = host_info[:-1]
    return host_info


def qualify_hostname(hostname, default_hostname='cst8245.lab'):
    """If the hostname is not qualified (it does not contain a period in the name) append the default domain name “cst8245.lab”.
    """
    if ('.' in hostname):
        return hostname
    else:
        return hostname + '.' + default_hostname

def get_search_string(prompt='Enter a search string: '):
    """Prompt user for search string
    """
    search_string = input(prompt)
    return search_string

def show_hosts(file_handler):
    """Display all hosts recorded in file
    """
    for line in file_handler:
        print(line.strip())
    file_handler.close()

def search_hosts(file_handler, search_string):
    """Match each host in the hosts file with the search string and display all matching hosts
    """
    match_found = False
    for line in file_handler:
        if (search_string in line):
            print(line.strip())
            match_found = True
    if  not match_found:
        print('No matching hosts found')
    file_handler.close()
    return match_found


def add_host(file_handler, host_info):
    """Append entry to hostnames file
    """
    host_info_str = '\n' + host_info[0] + ' ' + host_info[1]
    file_handler.write(host_info_str)
    file_handler.close()

def open_read(filename="hostnames.txt"):
    """Open file in read mode with exception handling and return file handle or raise exception
    """
    try:
        file_handler = open(filename, "r")
        return file_handler
    except(FileNotFoundError):
        print(f'Unable to find the file: \'{filename}\'')

def open_append(filename="hostnames.txt"):
    """Open file in append mode with exception handling and return file handle or raise exception
    """
    try:
        file_handler = open(filename, "a")
        return file_handler
    except(FileNotFoundError):
        print(f'Unable to find the file: \'{filename}\'')

if __name__ == '__main__':
    show_menu()
    user_option = get_menu_option()
    while (user_option.lower() != 'q'):
        if (user_option == 'd'):
            # display hosts
            read_handler = open_read()
            show_hosts(read_handler)
        elif (user_option == 's'):
            # search hosts
            search_query = get_search_string()
            read_handler = open_read()
            search_hosts(read_handler, search_query)
        elif (user_option == 'a'):
            # add hosts
            append_handler = open_append()
            host_info = get_hostinfo()
            host_info[0] = qualify_hostname(host_info[0])
            add_host(append_handler, host_info)
        else:
            print('Invalid entry: Please select a valid menu option')

        show_menu()
        user_option = get_menu_option()
