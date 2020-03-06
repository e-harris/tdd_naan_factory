# Import naan factory functions
# Define and run tests

from naan_factory_functions import  *


# # As a user, I can use the make_dough with water and flour to make dough.
# print("Calling make_dough with water and flour, expect 'dough' as a result")
# print(make_dough("water", "flour") == "dough")
# print("got:", make_dough("water", "flour"))
#
# print("Calling make_dough with water and cement, expect 'not dough' as a result")
# print(make_dough("water", "cement") == "not dough")
# print("got:", make_dough("water", "cement"))


#2
# As a user, I can use the bake_dough with dough to get naan.

print("Calling bake_dough with dough to get naan, expect 'naan' as a result")
print(bake_dough("dough") == "naan")
print("got: ", bake_dough("dough"))