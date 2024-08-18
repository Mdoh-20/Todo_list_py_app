import src.users


def main():
    """run the main program"""
    src.users.check_username(src.users.take_username())


if __name__ == '__main__':
    print('welcome, this todo list app')
    main()
