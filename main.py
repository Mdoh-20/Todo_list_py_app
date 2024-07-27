import users
import TODOlists

print('Hello, this is my TODO list app')


def main():
    """
    take no arg 

    produce all the app to run
    """
    status = input(
        'Type "N" if you want to register Or "O" if you have a list... ').lower().strip()
    if status != 'n' and status != 'o':
        print('Invalid input')
        main()
    else:
        userName = input('Type your username... ').lower().strip()
        check_user(userName, status)


def check_user(userName, status):
    """
    string, char -> None

    take the username and the status of the user to 
    return the list of tasks or add a new task
    """
    found = userName in users.get_users()
    if found and status == 'o':
        print(f'Hello, {userName}')
        TODOlists.make_choice(userName)

    elif status == 'o':
        print(f'username not found.')
        check_user(input('try again... '), status)

    elif found and status == 'n':
        print(f'Sorry, this username is already taken. try other username')
        check_user(input('... '), status)

    elif not found and status == 'n':
        users.new_user(userName)
        print(f'Your username has been add to the database.')
        TODOlists.make_choice(userName)
    else:
        print('Invalid input\ntry again')
        main()


main()
