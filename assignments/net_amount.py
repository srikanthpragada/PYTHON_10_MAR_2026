# Take qty and price and display net amount
# Discount 20% if qty > 2 otherwise 10%
# Additional discount of 5% if amount > 10000

price = int(input("Enter price :"))
qty = int(input("Enter qty : "))

amount = price * qty
if qty > 2:
    discount = amount * 20 // 100
else:
    discount = amount * 10 // 100

after_discount = amount - discount

additional_discount = 0
if after_discount > 10000:
    additional_discount = after_discount * 5 // 100

net_amount = after_discount - additional_discount

print(f"Gross Amount    :  {amount:6}")
print(f"- Discount      :  {discount:6}")
print(f"After Discount  :  {after_discount:6}")
print(f"- Add. Discount :  {additional_discount:6}")
print(f"Net Amount      :  {net_amount:6}")



