def tax():
    
    socialSecurityTax = 0
    federalIncomeTax = 0
    grossPay = 0
        ## we do not need to declare these variable yet.

    
    employeeName = input("Give the name of the employee:")
    hourlyRate = float(input("Give the hour rate:"))
    hoursWorked = float(input("Give the number of hours worked:"))

    if hoursWorked > 40:
        hoursWorked = hoursWorked + ((hoursWorked-40) * 1.5)

        # we need to make every additional hour after 40 hours be treated as overtime hours, which is equivalent to 1.5 hours.
        # this declaration says we will take the number of hours worked after 40, and multiply them by 1.5
        
    else:
        hoursWorked = hoursWorked
		##this is redundant. of course i = i. you don't need to state this. 

    grossPay = int(hoursWorked * hourlyRate)
    
    ##taxTotal = int(socialSecurityTax + federalIncomeTax)    
    ##netIncome = int(grossPay - taxTotal)
            ## we need to move this variable down to when we actually calculate socialSecurityTax.


    if grossPay < 2000:
        socialSecurityTax = grossPay * .062
    else:
        socialSecurityTax = 124
    # here I changed the <= to <. This is because we can simplify our if/else statement to check only if it is less, and if not then set equal to 124.

    


    if grossPay < 500:
        federalIncomeTax = grossPay * .15
    elif grossPay > 1000:
        federalIncomeTax = grossPay * .25 + 175
    else:
        federalIncomeTax = grossPay * .20 + 75

        ## there is a logic issue here with the homework parameters itself.
        ##
        ##  a discrete logic would be:
        ##      if a < 500
        ##      elif 500 <= a < 1000
        ##      else
        ##
        ##      this logic is poorly specified in the assignment.
        ##      e.g., what does the table in the assignment say about if we have a gross income of exactly 500?
        ##
        ##      the above logic gives a clearer direction and is better defined.
        ##      also, rather than going from small to big to medium, lets go from small to medium to big. 
        ##      this may be more costly at runtime, but we need to write programs so that other people can easily read them, and that starts with clear logic.
        
        
        

    ##taxTotal = int(socialSecurityTax + federalIncomeTax)    
    ##netIncome = int(grossPay - taxTotal)
        # even better, let us simplify netIncome

    netIncome = int(grossPay - (socialSecurityTax + federalIncomeTax))

    print(employeeName, " had a gross pay of $", grossPay, ".",sep = "")
    print("Social Security tax deduction is $", socialSecurityTax, ".",sep="")
    print("Federal tax deduction is $", federalIncomeTax, ".",sep="")
    print("Net pay is $", netIncome, ".",sep="")

    # note for this, we are returning a float for both socialSecurityTax and federalIncomeTax. let's only cast it as an int once. this will be done below.



    
# lets take all of this and remove the comments now, to give us a clear view of our logic.

def main():
    employeeName = input("Give the name of the employee:")
    hourlyRate = float(input("Give the hour rate:"))
    hoursWorked = float(input("Give the number of hours worked:"))

    if hoursWorked > 40:
        hoursWorked = hoursWorked + ((hoursWorked-40) * 1.5)

    grossPay = int(round(hoursWorked * hourlyRate))
    
    if grossPay < 2000:
        socialSecurityTax = grossPay * .062
    else:
        socialSecurityTax = 124

    if grossPay < 500:
        federalIncomeTax = grossPay * .15
    elif 500 <= grossPay < 1000:
        federalIncomeTax = grossPay * .20 + 75
    else:
        federalIncomeTax = grossPay * .25 + 175

    netIncome = int(round(grossPay - (socialSecurityTax + federalIncomeTax)))

    print(employeeName, " had a gross pay of $", grossPay, ".",sep = "")
    print("Social Security tax deduction is $", int(round(socialSecurityTax)), ".",sep="")
    print("Federal tax deduction is $", int(round(federalIncomeTax)), ".",sep="")
    print("Net pay is $", netIncome, ".",sep="")

main()
