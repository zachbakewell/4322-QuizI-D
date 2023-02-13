'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile = open('employee_data.csv', 'r', newline='')

reader = csv.reader(infile, delimiter=',')



#create an empty dictionary
emp_sal = {}

#use a loop to iterate through the csv file
for row in reader:
    #check if the employee fits the search criteria
    if row[3] == 'Marketing':
        if row[4] == 'CSR':
            first = row[1]
            last = row[2]
            name = first + ' ' + last
            #print(name)
            salary = row[5]
            #print(salary)
            emp_sal[name]= float(salary)
        
print()

#print the dictionary with original salaries before the salary increase
for key,value in emp_sal.items():
    print(f'Manager Name: {key} Current Salary: ${value:,.2f}')

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout

#iterate through and multiply by 1.1 to get a 10 percent increase to each salary
for key,value in emp_sal.items():
    value *= 1.1
    print(f'Manager Name: {key} Current Salary: ${value:,.2f}')


          
        

        
    
