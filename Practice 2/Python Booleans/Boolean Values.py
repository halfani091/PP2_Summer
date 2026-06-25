#You can evaluate any expression in Python, and get one of two answers, True or False.
is_raining = True
print(is_raining)       # True
print(type(is_raining))  #class

print(bool(0))    # False
print(bool(1))    # True
print(bool(-5))   # True
print(bool(100))  # True

print(bool(""))       # False
print(bool("hello"))  # True
print(bool(None))     # False
print(bool([]))       # False

print(True + True)   # 2
print(True + False)  # 1
print(False + False) # 0
print(True == 1)     # True


is_logged_in = False
has_permission = True
is_admin = False
print(is_logged_in, has_permission, is_admin)
is_logged_in = True
print(is_logged_in)