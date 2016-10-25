def someFunction(value, callback)
    result = pow(value, 2)
    callback(result)


def myFunction()
    v = 42
    someFunction(v, myFunction_contiinue())


def myFunction_contiinue(result)
    print result


myFunction()
