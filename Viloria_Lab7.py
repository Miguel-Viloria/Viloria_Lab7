Name= input("Input your name:")
Section= input("Section:")
Prelim= float(input("Prelim Grade:"))
Midterm= float(input("Midterm Grade:"))
Final_Term= float(input("Final Term Grade:"))
Sum_Grade= (Prelim * 0.3333) + (Midterm * 0.3333)+ (Final_Term * 0.3333)
Final_Grade= round(Sum_Grade)
if (40 <= Prelim <= 100) or (40 <= Midterm <=100) or (40 <= Final_Grade <= 100):

  if  Final_Grade >= 99 and Final_Grade <=100:
     print(f" Hi {Name} from class {Section}  your final grade is {Final_Grade} with  GPA : 1.00 ")
  elif  Final_Grade  >=96 and Final_Grade <=98:
     print(f" Hi {Name} from class {Section}  your final grade is {Final_Grade} with GPA: 1.25")
  elif  Final_Grade >=93 and  Final_Grade <=95:
     print(f" Hi {Name} from class {Section} your final grade is {Final_Grade} with GPA: 1.50")
  elif  Final_Grade >=90 and  Final_Grade <=92:
     print(f" Hi {Name} from class {Section} your final grade is {Final_Grade} with GPA: 1.75")
  elif  Final_Grade >=87 and  Final_Grade <=89:
     print(f" Hi {Name} from class {Section} your final grade is {Final_Grade} with GPA: 2.00")
  elif Final_Grade >=84 and  Final_Grade <=86:
     print(f" Hi {Name} from class {Section} your final grade is {Final_Grade} with GPA: 2.25")
  elif Final_Grade >= 81 and  Final_Grade <=83:
     print(f" Hi {Name} from class {Section} your final grade is {Final_Grade} with GPA: 2.50")
  elif Final_Grade >=78 and  Final_Grade <=80:
     print(f" Hi {Name} from class {Section} your final grade is {Final_Grade} withGpa: 2.75")
  elif Final_Grade >=75 and  Final_Grade <=77:
     print(f" Hi {Name} from class {Section} your final grade is {Final_Grade} with GPA: 3.00")
  elif Final_Grade <=74 and  Final_Grade >=41:
     print(f" Hi {Name} from class {Section} your final grade is {Final_Grade} with GPA : 5.00")
else:     
    print("Invalid Grade")
    
    
