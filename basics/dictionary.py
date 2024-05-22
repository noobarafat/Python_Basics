# studentId ={
      # "101" : "K. M. Arafat Islam",
    # "102" : "Shakib Al Hasan",
    # "103" : "Tamim Iqbal",
    # "104" : "Litton Das",

#     101 : "K. M. Arafat Islam",
#     102 : "Shakib Al Hasan",
#     103 : "Tamim Iqbal",
#     104 : "Litton Das",
# }
#


# print(studentId["104"])
# print(studentId.get("102"))
# print(studentId.get("106"))
# print(studentId.get("106", "not a valid key"))
# print(studentId.get("103", "not a valid key"))

# print(studentId.get(102))
# print(studentId.get(106))
# print(studentId.get(106, "not a valid key"))
# print(studentId.get(103, "not a valid key"))
#

customer ={
    'Name': "K. M. Arafat Islam",
    "age": 30,
    "is_verified": True
}
customer["Name"] = "Tamim Iqbal"
customer["Birthday"] = "jan 25, 2003"
print(customer.get('Name'))
print(customer.get("Birthday"))

