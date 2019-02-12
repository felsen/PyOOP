"""Using super."""


class Contact(object):

    """Managing contact list."""

    all_contacts = []

    def __init__(self, name='', email='', **keargs):
        """Initiating the contacts with name, and email."""
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class AddressHolder(object):

    """Managing address holder."""

    def __init__(self, street='', city='', state='', code='', **kwargs):
        """Initiating address parameters."""
        super().__init__(*kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):

    """Managing Friends contact details with address."""

    def __init__(self, phone='', **kwargs):
        """Initiating phone number with contact."""
        super().__init__(**kwargs)
        self.phone = phone
