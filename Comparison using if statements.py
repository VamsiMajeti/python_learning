x = int(input())
y = int(input())
str1 = str(input())
str2 = str(input())
#for numbers
if x > y:
	print("x is greater than y")
elif x < y:
	print("x is smaller than y")
else: 
	print("x is equal to y")

#for str1 and str2.
if str1 == str2:
	print("str1 is equal to str2")
else: print("str1 is not equal to str2")

if str1 > str2:
	print("str1 is greater than str2")
else: 
	print("str1 is not greater than str2")

if len(str1) == len(str2):
	print("str1 is equal to str2 in length")
else:
	print("str1 is not equal to str2")