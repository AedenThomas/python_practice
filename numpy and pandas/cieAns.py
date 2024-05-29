# import pickle

# class example_class:
#     def __init__(self, a_num, a_string, a_dict, a_list, a_tuple):
#         self.a_num= a_num
#         self.a_string= a_string
#         self.a_dict= a_dict
#         self.a_list= a_list
#         self.a_tuple= a_tuple

# example_classObj = example_class(1, 'a string', {'a':1, 'b':2}, [1,2,3], (1,2,3))


# with open('example_class.pickle', 'wb') as f:
#     pickle.dump(example_classObj, f)

# with open('example_class.pickle', 'rb') as f:
#     example_classObj = pickle.load(f)

# pickle.load(open('example_class.pickle', 'rb'))

# print(example_classObj.a_num)
# print(example_classObj.a_string) 


radius=int(input("Enter the radius: "))
if radius < 3:
    print("Error: Radius must be greater than 3")
    exit()

diameter=radius*2
area=3.14*radius*radius
circumference=2*3.14*radius

print("Radius: ", radius)
print("Diameter: ", diameter)
print("Circumference: ", circumference)
