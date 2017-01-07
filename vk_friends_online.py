import vk
from getpass import getpass

APP_ID = -1


def get_user_login():
    return input('Login: ')


def get_user_password():
    return getpass()


def vk_authorize(login, password):
    return vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope="friends"
    )


def get_online_friends(session):
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline()
    return api.users.get(user_ids=friends_online_ids)


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    try:
        login = get_user_login()
        password = get_user_password()
        vk_session = vk_authorize(login, password)
        friends_online = get_online_friends(vk_session)
        print("\nДрузья онлайн:\n")
        output_friends_to_console(friends_online)
    except vk.exceptions.VkAuthError:
        print("Приложение завершилось с ошибкой")
