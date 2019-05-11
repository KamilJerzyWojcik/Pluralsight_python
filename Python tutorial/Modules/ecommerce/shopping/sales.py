from ecommerce.customer import contact
from ..customer import contact

print("Initial sales module", __name__)

contact.contact_customer()


def calc_tax():
    pass

def calc_shipping():
    pass

if __name__ == "__main__":
    print("initial sale with __main__")