import math  
from datetime import date 

today = date.today() 

# mm/dd/yyyy 

currentDate = today.strftime("%m/%d/%Y")


print("Welcome to the Daily UPH tool. Please follow the instructions below.") 

hoursWorked = int(input("Enter the number of hours that you have worked for " + currentDate + ": ")) 

if hoursWorked == 4: 
        hourOne = int(input('Enter the number of items that you have picked in the first hour: ')) 
        hourTwo = int(input('Enter the number of items that you have picked in the second hour: ')) 
        hourThree = int(input('Enter the number of items that you have picked in the third hour: ')) 
        hourFour = int(input('Enter the number of items that you have picked in the fourth hour: ')) 

        #total number of items that were picked. 
        totalItems = hourOne + hourTwo + hourThree + hourFour
        #UPH Calculation: Take the total number number of items and divide it by the number of hours worked. 
        uphCalculation = (totalItems / hoursWorked )

        #Calculations Summary
        print("UPH Calculation Summary")  
        print("Total number of items picked : " + str(totalItems))
        print("Estimated UPH: " + str(uphCalculation)) 


    #Record the date and UPH to text file 

        with open('uphRecs.txt', mode = 'a') as file: 
            file.write(str(currentDate) + ": " + str(uphCalculation)) 
    
else:

    # For Eight Hour Days
    hourOne = int(input('Enter the number of items that you have picked in the first hour: ')) 
    hourTwo = int(input('Enter the number of items that you have picked in the second hour: ')) 
    hourThree = int(input('Enter the number of items that you have picked in the third hour: ')) 
    hourFour = int(input('Enter the number of items that you have picked in the fourth hour: ')) 
    hourFive = int(input('Enter the number of items that you have picked in the fifth hour: ')) 
    hourSix = int(input('Enter the number of items that you have picked in the sixth hour: ')) 
    hourSeven = int(input('Enter the number of items that you have picked in the seventh hour: ')) 
    hourEight = int(input('Enter the number of items that you have picked in the eighth hour: ')) 

    #total number of items that were picked. 
    totalItems = hourOne + hourTwo + hourThree + hourFour + hourFive + hourSix + hourSeven + hourEight
    #UPH Calculation: Take the total number number of items and divide it by the number of hours worked. 
    uphCalculation = (totalItems / hoursWorked )

    #Calculations Summary
    print("UPH Calculation Summary")  
    print("Total number of items picked : " + str(totalItems))
    print("Estimated UPH: " + str(uphCalculation)) 


    #Record the date and UPH to text file 

    with open('uphRecs.txt', mode = 'a') as file:  
        file.write("\n")
        file.write(str(currentDate) + ": " + str(uphCalculation))  
        file.close('uphRecs.txt')

print("UPH has been recorded to text file. Thank you :) ")  


#Four-day average ?

