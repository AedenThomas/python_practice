# pickling.py
import pickle
class example_class:
    a_number = 35
    a_string = "hey"
    a_list = [11, 2, 3]
    a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
    a_tuple = (22, 23)
my_object = example_class()

with open("pickled_object", "wb") as file:
    pickle.dump(my_object, file)
    # print the gibberish that is the pickled object
    print(file)

pickled_data = pickle.dumps(my_object)
print(pickled_data)




# my_pickled_object = pickle.dump(my_object) # Pickling the object
# print(f"This is my pickled object:\n{my_pickled_object}\n")


with open("pickled_object", "rb") as file:
    my_object=pickle.load(file)
    print(f"This is a_dict of the unpickled object: \n{my_object.a_dict}\n")

# my_object.a_dict = None
# my_unpickled_object = pickle. load(my_pickled_object) # Unpickling the object
# print(f"This is a_dict of the unpickled object: \n{my_object.a_dict}\n")