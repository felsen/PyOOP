

class Property(object):

    def __init__(self, square_feet="", beds="", baths="", **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_beds = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print(f"Square footage {self.square_feet}")
        print(f"Bedrooms {self.num_beds}")
        print(f"Bathrooms {self.num_baths}")
        print()
 
    @staticmethod
    def prompt_init():
        return {'square_feet': input("Enter a Square Feet? "),
                'beds': input("Enter number of bedrooms? "),
                'baths': input("Enter number of bathrooms? "),
               }


class Apratments(Property):

    valid_laundary = ('coin', 'ensuite', 'none', )
    valid_balcany = ('yes', 'no', 'solarium', )

    def __init__(self, laundary='', balcony='', **kwargs):
        super().__init__(**kwargs)
        self.laundary = laundary
        self.balcony = balcony

    @staticmethod
    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("Laundary {self.laundary}")
        print("Balcony {self.balcony}")
        parent_init = Property.prompt_init()
        laundary, balcany = ''
        while laundary.lower() in Apartments.valid_laundary:
            laundary = input(f"What laundary facilities does the property have? ({', '.join(Apartments.valid_laundary)})")
        while balcany.lower() in Apartments.valid_balcany:
            balcany = input(f"Does the property have balcany? ({', '.join(Apartments.valid_balcany)})")
        parent_init.update({'laundary': laundary, 'balcany': balcany})
        return parent_init

