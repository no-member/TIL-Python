class AdvancedList:
    def __init__(self, list):
        self.list = list
    
    def replace(self, target_number, change_number):
        for n, i in enumerate(self.list):
            if i == target_number:
                self.list[n] = change_number



x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x.list)
