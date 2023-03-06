def get_pet_shop_name(pet_shop):
    return f'{pet_shop["name"]}'

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash_amount):
    pet_shop["admin"]["total_cash"] += cash_amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] += pets_sold

def increase_pets_sold(shop, amount):
    shop["admin"]["pets_sold"] += amount

def get_stock_count(pet_shop):
    result = 0
    values = pet_shop["pets"]
    for value in values:
        result += 1
    return result

def get_pets_by_breed(pet_shop, pet_name):
    ex = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_name:
            ex.append(pet["breed"])
    return ex

def find_pet_by_name(pet_shop, pet_name):
    for pets in pet_shop["pets"]:
        if pets["name"] == pet_name:
            return pets
        
def remove_pet_by_name(pet_shop, pet_name):
    for pets in pet_shop["pets"]:
        if pets["name"] == pet_name:
            pet_shop["pets"].remove(pets)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customer, cash_amount):
    customer["cash"] -= cash_amount

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False
    

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet is None:
        return None

    if customer_can_afford_pet(customer, pet) == False:
        return None

    pet_price = pet["price"]

    customer["cash"] -= pet_price

    pet_shop["admin"]["total_cash"] += pet_price

    customer["pets"].append(pet)

    pet_shop["admin"]["pets_sold"] += 1 

    # get_customer_pet_count(customer)
    # get_pets_sold(pet_shop)
    # get_customer_cash(customer)
    # get_total_cash(pet_shop)