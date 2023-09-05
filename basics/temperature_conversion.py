conversion_type = input("Fahrenheit to celcius(f_c) or celcius to fahrenheit(c_f) ")
temp = int(input("What temperture "))
fahrenheit = 0
celcius = 0
def f_c(temp):
    celcius = (temp - 32) * 5/9     
    print(celcius)
def c_f(temp):
    fahrenheit  = (temp * 9/5) + 32
    print(fahrenheit)
if conversion_type == "f_c":
    f_c(temp)
else:
    c_f(temp)
    
