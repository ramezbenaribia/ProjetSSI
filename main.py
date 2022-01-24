from DBFunction.db_connector import DBConnector
from DBFunction.email_service import EmailService
from DBFunction.repository import UserRepository

from phase1 import register
from phase2 import authentification
from phase3.menu import phase3Menu


if __name__ == "__main__":
    user_choice = None
    DB_HOSTNAME = "localhost"
    DB_USER = "ramez"
    DB_PASSWORD = "ramez"
    DB_DATABASE = "ssi"
    EMAIL_LOGIN = "ramez.css@gmail.com"
    EMAIL_PASSWORD = "Ramez20622"
    conn = DBConnector.Instance(
        hostname=DB_HOSTNAME,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE,
    )
    email_service = EmailService(
        sender_email=EMAIL_LOGIN, sender_password=EMAIL_PASSWORD
    )
    user_repo = UserRepository(db_connector=conn, email_service=email_service)
    while user_choice != 4:
        user_choice = int(
            input(
                "Enter your choice: \n"
                "1. register a new user.\n"
                "2. login a user.\n"
                "3. Go to phase3 so you can Encrypt or  Decrypt a Message .\n"
                "4. To quit.\n"
            )
        )
        if user_choice == 1:
            register.sign_up(user_repo=user_repo)
            print()
            print()
        elif user_choice == 2:
            authentification.login(user_repo=user_repo)
            print()
            print()
        elif user_choice == 3:
            phase3Menu()
