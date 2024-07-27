import os.path


def get_list(userName) -> list[str]:
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
    if not os.path.isfile(f'./{userName}.txt'):
        print(f"Your file is not here i'll make you a new one")
        with open(f'./database/{userName}.txt', 'w') as newFile:
            pass
    make_choice(userName)


def make_choice(userName):
    answer = input(
        'type A to add a new task Or S to show your task list... ').lower().strip()
    if answer == 's':
        get_list(userName)
    elif answer == 'a':
        add_task(userName)
    else:
        print('invalid input')


# get_list('tarek')
# add_task('amr')
