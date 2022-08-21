'''
====================================
-- 111 - OOP – Part 9 Multiple Inheritance &amp; Methods Override 
-- link : https://www.youtube.com/watch?v=OwfiogOFIF4&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs 
====================================
'''
# ---------------------------------------------------------
# -- Object Oriented Programming =&gt; Multiple Inheritance --
# ---------------------------------------------------------

class BaseOne:

  def __init__(self):

    print("Base One")

  def func_one(self):

    print("One")

class BaseTwo:

  def __init__(self):

    print("Base Two")

  def func_two(self):

    print("Two")

class Derived(BaseOne, BaseTwo):

  pass

my_var = Derived()

# print(Derived.mro())

print(my_var.func_one)
print(my_var.func_two)

my_var.func_one()
my_var.func_two()

class Base:

  pass

class DerivedOne(Base):

  pass

class DerivedTwo(DerivedOne):

  pass