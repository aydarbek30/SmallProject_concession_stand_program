#Concession Stand Programm


menu = {"popcorn": 2.4,
        "mars": 3.5,
        "cola": 2,
        "snickers": 10.3,
        "sandwich": 5.35}

cart = []
total = 0

for key, value in menu.items():
        print(f"{key}: ${value}")

while True:
        food = input("Enter your food (or press q to quit): ").lower()
        if food == "q":
                break
        elif menu.get(food) is not None:
                cart.append(food)

for food in cart:
        total += menu.get(food)
        print(food)

print(f"Your total is: ${total:.2f}")
