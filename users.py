# import csv

# user functions file


def get_users() -> list[str]:
    """
    take no arg

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
        newFile.write(f'Hello this {username} tasks file')


# print(new_user('mohamed'))
# print(get_users())
