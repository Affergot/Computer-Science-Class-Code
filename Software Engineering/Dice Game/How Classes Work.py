class MyClass1:
    a = 25

    def __init__(self):
        self.a = 100

    def instance_a(self):
        print(self.a)

    def change_instance_a(self):
        self.a = 5

    def class_a(self):
        print(MyClass1.a)

    def change_class_a(self):
        MyClass1.a = 10


# Create two instances
ins1 = MyClass1()
ins2 = MyClass1()

# Both instances have the same Class member a, and the same instance member a
ins1.instance_a()
ins2.instance_a()
ins1.class_a()
ins2.class_a()

# Now lets change instance a on one of our instances
ins1.change_instance_a()

# Print again, see that class a values remain the same, but instance a has
# changed on one instance only
print()
ins1.instance_a()
ins2.instance_a()
ins1.class_a()
ins2.class_a()

# Lets change the class member a on just one instance
ins1.change_class_a()

# Both instances now report that new value for the class member a
print()
ins1.instance_a()
ins2.instance_a()
ins1.class_a()
ins2.class_a()