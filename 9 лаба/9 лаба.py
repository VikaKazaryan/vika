def task1():
    class Restaurant:

        def __init__(self, name, cuisine_type):
            self.name = name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"{self.name} serves {self.cuisine_type} cuisine.")

        def open_restaurant(self):
            print(f"{self.name} is now open.")

    class IceCreamStand(Restaurant):

        def __init__(self, name, flavors):
            super().__init__(name, "ice cream")
            self.flavors = flavors

        def list_flavors(self):
            print("Flavors:")
            for flavor in self.flavors:
                print(f"- {flavor}")

    ice_cream_stand = IceCreamStand("Sweet Tooth", ["chocolate", "vanilla", "strawberry"])
    ice_cream_stand.list_flavors()


task1()


def task2():
    class Restaurant:

        def __init__(self, name, cuisine_type):
            self.name = name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"{self.name} serves {self.cuisine_type} cuisine.")

        def open_restaurant(self):
            print(f"{self.name} is now open.")

    class IceCreamStand(Restaurant):

        def __init__(self, name, flavors, location, hours):
            super().__init__(name, "ice cream")
            self.flavors = flavors
            self.location = location
            self.hours = hours

        def list_flavors(self):
            print("Flavors:")
            for flavor in self.flavors:
                print(f"- {flavor}")

        def add_flavor(self, flavor):
            self.flavors.append(flavor)

        def remove_flavor(self, flavor):
            self.flavors.remove(flavor)

        def has_flavor(self, flavor):
            return flavor in self.flavors

        def get_location(self):
            return self.location

        def get_hours(self):
            return self.hours

    ice_cream_stand = IceCreamStand("Sweet Tooth", ["chocolate", "vanilla", "strawberry"], "123 Main Street",
                                    "10am-10pm")

    ice_cream_stand.add_flavor("cookie")

    ice_cream_stand.remove_flavor("strawberry")

    print(ice_cream_stand.has_flavor("cookie"))

    print(ice_cream_stand.get_location())

    print(ice_cream_stand.get_hours())


task2()


def task3():
    import tkinter as tk

    class IceCreamStand:

        def __init__(self, name, flavors):
            self.name = name
            self.flavors = flavors

        def create_gui(self):
            self.window = tk.Tk()
            self.window.title(self.name)

            self.flavors_frame = tk.Frame(self.window)
            self.flavors_frame.pack()

            self.flavors_label = tk.Label(self.flavors_frame, text="Flavors:")
            self.flavors_label.pack()
            self.flavors_listbox = tk.Listbox(self.flavors_frame)
            self.flavors_listbox.pack()

            for flavor in self.flavors:
                self.flavors_listbox.insert(tk.END, flavor)

            self.close_button = tk.Button(self.window, text="Close", command=self.window.destroy)
            self.close_button.pack()

            self.window.mainloop()

    ice_cream_stand = IceCreamStand("Sweet Tooth", ["chocolate", "vanilla", "strawberry"])
    ice_cream_stand.create_gui()


task3()