#Создать переменную типа String
a = "Orange"

#Создать переменную типа Integer
b = 2

#Создать переменную типа Float
c = 1.5

#Создать переменную типа Bytes
d = bytes(5)

#Создать переменную типа List
e = [1, 2, 3, ["Mike", 18]]

#Создать переменную типа Tuple
f = ((1, 2), "Hello", "World")

#Создать переменную типа Set
g = {"cherry", "banana", "apple"}

#Создать переменную типа Frozen set
h = frozenset(["Tiger", "Cat"])

#Создать переменную типа Dict
i = {"Russia": "Moscow", "USA": "Washington"}

#Вывести в консоль все выше перечисленные переменные с добавлением типа данных
print(type(a), a, "\n",
      type(b), b, "\n",
      type(c), c, "\n",
      type(d), d, "\n",
      type(e), e, "\n",
      type(f), f, "\n",
      type(g), g, "\n",
      type(h), h, "\n",
      type(i), i)

#Создать 2 переменные String, создать переменную в которой сканкатезируете эти переменные .
#Вывести в консоль
per_1 = "Hello"
per_2 = "World!!!"
per_3 = per_1 + " " + per_2
print(per_3)

#Вывести в одну строку переменные типа String и Integer используя "," (Запятую)
per_4 = "I like HONDA CRV"
per_5 = 3
print(per_4, per_5)

#Вывести в одну строку переменные типа String и Integer используя "+" (Плюс)
print(per_4 + " " + str(per_5))
