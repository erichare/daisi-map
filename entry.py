from pydaisi import Daisi

def test_func():
    with Daisi("Add Two Numbers") as my_daisi:
        dbe = my_daisi.map(func="compute", args_list=[{"firstNumber": 5, "secondNumber": x} for x in range(10)])
        print(dbe.value)

    return("Completed")
    