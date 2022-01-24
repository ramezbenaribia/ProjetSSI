import getpass

from DBFunction.repository import UserRepository


def login(user_repo: UserRepository):
    print(
        "********************************* Login **************************************"
    )
    email = None
    password = None
    while email is None and password is None:
        email = str(input("Enter your email: "))
        password = getpass.getpass("Enter your password: ")

    login_result = user_repo.login(email=email, password=password)
    if login_result is True:
        print("Login Successfully!")
    else:
        print("Please verify your email and password and re-login!")
