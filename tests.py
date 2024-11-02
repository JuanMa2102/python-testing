def calculate_total(products):
    total = 0
    for product in products:
        total += product['price']
    return total


def test_calculate_total_with_no_products():
    assert calculate_total([]) == 0

def test_calculate_total_with_one_product():
    products = [
        {
            'price': 10
        }
    ]
    assert calculate_total(products) == 10

    
if __name__ == "__main__":
    test_calculate_total_with_no_products()
    test_calculate_total_with_one_product()