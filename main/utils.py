def calculate_insurance(car_price: float, driver_age: int, driving_exp: int, car_type: str) -> float:

    base = car_price * 0.05  

    if driver_age < 25:
        base *= 1.5
    elif driver_age > 60:
        base *= 1.2
    if driving_exp < 3:
        base *= 1.3

    if car_type.lower() == "suv":
        base *= 1.2
    elif car_type.lower() == "sports":
        base *= 1.5

    return round(base, 2)
