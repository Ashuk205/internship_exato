# info ={'name': 'Karan', 'age':19, 'eligible':True}
# print(info)
# print(info.keys())
# for key in info.keys():
#     print(info[key])

ep1 ={122: 45, 123: 89, 567:69, 670: 69 }
ep2 = {222:67, 566: 90}

# ep1.update(ep2)
# print(ep1)
ep1.popitem()
del ep1[122]
print(ep1)