# import example_module as em
#
# print(em.my_function.__module__)
#
# print(em.MyClass.__module__)
#
# print(em.MyClass.my_method.__module__)

method_name_list = [1, 2, 3, 3]
a = list(filter(lambda x: method_name_list.count(x) > 1, method_name_list))
print(a)
