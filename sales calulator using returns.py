def calculate_sales(price, quantity, discount):
	total = (price * quantity)
	discount_amount = total * (discount /100)
	final_price = total - discount_amount
	return f"Final price after {discount}% discount is {final_price}"
result = calculate_sales(100,1,10)
print(result)