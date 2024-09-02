def luhns_algorithm(card_no):
    card = [int(no) for no in str(card_no)] 
    card.reverse()

    digits = []
    number = []
    
    for i, d in enumerate(card):
        if i % 2 == 0:
            digits.append(d * 2)
        else:
            digits.append(d)
            
    for digit in digits:
        if digit > 9:
            number.append(digit - 9)
        else:
            number.append(digit)
    total = sum(number)

    is_valid = (total % 10) == 0
    return is_valid

result = luhns_algorithm("23627398")
print(result)