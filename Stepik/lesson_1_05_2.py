'''
Условие
Вам дается последовательность целых чисел и вам нужно ее обработать и вывести 
на экран сумму первой пятерки чисел из этой последовательности, затем сумму 
второй пятерки, и т. д.

Но последовательность не дается вам сразу целиком. С течением времени к вам 
поступают её последовательные части. Например, сначала первые три элемента, 
потом следующие шесть, потом следующие два и т. д.

Реализуйте класс Buffer, который будет накапливать в себе элементы 
последовательности и выводить сумму пятерок последовательных элементов по 
мере их накопления.

Одним из требований к классу является то, что он не должен хранить в себе 
больше элементов, чем ему действительно необходимо, т. е. он не должен 
хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма.
'''
#**************************************************

class Buffer:
	def __init__(self):
	# конструктор без аргументов
		self.arr = []	
		#self.s = 0
	def add(self, *a):
	# добавить следующую часть последовательности
		
		self.arr += a
		
		while len(self.arr)>=5:
			self.sum = 0
			for i in range(5):
				self.sum += self.arr[i]
			self.arr = self.arr[5:]
			print(self.sum)

	def get_current_part(self):
	# вернуть сохраненные в текущий момент элементы последовательности в 

		return self.arr



#Тест
buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]

'''
Пример правильного решения:

Атрибут self.part -- хранит текущее состояние нашего буфера. Внутри метода add 
после добавления каждого элемента, проверяем длину текущего состоянии нашего 
буфера: если длина стала равно 5 -- выводим на экран сумму элементов в буфере 
и не забываем чистить буфер.

class Buffer:
    def __init__(self):
        self.part = []

    def add(self, *a):
        for i in a:
            self.part.append(i)
            if len(self.part) == 5:
                print(sum(self.part))
                self.part.clear()

    def get_current_part(self):
        return self.part
'''