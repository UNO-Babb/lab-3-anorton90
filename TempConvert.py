#TempConvert.py
#Name:
#Date:
#Assignment:


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = float(input("Enter temperature in Fahrenheit: "))

  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempC = (5/9) * (tempF - 32)

  #Output converted temperature.
  
  tempC = round(tempC, 2)
  
  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
