

class ContactList(list):

    '''Maintaining list of contacts, and inheriting from list datatype.'''

    def search(self, name):
        '''Seaching contacts from list of contacts.'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact(object):

    '''Creating contact objects.'''

    all_contact = ContactList()

    def __init__(self, name, email):
        '''Initiating contact variables.'''
        self.name = name
        self.email = email
        self.all_contact.append(self)


class AddressHolder(object):

    '''specifying the address of the person.'''
   
    def __init__(self, street, city, state, code):
        '''Initializing address variables.'''
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):

    '''Inheriting contact class, adding one or more attribute.'''

    def __init__(self, name, email, phone, street, city, state, code):
        '''Overriding parent class init method.'''
        Contact.__init__(name, email)
        AddressHolder.__init__(street, city, state, code)
        self.phone = phone


class LongNameDict(dict):

    '''Inheriting data from dictionary.'''

    def longest_key(self):
        '''Finding the longest key from the dictionary.'''
        longest = None
        for key in self: # we can use like, for key, value in self.items()
            if (longest is None) or (len(key) > len(longest)):
                longest = key
        return longest


class BaseClass(object):

    '''Base class.'''

    num_base_calls = 0

    def call_me(self):
        '''Method of base class.'''
        print("Base class call me.")
        self.num_base_calls += 1


class LeftBaseClass(BaseClass):

    '''Left base class.'''

    num_left_base_class = 0

    def call_me(self):
        '''Left base class.'''
        BaseClass.call_me(self)
        print("Left base class call me.")
        self.num_left_base_class += 1


class RightBaseClass(BaseClass):

    '''Right base class.'''

    num_right_base_class = 0

    def call_me(self):
        '''Right base class.'''
        BaseClass.call_me(self)
        print("Right base class call me.")
        self.num_right_base_class += 1


class SubClass(LeftBaseClass, RightBaseClass):

    '''Inheriting the left, right base calss into sub class.'''

    num_subclass_calls = 1

    def call_me(self):
        '''Sub class call me.'''
        LeftBaseClass.call_me(self)
        RightBaseClass.call_me(self)
        print("Sub class call me.")
        self.num_subclass_calls += 1

