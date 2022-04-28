class Animal:
    this_list = ["Kane", "Kabob", "Gully"]

    def add_name(self, name):
        self.this_list.append(name)
        return self.this_list

    @property
    def get_gully(self):
        return self.this_list[2]


a = Animal()

print(a.get_gully)

print(a.add_name("Chat"))

