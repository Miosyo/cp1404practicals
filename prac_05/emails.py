"""
Emails
Estimate: 20 minutes
Actual:    21 minutes
"""


def main():
    """A program to store and print emails and names"""
    user_to_email = {}
    user_name, email = get_email()
    while email != "":
        choice = input(f"Is your name {user_name}? (Y/n) ")
        if choice not in "Yy ":
            user_name = input("Name: ")
        user_to_email[user_name] = email
        user_name, email = get_email()
    for user, email in user_to_email.items():
        print(f"{user} ({email})")


def get_email():
    """Get email from user"""
    email = input("Email: ")
    user_name = " ".join(email.split('@')[0].split('.')).title()
    return user_name, email


if __name__ == '__main__':
    main()
