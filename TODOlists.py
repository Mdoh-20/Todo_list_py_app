# the main logic here
# get_list to return the task list
# Or add_task to add a new one to the database

import os.path


def get_list(userName) -> list[str]:
    """
    string -> list[str]

    username: string 
    take the username and return the list of tasks
    """
    find(userName)
    with open(f'./database/{userName}.txt', 'r') as data:
        for row in data:
            print(row)


def add_task(userName: str) -> None:
    find(userName)
    with open(f'./database/{userName}.txt', 'a') as data:
        newTask = input('Inter your new task... ')
        data.write(f'\n{newTask}')
        print('the task has been add successfully')
        make_choice(userName)


def find(userName):
    """
    string -> None

    take username and checks if it has a database or not 
    if has a database then pass
    if it has not make database for it
    """
    if not os.path.isfile(f'./database/{userName}.txt'):
        print(f"Your file is not here i'll make you a new one")
        with open(f'./database/{userName}.txt', 'w') as newFile:
            make_choice(userName)


def make_choice(userName):
    """
    string -> list[str] | write to some file

    take the username to show | write the tasks in the right place 
    """
    answer = input(
        'type A to add a new task, S to show your task list Or q for quit... ').lower()
    if answer == 's':
        get_list(userName)
    elif answer == 'a':
        add_task(userName)
    elif answer == 'q':
        quit()
    else:
        print('invalid input')


# get_list('tarek')
# add_task('amr')
# make_choice('marwan')
