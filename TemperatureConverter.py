#Temperature Converter
#By Kaiser_Bray
#2/21/2022
def tempConvert():
    #Checks for temperature type
    farcel = input("Fahrenheit or Celcius (f/c):")
    if farcel == "f":
        tempNumber = int(input("Enter the Temperature:"))
        #(X°F - 32) x .5556 Fahrenheit to Celcius formula
        newTemp = (tempNumber - 32) * .5556
        print(str(newTemp) + "°C")
    elif farcel == "c":
        tempNumber = int(input("Enter the Temperature:"))
        #(X°C x 1.8) + 32 Celcius to Fahrenheit formula
        newTemp = (tempNumber * 1.8) + 32
        print(str(newTemp) + "°F")
    else:
        print("Please enter a valid temperature type:")
        tempConvert()


tempConvert()



