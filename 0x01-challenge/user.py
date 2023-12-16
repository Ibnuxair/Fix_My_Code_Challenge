#!/usr/bin/python3
"""
User class
"""

class User():
    """ Defines a user. """

    def __init__(self):
        """ Initializes instance. """
        self.__email = None

    @property
    def email(self):
        """ Gets the email. """
        return self.__email

    @email.setter
    def email(self, value):
        """ Sets the email. """
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
                                                                                                                        
