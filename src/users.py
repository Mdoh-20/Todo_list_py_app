import src.tasks
from src.tasks import cursor,connection


def take_username() -> str:
    """just take a username from the user"""
    try:
        return input('Type your username to continue... ').lower().strip()
    except KeyboardInterrupt:
        print('Somthing went wrong.')
        quit()

def check_username(userName:str):
    """check if the username in the database"""
    if (userName,) in users_list():
        try:
            password = input('Inter your password... ')
        except KeyboardInterrupt:
            print('Somthing went wrong.')
            quit()
        pas = cursor.execute('SELECT password FROM usersTable WHERE name = ?'
                             , (userName,))
        if (password,) == pas.fetchone():
            return src.tasks.edit_tasks(userName)
        else:
            print('wrong password bro, try again')
            check_username(userName)
    else:
        return user_not_found(userName)


def users_list():
    """produce list of str (list[username]) from the database"""
    users = cursor.execute('SELECT name FROM usersTable')
    return users.fetchall()


def new_user(userName):
    """ Add the new username to the database """
    try:
        password = input('Inter a password... ')
    except KeyboardInterrupt:
        print('Somthing went wrong.')
        quit()
    cursor.execute('INSERT INTO usersTable (name, password) VALUES (?, ?)'
                   , (userName, password))
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {userName}Table (id INTEGER
                    NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, task TEXT NOT 
                    NULL, status TEXT)''')
    connection.commit()
    print('your username has been add successfully')
    return src.tasks.edit_tasks(userName)


def user_not_found(userName: str) -> None:
    """add new user or try the username again"""
    print("can't find your username, are you a new user or want to try "
          "again?")
    try:
        answer = input('Type "N" to register Or anything to try your username '
                       'again... ').lower().strip()
    except KeyboardInterrupt:
        print('Somthing went wrong.')
        quit()
    if answer == 'n':
        new_user(userName)
    else:
        check_username(take_username())

if __name__ == '__main__':
    print('before')
    print(users_list())
    print('after')
