studentId ={
      # "101" : "K. M. Arafat Islam",
    # "102" : "Shakib Al Hasan",
    # "103" : "Tamim Iqbal",
    # "104" : "Litton Das",
    
    101 : "K. M. Arafat Islam",
    102 : "Shakib Al Hasan",
    103 : "Tamim Iqbal",
    104 : "Litton Das",
}
  


# print(studentId["104"])
# print(studentId.get("102"))
# print(studentId.get("106"))
# print(studentId.get("106", "not a valid key"))
# print(studentId.get("103", "not a valid key"))

print(studentId.get(102))
print(studentId.get(106))
print(studentId.get(106, "not a valid key"))
print(studentId.get(103, "not a valid key"))

