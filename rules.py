def calculate_points(receipt):
    total_points = 0
    

def alphanumeric_count(retailer_name):
    total = 0
    for char in retailer_name:
        if (97 <= ord(char) <= 122) or (65 <= ord(char) <= 90):
            total += 1
    return total

def total_round_dollar(total):
    # Convert total to float
    total = float(total)
    roundedTotal = total * 100 // 100
    if roundedTotal != 0 and total % roundedTotal:
        return 0
    return 50

def total_multiple(total):
    pass

def description_multiple(description):
    pass

def odd_purchase_date(purchase_date):
    pass

def purchase_range(start, end, purchase_time):
    pass

