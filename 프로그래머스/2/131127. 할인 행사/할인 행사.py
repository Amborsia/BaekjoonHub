def solution(want, number, discount):
    dict = {product: quantity for product, quantity in zip(want, number)}
    date = 0

    for i in range(len(discount)-9):
        current = {}
        for day in range(i, i+10):
            product = discount[day]
            if product in current:
                current[product]+=1
            else:
                current[product]=1

        matches = True
        for product, quantity in dict.items():
            if current.get(product,0) <quantity:
                matches = False
                break
        if matches:
            date+=1
    return date