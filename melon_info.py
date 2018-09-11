"""Print out all the melons in our inventory."""


from melons import melons   #melons={name:{seeds, price, flesh, rind, weight}}


def print_melon(melons):
    """Print each melon with corresponding attribute information."""

    for melon, attributes in melons.items():
        print("{}" .format(melon))
        for attribute in attributes:
            print("{}: {}" .format(attribute, attributes[attribute]))


print_melon(melons)
