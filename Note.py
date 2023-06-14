# # from mcodig

# x = "global x"

# def level_six():
#     z = "outer z"

#     def donkey():
#         def inner(y):
#             return x, y, z
        
#         z = "donkey z"
#         return inner
    
#     def chonky():
#         x = "chonky x"
#         f = donkey()
#         return f("y arg")
#     return chonky()

# print(level_six())


# """
# Key to this rule is  COMPILE TIME OF PYTHON
# PYTHON IS COMILED AND INTERPRETER 

#     The one rule...

#     Variable lookups happen at runtime
#     Locations decided at compile time



# """

# x = "global x"

# def level_one():
#     return x  # simple code where the funtion return x from global scope

# print(level_one())



# def level_two(v):
#     print(v)
#     if v:
#         x = "local x" # here the funtion return local x , but if 
#                       # if the v is False it will give error even there is 
#                       # global scope
#                       # 
#                       # in the compile  compiler doesint take any information
#                       # about the variable v , the compiler notes that some where 
#                       # in the funtion the user assingned the x.
#                       # so the x inide it will take as local variabl.
#                       # if the variable v is False , the comiler take it as it is 
#                       # the local variable x is not assinged

#     return x

# print(level_two(True))
# # print(level_two(False))

# # def level_three():
# #     z = "Outer z"

# #     def inner(y):
# #         return x, y, z

# #     return inner("y arg")

# # print(level_three())

# def level_three():
  

#     def inner(y):
#         return x, y, z
    
#     z = "Outer z" # even if we deffine z after inner funtion 
#                   # it will not  generate any error, it dosen't matter
#                   # where is the z is located , avery inside the variable 
#                   # as a level 3 funtion 
#                   # but, it doesn't look up the value of the variable until
#                   # runtime 
#                   # only the z is defined after the `inner("y arg")` is called
#                   # at that time the Z is defined
#     return inner("y arg")

# print(level_three())


# def level_four():
#     """
 
#     (<cell at 0x00000274760AACE0: str object at 0x00000274762CEF30>,)
#     Python deternuned at compile time that 
#     this cell is where the value of Z is going to be stored
#     the cell has a refernce to a string object which is going to be the first
#     outer Z beacuse we're printing it before we Define second outer Z printing
#     out the clousure again after the second outer z the cell object iteslf hasn't 
#     changed it has same object tje string object that it's referencing has changed
#     this use of a cell instead of the object itself is how python ensures always get
#     the latest value of Z at runtime because the inner funtion only refernces the 
#     cell and not the string object itself this ensures both that when we run the 
#     function we get the latest value of Z and it means that we can define the inner
#     even when the value of Z isn't defined yet .
#     (<cell at 0x00000274760AACE0: str object at 0x00000274762D4DB0>,)

#     if there is no z or defined the the cell reference will be empty.


#     """
#     z = "first outer z"

#     def inner(y):
#         return x, y, z
#     # print(inner.__closure__) # the cell 
#     # print(inner.__globals__)
    
#     z = "second outer z"
#     print(inner.__closure__)

#     return inner("y arg") 

    

# print(level_four())



# def level_five(n):
#     """although funtions are compiled at compile time 
#     meaning their source is translated into bytecode at comile 
#     time actual funtion objeact that get hooked up to that bytecode are
#     created at runtime that's what the def keyword does def does not comile 
#     a new funtion def creates new funtion object with the given name 
#     and hooks it up to the pre-existing bytecode that means every call to level5
#     defines its own copy of the inner funtion each ot these copies is distinct and has its
#     own clouser
#     every call to level 5 has its own cel for its own copy of Z therefore the clouseres
#     for each copy of the inner funtion can refer to completlely different Z's

#     """

#     z = f"outer z {n}"

#     def inner(y):
#         return x, y, z
#     return inner


# def main():
#     f = level_five(0)
#     g = level_five(1)
#     print(f("y arg"), g("other y arg"))

# main()

# def what_about_lambdas_and_comprehensions():
#     """The rules for lambda and generator are same"""
#     # return lambda y:(x, y)

#     # return lambda y: (x, y)

#     l = [x * x for x in range(10)]
#     l = list(x * x for x in range(10))
#     l = list((x * x for x in range(10)))

#     g = (x * x for x in range(10))

#     def gen():
#         for x in range(10):
#             yield x * x


#     g = gen()


# def nonlocal_and_global():
#     x = "nonlocal x"

#     def f():
#         nonlocal x

#         x = "overwritten global"
#         return x 
    
#     print(x)
#     print(f())
#     print(x)
    
# nonlocal_and_global()

# def main():
#     nonlocal_and_global()
#     print(x)

# main()

# x = "global x"

# def level_seven():
#     def please_dont_do_this():
#         if False:

#             a = None

#         def gen_func():
#             nonlocal a
#             for v in range(10):
#                 a =  v
#                 yield v
#         return gen_func(), lambda:a
    
#     gen, fun = please_dont_do_this()
    
#     # print(fun())
#     next(gen())
#     print(fun())
#     next(gen())
#     print(fun())

# level_seven()


