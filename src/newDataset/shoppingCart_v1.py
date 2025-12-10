#basic shopping cart
cart = []

def add_item(item):
    cart.append(item)
    print("Added:", item)

def total_items():
   return len(cart)

add_item("Apples")
add_item("Bananas")
add_item("Grapes")

print("Current cart:", cart)
print("Count", total_items())

print("Done shopping.")



