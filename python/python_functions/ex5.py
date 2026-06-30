test_dict = {
    "Wireless Mouse": 25,
    "Coffee Mug": 12.5,
    "Leather Jacket": 18,
    "Speaker": 45,
    "Lamp": 32,
    "Shoes": 89,
    "Bottle": 15,
    "Backpack": 49
}


def sale_discount(target_dict):
    for key in target_dict.keys():
        target_dict[key]*=1.1
    return target_dict


print(sale_discount(test_dict))