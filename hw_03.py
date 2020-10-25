class Storage:
    def __init__(self):
        self.main_storage = []
        self.max_profit = 0
    def add_new(self,company,profit):
        self.main_storage.append([company,profit])
        if profit > self.max_profit:
            self.max_profit = profit
            most_profitable
    def get_most_profitable(self):
        return self.max_profit


a = Storage()
a.add_new("Big Tech", 30000)
a.add_new("Biug Tech", 20000)
a.add_new("Bog Tech", 40000)
a.add_new("Bi Tech", 30000)
print(a.max_profit)