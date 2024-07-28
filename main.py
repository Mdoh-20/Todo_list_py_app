import users
import todo_app

print('Hello, this is my TODO list app')


def main():
    """
    take no arg

    produce all the app to run
    """
    status = input('Type "N" if you want to register Or "O"'
                   'if you have a list... ').lower().strip()
    if status != 'n' and status != 'o':
        print('Invalid input')
        main()
    else:
        userName = input('Type your username... ').lower().strip()
        users.check_user(userName, status)


main()
