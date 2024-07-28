import todo_app
# user functions file


def check_user(userName, status):
    """string, char -> None

    take the username and the status of the user to 
    return the list of tasks or add a new task
    """
    found = userName in get_users()

    if found and status == 'o':
        print(f'Hello, {userName}')
        todo_app.make_choice(userName)

    elif status == 'o':
        print(f'username not found.')
        check_user(input('try again... '), status)

    elif found and status == 'n':
        print(f'Sorry, this username is already taken. try other username')
        check_user(input('... '), status)

    elif not found and status == 'n':
        new_user(userName)
        print(f'Your username has been add to the database.')
        todo_app.make_choice(userName)
    else:
        print('Invalid input\ntry again')
        check_user(input('Inter your user name ...').lower().strip(),
                   input('O for old user, N for new user').lower().strip())


def get_users() -> list[str]:
    """take no arg

    return list of users (string)
    """
    content = []
    with open('./database/usernames.txt') as data:
        for row in data:
            line = row.split(',')
            for word in line:
                content.append(word)
    return content


def new_user(username: str) -> None:
    """
    username is a string

    take string (username) and add it to the data base file
    """
    with open('./database/usernames.txt', 'a') as data:
        data.write(f'{username},')

    with open(f'./database/{username}.txt', 'w') as newFile:
        newFile.write(f'\nHello this {username} tasks file')

# for test do not need this now
# print(new_user('mohamed'))
# print(get_users())
