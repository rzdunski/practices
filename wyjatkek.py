inp = raw_input('Enter Fahrenheit Temperature:')
def fahrenheit_to_celcius(inp):
    try:
        fahrenheit = float(inp)
        celcius = (fahrenheit - 32.0) * 5.0 / 9.0
        print celcius
    except:
        print 'Please enter a number:%s', inp
        fahrenheit_to_celcius(inp)