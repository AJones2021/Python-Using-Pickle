#
# Anna Jones
# 08/12/2023
#  creating a class that take parameters for creating objects
#

class InventoryItem:

    def __init__(self, name='', count=0, cost=0.0, description=''):
        self.name = name
        self.count = count
        self.cost = cost
        self.description = description

    def get_item_input(self):
        self.name = input('Enter the item name: ')
        while True:
            try:
                self.count = int(input('Enter the item count: '))
                if self.count < 0:
                    print('Item count must be 0 or greater.')
                else:
                    break
            except:
                print('Item count must be an integer.')

        while True:
            try:
                self.cost = float(input('Enter the unit cost: '))
                if self.cost < 0.0:
                    print('Unit cost must be 0 or greater.')
                else:
                    break
            except:
                print('Unit cost must be an float.')

        self.description = (input('Enter the description: '))

    def __str__(self):
        return f'{self.name}\n' \
               f'   Count: {self.count}, Cost: {self.cost}\n' \
               f'   {self.description}'