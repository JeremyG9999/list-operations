class list_sizes:
    def __init__(self):
        self.list1 = [1, 2, 2, 2, 3, 4, 4, 5]
        self.once = []
        self.more_than_one = []
        self.three_time = []
        self.twice = []
        self.four = []
    def only_once(self):
        for list in self.list1:
            if list not in self.once:
                self.once.append(list)
        return self.once
    def more_than_once(self):
        for list in self.list1:
            if self.list1.count(list) > 1:
                self.more_than_one.append(list)
        return self.more_than_one
    def three_times(self):
        for list in self.list1:
            if self.list1.count(list) == 3:
                self.three_time.append(list)
        return self.three_time
    def twices(self):
        for list in self.list1:
            if self.list1.count(list) == 2:
                self.twice.append(list)
        return self.twice
    def four_times(self):
        for list in self.list1:
            if self.list1.count(list) == 4:
                self.four.append(list)
        return self.four
class even_or_odd:
    def __init__(self):
        self.list2 = [1, 1, 2, 2, 2, 2, 3, 4, 4, 5, 5]
        self.even_list = []
        self.odd_list = []
        self.count_even = 0
        self.count_odd = 0
    def even(self):
        for list in self.list2:
            if list % 2 == 0:
                self.even_list.append(list)
        return self.even_list
    def odd(self):
        for list in self.list2:
            if list % 2 == 1:
                self.odd_list.append(list)
        return self.odd_list
    def count_evens(self):
        for list in self.list2:
            if list % 2 == 0:
                self.count_even += 1
        return self.count_even  
    def count_odds(self):
        for list in self.list2:
            if list % 2 == 1:
                self.count_odd += 1
        return self.count_odd
class statistics:
    def __init__(self):
        self.list3 = [1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5] # 14
        self.mean = 0
        self.range = 0
        self.percentage = 0
        self.quads = 0
    def means(self):
        sums = sum(self.list3)
        amount = len(self.list3)
        self.mean = sums / amount
        return round(self.mean, 2)
    def ranges(self):
        self.list3.sort()
        last = self.list3[-1]
        first = self.list3[0]
        self.range = last - first
        return self.range
    def percentages(self, number):
        length = len(self.list3)
        amount = self.list3.count(number)
        self.percentage = amount / length
        return round(self.percentage, 2)
    def sum_of_quads(self):
        for list in self.list3:
            self.quads += list ** 4
        return self.quads
run = list_sizes()
print(f"{run.only_once()}\n{run.more_than_once()}\n{run.three_times()}\n{run.twices()}\n{run.four_times()}\n")
run2 = even_or_odd()
print(f"{run2.even()}\n{run2.odd()}\n{run2.count_evens()}\n{run2.count_odds()}\n")
run3 = statistics()
print(f"{run3.means()}\n{run3.ranges()}\n{run3.percentages(3)}\n{run3.sum_of_quads()}")
