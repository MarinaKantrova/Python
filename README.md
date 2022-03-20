==============  
### Python HW_1
==============  

#Создать переменную типа String  
**`a = "Orange"`**

#Создать переменную типа Integer  
**`b = 2`**

#Создать переменную типа Float  
**`c = 1.5`**

#Создать переменную типа Bytes  
**`d = bytes(5)`**

#Создать переменную типа List  
**`e = [1, 2, 3, ["Mike", 18]]`**

#Создать переменную типа Tuple  
**`f = ((1, 2), "Hello", "World")`**

#Создать переменную типа Set  
**`g = {"cherry", "banana", "apple"}`**

#Создать переменную типа Frozen set  
**`h = frozenset(["Tiger", "Cat"])`**

#Создать переменную типа Dict  
**`i = {"Russia": "Moscow", "USA": "Washington"}`**

#Вывести в консоль все выше перечисленные переменные с добавлением типа данных  
**`print(type(a), a, "\n",`**  
      **`type(b), b, "\n",`**  
      **`type(c), c, "\n",`**  
      **`type(d), d, "\n",`**  
      **`type(e), e, "\n",`**  
      **`type(f), f, "\n",`**  
      **`type(g), g, "\n",`**  
      **`type(h), h, "\n",`**  
      **`type(i), i)`**  

#Создать 2 переменные String, создать переменную в которой сканкатезируете эти переменные  
#Вывести в консоль  
**`per_1 = "Hello"`**  
**`per_2 = "World!!!"`**  
**`per_3 = per_1 + " " + per_2`**  
**`print(per_3)`**  

#Вывести в одну строку переменные типа String и Integer используя "," (Запятую)  
**`per_4 = "I like HONDA CRV"`**  
**`per_5 = 3`**  
**`print(per_4, per_5)`**  

#Вывести в одну строку переменные типа String и Integer используя "+" (Плюс)  
**`print(per_4 + " " + str(per_5))`**  


==============  
### Python HW_2
==============  
import math

#Создать переменную item_1 типа integer.  
**`item_1 = 9`**  

#Создать переменную item_2 типа integer.  
**`item_2 = 3`**  

#Создать переменную result_sum в которой вы суммируете item_1 и item_2.  
**`result_sum = item_1 + item_2`**  

#Вывести result_sum в консоль.  
**`print("result_sum = ", result_sum)`**  

#Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.  
**`result_subtr = item_1 - item_2`**  

#Вывести result_subtr в консоль.  
**`print("result_subtr = ", result_subtr)`**  

#Создать переменную result_multi в которой вы умножаете item_1 на item_2.  
**`resul_multi = item_1 * item_2`**  

#Вывести result_multi в консоль.  
**`print("result_multi = ", resul_multi)`**  

#Создать переменную result_exp в которой вы item_1 возводите в степень item_2.  
**`result_exp = item_1 ** item_2`**  

#Вывести result_exp в консоль.  
**`print("result_exp = ", result_exp)`**  

#Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.  
**`result_m_exp = math.pow(item_1, item_2)`**  

#Вывести result_m_exp в консоль.  
**`print("result_m_exp = ", result_m_exp)`** 

#Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item.  
**`result_s_root = item_1 ** 0.5`** 

#Вывести result_s_root в консоль.  
**`print("result_s_root = ", result_s_root)`** 

#Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math.  
**`result_m_s_root = math.sqrt(item_1)`** 

#Вывести result_m_s_root в консоль.  
**`print("result_m_s_root = ", result_m_s_root)`** 

#Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.  
**`result_mp_s_root = math.pow(item_1, 0.5)`** 

#Вывести result_mp_s_root в консоль.  
**`print("result_mp_s_root = ", result_mp_s_root)`** 

#Присвоить переменной item_1 odd значение.  
**`item_1 = 11`** 
**`if item_1 % 2 != 0:`** 
    **`print("item_1 = Переменная -odd", item_1)`** 
**`else:`** 
    **`print("item_1 = Переменная -even", item_1)`** 

