class Person:
    arms_count = 2
    legs_count = None
    def __init__(self, name):
        self.name = name

    def great(self):
        print(f'Hi{self.name}!')
    def __str__(self):
        print("hi, my names is ", ", ", self.name)
me = Person('vanya')
you = Person("lesha")

print(me.arms_count, you.arms_count)
me.arms_count  = 1
print(me.arms_count, you.arms_count)
me.legs_count = 2
you.legs_count = 0
print(me.legs_count, you.legs_count)

print(me.name)
me.age = 23
print(me.age)
me.great()
print(me)