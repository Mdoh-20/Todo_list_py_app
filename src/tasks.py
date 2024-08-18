import sqlite3


connection = sqlite3.connect('src/db_file.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS usersTable (name TEXT,
                    password TEXT)''')


def get_tasks(userName) -> None:
    """print the tasks table of the user"""
    print(f'check your tasks')
    content = cursor.execute(f'SELECT * FROM {userName}Table')
    for cont in content.fetchall():
        print(f'{cont[0]},{cont[1]},{cont[2]}')


def add_task(userName):
    """add new task to the database"""
    get_tasks(userName)
    try:
        newTask = input('type the new task... ')
        taskNumber = input('Inter the task number you want to add... ')
    except KeyboardInterrupt:
        print('the program has ended')
        quit()
    try:
        cursor.execute(f'INSERT INTO {userName}table (id, task, status) VALUES (?, ?, ?)'
                       ,(taskNumber, newTask, 'not yet'))
    except sqlite3.IntegrityError:
        cursor.execute(f'INSERT INTO {userName}table (task, status) VALUES (?, ?)'
                       , (newTask, 'not yet'))
    connection.commit()
    return edit_tasks(userName)


def rm_task(userName):
    """remove task from the database"""
    get_tasks(userName)
    try:
        taskNumber = input('Inter the task number you want to remove... ')
    except KeyboardInterrupt:
        print('the program has ended')
        quit()
    try:
        cursor.execute(f'DELETE FROM {userName}table WHERE id = (?)',taskNumber)
        connection.commit()
        return edit_tasks(userName)
    except sqlite3.ProgrammingError:
        print('the given task number do NOT EXISTS')
        quit()


def change_statu(userName):
    """update the status of some task in the database"""
    get_tasks(userName)
    ids = cursor.execute(f'SELECT id FROM {userName}table')
    try:
        taskNumber = int(input('Inter the task Number that you want to update... '))
        if not (taskNumber,) in ids.fetchall():
            print('nothing to update')
            return edit_tasks(userName)
        statusUpdate = input('Update to... ')
    except KeyboardInterrupt:
        print(' Something went wrong.')
        quit()
    except ValueError:
        print('Invalid input')
        change_statu(userName)

    cursor.execute(f'UPDATE {userName}table SET status = (?) WHERE id = (?)',
                   (statusUpdate, taskNumber))
    connection.commit()
    print('done updating')
    return edit_tasks(userName)


def edit_tasks(userName):
    """edit the tasks after take input from the user"""
    try:
        decision = input('Type "a" for append new task, "rm" to remove task,'
                         'C to change the status,S to display the tasks Or q'
                         'to Quit... ').lower().strip()
    except KeyboardInterrupt:
        print('Invalid input')
        quit()
    match decision:
        case 'a' | 'append':
            add_task(userName)
        case 'r' | 'rm' | 'remove' | 'd' | 'delete':
            rm_task(userName)
        case 'c' | 'change':
            change_statu(userName)
        case 's' | 'show':
            get_tasks(userName)
            edit_tasks(userName)
        case 'q' | 'quit':
            print('the program has ended')
            quit()
        case _:
            print('Invalid input')
            edit_tasks(userName)

if __name__ == '__main__':
    # sqliteConnection = sqlite3.connect('database/db_file.db')
    # cursor = sqliteConnection.cursor()
    # cursor.execute('''CREATE TABLE IF NOT EXISTS todoTable (id INTEGER NOT NULL
    #                 PRIMARY KEY AUTOINCREMENT UNIQUE, task TEXT, status TEXT)
    #                 ''')
    # edit_tasks()
    change_statu('marwan')
    connection.close()