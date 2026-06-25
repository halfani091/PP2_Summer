#and 
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

#or
print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False) # False

print(not True)   # False
print(not False)  # True
door_open = False
print(not door_open)  # True — дверь закрыта?


age = 25
has_license = True
is_sober = True
can_drive = age >= 18 and has_license and is_sober
print(can_drive)  # True

print(True or False and False)    # True (сначала and)
print((True or False) and False)  # False (сначала or)