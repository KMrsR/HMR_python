'''
Условие
Каждая копилка имеет ограниченную вместимость, которая выражается целым 
числом – количеством монет, которые можно положить в копилку. Класс должен 
поддерживать информацию о количестве монет в копилке, предоставлять 
возможность добавлять монеты в копилку и узнавать, можно ли добавить в 
копилку ещё какое-то количество монет, не превышая ее вместимость.
'''
#**************************************************

class MoneyBox:
	def __init__(self, capacity, cur=0):
	# конструктор с аргументом – вместимость копилки
		self.capacity = capacity
		self.cur = cur
	def can_add(self, v):
	# True, если можно добавить v монет, False иначе
		if self.capacity >= self.cur + v:
			return True
		else:
			return False
	def add(self, v):
	# положить v монет в копилку
		self.cur += v

#Тест
vb = 0		
x = MoneyBox(15,vb)
x.add(5)
x.add(9)
x.add(3)

'''
class MoneyBox:
    def __init__(self, capacity):
        self.count_coin = 0
        self.capacity = capacity

    def can_add(self, v):
        return self.count_coin + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.count_coin += v
'''