#Присвоить переменной item_2 even значение.  
**`item_2 = 4`** 
**`if item_2 % 2 == 0:`** 
    **`print("item_2 = Переменная -even", item_2)`** 
**`else:`** 
    **`print("item_2 = Переменная -odd", item_2)`** 

#Создать переменную result_division в которой вы разделите item_1 на item_2.  
**`result_division = item_1 / item_2`** 

#Вывести result_division в консоль.  
**`print("result_division = ", result_division)`** 

#Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.  
**`result_m_floor = math.floor(result_division)`** 

#Вывести result_m_floor в консоль.  
**`print("result_m_floor = ", result_m_floor)`** 

#Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.  
**`result_m_ceil = math.ceil(result_division)`** 

#Вывести result_m_ceil в консоль.  
**`print("result_m_ceil = ", result_m_ceil)`** 

#Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.  
**`result_int = round(result_division)`** 

#Вывести result_int в консоль.  
**`print("result_int = ", result_int)`**

#Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.  
**`result_no_division_loss = item_1 // item_2`**

#Вывести result_no_division_loss в консоль.  
**`print("result_no_division_loss = ", result_no_division_loss)`**

#Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.  
**`result_division_loss = item_1 % item_2`**

#Вывести result_division_loss в консоль.  
**`print("result_division_loss = ", result_division_loss)`**

#Дальше будет реализация через арифметические действия с присваиванием.  

#Создать переменную item_3 и присвоить ей целое число.  
**`item_3 = 8`**

#Прибавить 10 к item_3 с присвоением.  
**`item_3 += 10`**

#Вывести item_3 в консоль.  
**`print("item_3 = ", item_3)`**

#Отнять 5 от item_3 с присвоением.  
**`item_3 -= 5`**

#Вывести item_3 в консоль.  
**`print("item_3 = ", item_3)`**

#Умножить item_3 на 3 с присвоением.  
**`item_3 *= 3`**

#Вывести item_3 в консоль.  
**`print("item_3 = ", item_3)`**

#Разделить item_3 на 2 с присвоением.  
**`item_3 /= 2`**

#Вывести item_3 в консоль.  
**`print("item_3 = ", item_3)`**

#Возвести в степень 2 item_3 с присвоением.  
**`item_3 **= 2`**

#Вывести item_3 в консоль.  
**`print("item_3 = ", item_3)`**

#Найти квадратный корень item_3 с присвоением.  
**`item_3 **= 0.5`**

#Вывести item_3 в консоль.  
**`print("item_3 = ", item_3)`**

#Присвоить остаток от деления item_3  
**`item_3 %= 2`**

#Вывести item_3 в консоль.  
**`print("item_3 = ", item_3)`**

#Boolean

#Создать переменную b_item_t и присвоить True  
**`b_item_t = True`**

#Создать переменную b_item_f и присвоить False  
**`b_item_f = False`**

#Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f  
**`b_item_result_sum = (b_item_t + b_item_f)`**

#Вывести b_item_relult_sum в консоль.  
**`print("b_item_result_sum = ", b_item_result_sum)`**

#Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f  
**`b_item_relult_subtr = (b_item_t - b_item_f)`**

#Вывести b_item_relult_subtr в консоль.  
**`print("b_item_relult_subtr = ", b_item_relult_subtr)`**

#Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f  
**`b_item_relult_multi = b_item_t * b_item_f`**

#Вывести b_item_relult_multi в консоль.  
**`print("b_item_relult_multi = ", b_item_relult_multi)`**

#Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f  
#b_item_relult_division = b_item_t / b_item_f

#Вывести b_item_relult_division в консоль. (Получить ошибку)  
#print("b_item_relult_division = ", b_item_relult_division)

#Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int  
**`b_item_1_int = int(b_item_t)`**

#Вывести b_item_1_int в консоль.  
**`print("b_item_1_int = ",b_item_1_int)`**

#Создать переменную b_item_2_int и присвоить явное приведение b_item_2 к int  
**`b_item_2_int = int(b_item_f)`**

#Вывести b_item_2_int в консоль.  
**`print("b_item_2_int = ", b_item_2_int)`**
