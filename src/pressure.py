from random import randrange
from time import sleep


def emit_gel(step):
    pressure: int = 50
    while True:
        new_step = yield pressure
        if new_step is not None:
            step = new_step
        if step < 0:
            pressure += -randrange(0, -step)
        else:
            pressure += randrange(0, step)
        if pressure > 100:
            yield {"error1": pressure}
        if pressure < 10 or pressure > 90:
            yield {"error2": pressure}


def valve(gen: emit_gel, step, quantity_iteration=20, print_pressure=True):
    for i in range(quantity_iteration):
        pressure = next(gen)
        if isinstance(pressure, dict):
            if "error2" in pressure:
                print(f"Emergency stop, pressure = {pressure['error2']}")
                break
            if "error1" in pressure:
                message = "The value limit has been reached pressure"
                print(f"{message} = {pressure['error1']}")
                break
        if pressure < 20 or pressure > 80:
            step = -step
            pressure = gen.send(step)
        if print_pressure:
            print(pressure)
        sleep(1)


if __name__ == "__main__":
    step = 13
    generator = emit_gel(step)
    valve(generator, step)
