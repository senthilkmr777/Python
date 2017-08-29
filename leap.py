years = int(input("Enter the year: ")) 

if years % 4 == 0 and years %100 != 0 or years % 400 == 0:
    
    print (years,"\nIs a leap year")

else:
    print (years,"\nIs not a leap year")
