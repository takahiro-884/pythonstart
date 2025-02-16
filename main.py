# print("Hello, World")

# ex. fizzbuzz => 3倍数 => fizz, 5倍数 => buzz, 15倍数 => fizzbuzz, other => number
# input number , out string? number
# def fizzbuzz (num):
#     if num % 15 == 0:
#         print("fizzbuzz")
#     elif num % 5 == 0:
#         print("buzz")
#     elif num % 3 == 0:
#         print("fizz")
#     else:
#         print(num)

# fizzbuzz(9)
# fizzbuzz(20)
# fizzbuzz(45)
# fizzbuzz(7)

# # 1-100までをfizzbuzzしてほしす
# # for i in range(a, b):
# for i in range(1,101):
#     fizzbuzz(i)

members = [
    {"Name": "松井", "Age": 39, "Gender": "male"},
    {"Name": "今田", "Age": 34, "Gender": "female"},
    {"Name": "鈴木", "Age": 24, "Gender": "male"},
    {"Name": "山田", "Age": 56, "Gender": "male"},
    {"Name": "田中", "Age": 89, "Gender": "female"},
]


for name in members:
    print(name["Name"])

sum = 0
for n in members:
    sum += n["Age"]

print(sum)