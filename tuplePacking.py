# #packing and unpacking
# tuple1 = (1,2,3)
# (one, two, three) = tuple1
# print(one) 
# print(two)
# print(three) 


tuple1 = ("car", "bike", "boat", "cycle")
(*item1, item2, item3) = tuple1

print(item1)
print(item2)
print(item3)