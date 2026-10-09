"""
This program creates a table of inventory for Holy Cross merchandise, 
including sweatshirts, t-shirts, sweatpants, and mugs.
It calculates the dollar amount of inventory the merchandise company
has for each item, and alerts the user if they are at 0 for any item,
or if they have gone over the warehouse capacity 
"""

# define fucntions
def dollar_amount_per_category (quantity, price):
    """
    Function finds the total dollar amount of an invetory item.
    Inputs:
        quantity: an integer; the number of items you have in a category of product
        price: a float; the price of one item in a category of product
    Output:
        The total price of all the items in a category of product
    """
    total_price_of_items = quantity * price
    return total_price_of_items

# ask user for quantity and price of each item

if __name__ == '__main__':

    sweatshirts_price = float(input('What is the price of a sweatshirt? '))
    sweatshirts_quantity = int(input('How many sweatshirts do you have? '))

    tshirts_price = float(input('What is the price of a tshirt? '))
    tshirts_quantity = int(input('How many tshirts do you have? '))

    sweatpants_price = float(input('What is the price of one pair of sweatpants? '))
    sweatpants_quantity = int(input('How many paris of sweatpants do you have? '))

    mugs_price = float(input('What is the price of a mug? '))
    mugs_quantity = int(input('How many mugs do you have? '))

    # validate user input by alerting the user if the total quantity is above the warehouse capacity, or if any item is at 0 quantity

    if sweatshirts_quantity + tshirts_quantity + sweatpants_quantity + mugs_quantity > 5000:
        print("Warning! You are over your warehouse's capacity of 5000 total items.")
    
    if sweatshirts_quantity < 0:
        print('Quantity cannot be negative!')
    elif sweatshirts_quantity < 5:
        print('You need to restock sweatshirts!')

    if tshirts_quantity < 0:
        print('Quantity cannot be negative!')
    elif tshirts_quantity < 5:
        print('You need to restock tshirts!')

    if sweatpants_quantity < 0:
        print('Quantity cannot be negative!')
    elif sweatpants_quantity < 5:
        print('You need to restock sweatpants!')

    if mugs_quantity < 0:
        print('Quantity cannot be negative!')
    elif mugs_quantity < 5:
        print('You need to restock mugs!')

    if sweatshirts_price < 0:
        print('Price cannot be negative!')   
    if tshirts_price < 0:
        print('Price cannot be negative!')
    if sweatpants_price < 0:
        print('Price cannot be negative!')  
    if mugs_price < 0:
        print('Price cannot be negative!') 

    # calculate the monetary inventory amount for each item and the total inventory

    total_sweatshirts_dollar_amount = dollar_amount_per_category(sweatshirts_quantity, sweatshirts_price)
    total_tshirts_dollar_amount = dollar_amount_per_category(tshirts_quantity, tshirts_price)
    total_sweatpants_dollar_amount = dollar_amount_per_category(sweatpants_quantity, sweatpants_price)
    total_mugs_dollar_amount = dollar_amount_per_category(mugs_quantity, mugs_price)

    total_assets_inventory = (total_sweatshirts_dollar_amount + total_tshirts_dollar_amount 
                            + total_sweatpants_dollar_amount + total_mugs_dollar_amount)

    # format the output in a table with columns item, price, quanity, and dollar amount of total quantity.

    print('\n')
    print(f'{'Item name':<20}'
        f'{'Price of item ($)':>17}'
        f'{'Quantity':>15}'
        f'{'Total Assets ($)':>20}')
    print('-' * 72)
    print(f'{'Sweatshirts':<20}'
        f'{sweatshirts_price:>17,.2f}'
        f'{sweatshirts_quantity:>15}'
        f'{total_sweatshirts_dollar_amount:>20,.2f}')
    print(f'{'T-Shirts':<20}'
        f'{tshirts_price:>17,.2f}'
        f'{tshirts_quantity:>15}'
        f'{total_tshirts_dollar_amount:>20,.2f}')
    print(f'{'Sweatpants':<20}'
        f'{sweatpants_price:>17,.2f}'
        f'{sweatpants_quantity:>15}'
        f'{total_sweatpants_dollar_amount:>20,.2f}')
    print(f'{'Mugs':<20}'
        f'{mugs_price:>17,.2f}'
        f'{mugs_quantity:>15}'
        f'{total_mugs_dollar_amount:>20,.2f}')
    print('-' * 72)
    print(f'{'Total Inventory ($)':<20}'
            f'{'':>17}'
            f'{'':>15}'
            f'{total_assets_inventory:>20,.2f}')
    print('\n')