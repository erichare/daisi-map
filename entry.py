import time
from pydaisi import Daisi

def test_func():
    with Daisi("Add Two Numbers", instance="dev3") as my_daisi:
        dbe = my_daisi.map(func="subtract", args_list=[{"firstNumber": 5, "secondNumber": x} for x in range(10)])
        dbe.start()
        time.sleep(6)
        print(dbe.value)

    return("Completed")
    
