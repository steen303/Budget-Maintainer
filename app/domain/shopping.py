from domain.contact import Contact


class ShoppingListItem:
    def __init__(self, shopping_list_id=None, shopping_item=None, shopping_item_name=None, contact_name=None,
                 price=0.00):
        self.shopping_list_id = shopping_list_id
        if shopping_item_name is None:
            shopping_item_name = 'Algemeen'
        if contact_name is None:
            contact_name = 'Algemeen'
        if shopping_item is None:
            shopping_item = ShoppingItem(shopping_name=shopping_item_name, contact=contact_name, price=price)
        self.shopping_item = shopping_item


class ShoppingItem:
    def __init__(self, shopping_id=None, shopping_name=None, contact=None, price=0.00):
        self.shopping_id = shopping_id
        if shopping_name is None:
            shopping_name = ''
        self.shopping_name = shopping_name
        if contact is None:
            self.contact = Contact('Algemeen')
        elif contact is Contact:
            self.contact = contact
        else:
            self.contact = Contact(contact)
        self.price = price
