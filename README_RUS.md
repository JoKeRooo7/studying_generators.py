
## Изучение генераторов в python


* [`personality.py`](#personalitypy)
* [`pressure.py`](#pressurepy)
* [`energy.py`](#energypy)

Для изучения генераторов, я реализовал решение двух задач, предствленных в разных файлах - `personality,py` и `pressure.py`

Генератор позволяет в процессе работы, выполнять опреденные последовательности действий без необходимости хранения всех значений в памяти.


### `personality.py`

Данный скрипт используется для создании функции-генератора результатов анализа для турели.
Анализ - представлен абстрактно, поэтому веса у характеристик анализа абсолютно рандомны.

Функция, которая анализирует абстрактных персонажей, является `turrets_generator()`. Она возращает класс, названный "Turret", который содержит в себе словар атрибутов `"personality"` `"shoot"` `"search"` `"talk"`. Методами будут являться значение содержащиеся в ключе.

`generate_random()` - генерирует словарь, где ключи - характеристики персонажа, а значения - веса.


### `pressure.py`

Данный скрип используется для решения задач с клапаном, взависимости от поданного в него давления.

Функция `valve()` позволяет автоматизировать клапан, снижая давления или повышая.

Функция-генератор `emit_gel(step)` по умолчанию задает давление 50, и создает цикл генерацийЮ в котором давление будет повышаться или понижатсья, взависимости от шага. При значение давления больше 100 - выкинет ошибку. При давление меньше 10 или больше 90 тоже выкидывает ошибку, которую отлавливает `valve()`.

Функция `valve(gen: emit_gel, step, quantity_iteration=20, print_pressure=True)`, в качестве первого аргумента - принимает функцию-генератор `emit_gel(step)`. Принимает количество итераций , по умолчанию - 20 и флаг для вывода давления в терминал, по умолчанию - True.

В функции `valve()` происходит итерации, до числа установленно в quantity_iteration. Если давление падает меньше 20, он меняет на положительное значение шаги, если увеличивается больше 80, меняет на отрицательное. В случаее повышения давление или понижение - обрывает цикл.

### `energy.py`

Скрипт - для соединения розеток и проводов. Не является генератором. Содержит в себе функцию, где вся логика находиться в return().


