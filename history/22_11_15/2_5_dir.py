# 2.5 dir 


# V1 ------------------------------------------------------

# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return f"Dog : {self.name}"

# hun1 = Dog("hunsman1")

# print("hun1", hun1)

# hun2 = Dog("hunsman2")

# print("hun2", hun2)


"""
    ~/p/Django_airbnb/h/22_11_15    main ?1  python3 2_5_dir.py
hun1 Dog : hunsman1
hun2 Dog : hunsman2

"""

# V1 ------------------------------------------------------


# V2 ------------------------------------------------------

class Dog:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        print(super().__str__())
        return f"Dog: {self.name}"
    def __getattribute__(self, name):
        print(f"they want to get {name}")
        return "getattr def"

hun1 = Dog("hunsman1")

print("hun1", hun1)

hun2 = Dog("hunsman2")

print("hun2", hun2)

"""
    ~/p/Django_airbnb/h/22_11_15    main ?1  python3 2_5_dir.py

hun1 <__main__.Dog object at 0x7f8a3f0d99a0>
Dog: hunsman1
hun2 <__main__.Dog object at 0x7f8a3f03c7f0> 
Dog: hunsman2
"""

# V2 ------------------------------------------------------