
## Learning about generators in python


* [`personality.py`](#personalitypy)
* [`pressure.py`](#pressurepy)
* [`energy.py`](#energypy)

To study the generators, I implemented the solution of two tasks presented in different files - `personality,py` and `pressure.py `

The generator allows you to perform certain sequences of actions during operation without having to store all the values in memory.


### `personality.py`

This script is used to create an analysis results generator function for the turret.
The analysis is presented abstractly, so the weights of the analysis characteristics are absolutely random.

The function that analyzes abstract characters is `turrets_generator()'. It returns a class called "Turret", which contains a dictionary of attributes `"personality"` `"shoot"` `"search"` `"talk"`. The methods will be the value contained in the key.

`generate_random()` - generates a dictionary where the keys are character characteristics and the values are weights.


### `pressure.py`

This squeak is used to solve problems with the valve, depending on the pressure applied to it.

The `valve()` function allows you to automate the valve by reducing or increasing pressure.

Generator function `emit_gel(step)` by default, it sets the pressure to 50, and creates a generation cycle in which the pressure will rise or fall, depending on the step. If the pressure value is greater than 100, it will throw an error. If the pressure is less than 10 or more than 90, it also throws an error, which is caught by `valve()`.

The function `valve(gen: emit_gel, step, quantity_iteration=20, print_pressure=True)`, takes the generator function `emit_gel(step)` as the first argument. Accepts the number of iterations, by default - 20 and a flag for displaying pressure to the terminal, by default - True.

The `valve()` function iterates up to the number set in quantity_iteration. If the pressure drops below 20, it changes the steps to a positive value, if it increases above 80, it changes to a negative value. In the event of an increase in pressure or decrease, the cycle ends.

### `energy.py`

The script is for connecting sockets and wires. It is not a generator. It contains a function where all the logic is in return().