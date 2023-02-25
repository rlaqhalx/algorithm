shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# No need to sort and do binary serach but use "SET", no duplicates allowed data structure
def is_available_to_order(menus, orders):
   menus_set = set(menus) #O(N)
   for order in orders:
       if order not in menus_set:
           return False
   return True

# O(M + N)

result = is_available_to_order(shop_menus, shop_orders)
print(result)