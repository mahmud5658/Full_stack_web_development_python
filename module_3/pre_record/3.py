# def info(**person):
#     for key,value in person.items():
#         print(f"{key} : {value}")

# info(
#     name = 'Abdullah Al Mahmud',
#     age = 25,
#     city = 'Dhaka'
# )

set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.intersection(set2)
print(result)
