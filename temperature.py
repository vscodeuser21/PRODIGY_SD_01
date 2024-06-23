# Temperature in celsius degree
celsius = float(input())
 
# Converting the temperature to
# fehrenheit using the formula
fahrenheit = (celsius * 1.8) + 32

# Converting the temperature to
# Kelvin using the formula
Kelvin=(celsius +273.15)
 
# printing the result
print('%.2f Celsius is equivalent to: %.2f Fahrenheit'
      % (celsius, fahrenheit))

print('%.2f Celsius is equivalent to: %.2f Kelvin'
      % (celsius, Kelvin))

