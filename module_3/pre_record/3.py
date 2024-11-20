def info(**person):
    for key,value in person.items():
        print(f"{key} : {value}")

info(
    name = 'Abdullah Al Mahmud',
    age = 25,
    city = 'Dhaka'
)