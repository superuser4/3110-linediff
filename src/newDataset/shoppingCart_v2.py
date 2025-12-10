#basic shopping cart
cart = []

def add_item(item):
    if item not in cart:         
        cart.append(item)
        print("Added:", item)

def remove_item(item):            
    if item in cart:
         cart.remove(item)
         print("Removed:", item)

def total_items():
   return len(cart)

add_item("Apples")
add_item("Bananas")
add_item("Apples")
remove_item("Apples")

print("Current cart:", cart)      
print("Count:", total_items())
