# Practice 3: Python Functions and Object-Oriented Programming

## Overview
This practice covers Python functions, lambda expressions, and object-oriented
programming (OOP) concepts: classes, objects, and inheritance. Each topic includes
at least four practical, runnable examples with explanatory comments.

## Project Structure
```
Practice-03/
├── functions/
│   ├── basic_functions.py      # function definition & calling basics
│   ├── function_arguments.py   # positional, keyword, and default arguments
│   ├── return_values.py        # single, multiple, conditional, and no return
│   └── args_kwargs.py          # *args, **kwargs, and argument unpacking
├── lambda/
│   ├── lambda_basics.py        # lambda syntax vs regular functions
│   ├── lambda_with_map.py      # transforming data with map()
│   ├── lambda_with_filter.py   # selecting data with filter()
│   └── lambda_with_sorted.py   # custom sort keys with sorted()
├── classes/
│   ├── class_definition.py     # defining classes and creating objects
│   ├── init_method.py          # the __init__() constructor
│   ├── class_methods.py        # instance methods and self
│   └── class_variables.py      # class variables vs instance variables
├── inheritance/
│   ├── inheritance_basics.py   # parent/child class relationships
│   ├── super_function.py       # calling parent methods with super()
│   ├── method_overriding.py    # overriding parent methods
│   └── multiple_inheritance.py # inheriting from multiple parents, MRO
└── README.md                   # this file
```

## How to Run
Each file is self-contained and can be run independently with Python 3:

```bash
python3 functions/basic_functions.py
python3 lambda/lambda_with_map.py
python3 classes/init_method.py
python3 inheritance/super_function.py
```

All 16 example files were tested and run without errors.

## Topics Covered

**Functions:** definition and calling, positional/default/`*args`/`**kwargs`
arguments, return values (single, multiple, conditional, implicit `None`), and
docstrings.

**Lambda expressions:** basic syntax, and practical use with `map()`,
`filter()`, and `sorted()` for transformation, selection, and custom sorting.

**Classes and objects:** class definition, the `__init__()` constructor,
instance methods, and the difference between class variables (shared across
all instances) and instance variables (unique per object).

**Inheritance:** parent/child relationships, `super()` for calling and
extending parent behavior, method overriding, and multiple inheritance
including Method Resolution Order (MRO) and the diamond problem.

## Submission
```bash
git add .
git commit -m "Complete Practice 3: Python functions, lambda, classes, and inheritance examples"
git push origin main
```
