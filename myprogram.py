def convertCelciusToFarenheit(celcius):
    if celcius < -273.5:
        return "That temperature does not exist"
    else:
        f = float(celcius) * 9/5 + 32
        return f;

def getStringLength(string):
    if type(string) == int:
        return " It is a string"
    elif type(string) == float:
        return " it is a float"
    else:
        print(string.isalpha())
        return len(string)

temperatures = [10, -20, -289, 100]
file = open("temperature.txt", 'w')

for temperature in temperatures:
    print("Enter temperature in celcius : "+str(temperature))
    if temperature > -273.5:
        file.write(str(convertCelciusToFarenheit(temperature)) +"\n")

file.close()





string = input("Please enter a string: ")
length = getStringLength(string)

print("The length of the string is : "+ str(length))
