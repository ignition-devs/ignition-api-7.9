__all__ = ["ContactInfo", "User"]

import pprint

from java.lang import Object


class ContactInfo(Object):
    def __init__(self, contactType=None, value=None):
        self.contactType = contactType
        self.value = value

    def getContactType(self):
        pass

    def getValue(self):
        pass

    def setContactType(self, contactType):
        pass

    def setValue(self, value):
        pass


class User(object):
    Username = "johdoe"
    FirstName = "John"
    LastName = "Doe"
    Email = "johdoe@mycompany.com"
    Notes = "These are some notes."
    Roles = ["Administrator", "Developer"]
    Schedule = "Always"
    Language = "en_US"

    def get(self, prop):
        """Returns a the value of the requested item.

        Args:
            prop (User property): The user property to retrieve.

        Returns:
            str: The value of the requested property.
        """
        pprint.pprint(self)
        return prop

    def getContactInfo(self):
        """Returns a sequence of ContactInfo objects.

        Each of these objects will have a contactType and value property
        representing the contact information, both strings.

        Returns:
            list[ContactInfo]: A sequence of ContactInfo objects.
        """
        pprint.pprint(self)
        ci_email = ContactInfo("email", "johdoe@mycompany.com")
        ci_phone = ContactInfo("phone", "+1 5551324567")
        ci_sms = ContactInfo("sms", "+1 5557654321")
        return [ci_email, ci_phone, ci_sms]

    def getId(self):
        """Returns the internal identifier object that the backing user
        source needs to identify this user.

        Returns:
            str: The internal identifier object that the backing user
                source needs to identify this user.
        """
        pprint.pprint(self)
        return 1

    def getOrDefault(self, prop):
        """Returns a default value if the requested item is not
        present.

        Args:
            prop (Property): The user property to retrieve.

        Returns:
            object: The value of the requested property.
        """
        pprint.pprint([self, prop])

    def getOrElse(self, prop, value):
        """Get the value for a given Property, or else fall back to
        value if it's not present.

        Args:
            prop (Property): The Property for which a value is to be
                retrieved.
            value (object): The value to default to if property isn't
                present.

        Returns:
            object: The value of property if present, value if not.
        """
        pprint.pprint([self, prop])
        return value

    def getRoles(self):
        """Returns a sequence of strings representing the roles that
        this user belongs to.

        Returns:
             list[str]: Sequence of strings representing the roles that
                this user belongs to.
        """
        pprint.pprint(self)
        return User.Roles
