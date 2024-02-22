people =[
    {"name":"dinesh","house":"birpur"},
    {"name":"umesh","house":"brt"},
    {"name":"mahesh","house":"rjb"}
]

# def f(person):
#     return person["name"]
# people.sort(key=f)
# print(people)


# above can be written as:
people.sort(key=lambda person: person["name"])
print(people)