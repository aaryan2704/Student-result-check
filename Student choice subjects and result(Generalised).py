#  WAP to enter student choice (year and semester subjects)---- Generalised for subjects
#  To print the failed subject name

print("Electrical Engineering:\n 1st year\n 2nd year\n 3rd year\n 4th year\n")
year=int(input("enter the student's year\n"))
if year==1:
    print("\nSemesters are: sem 1 and sem 2")
    sem=int(input("enter the semester\n"))
    if sem==1:
        print("\nThe subjects in sem 1 are:\nMaths1, Electronics, engineering drawing")
        a=int(input("enter marks obtained in Maths1\n"))
        b=int(input("enter marks obtined in Electronics\n"))
        c=int(input("enter marks obtained in Engineering drawing\n"))
        total=(a+b+c)
        per=total*100/300
        if per>=75 and a>=40 and b>=40 and c>=40:
            print('you pass with Distinction.\n Total marks obtained= ',total)
        elif per>=60 and a>=40 and b>=40 and c>=40:
            print('you passed with Merit.\n Total marks obtained= ',total)
        elif per>=50 and a>=40 and b>=40 and c>=40:
            print('you passed in pass class.\n Total marks obtained= ',total)
        elif a<40 or b<40 or c<40:
            if a<40 and b>=40 and c>=40:
                print('you failed in Maths 1, please try again.\n Total marks obtained= ',total)
            elif a<40 and b<40 and c>=40:
                print('you failed in Maths 1 and Electronics, please try again.\n Total marks obtained= ',total)
            elif a<40 and b>=40 and c<40:
                print('you failed in Maths 1 and Engineering Drawing, please try again.\n Total marks obtained= ',total)    
            elif a>=40 and b<40 and c>=40:
                print('you failed in Electronics, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b<40 and c<40:
                print('you failed in Electronics and Engineering Drawing, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b>=40 and c<40:
                print('you failed in Engineering Drawing, please try again.\n Total marks obtained= ',total)
            elif a<40 and b<40 and c<40:
                print('you failed in all the subjects, please try again.\n Total marks obtained= ',total)
            else:
                print('invalid imput')
        else:
            print('invalid input')
    elif sem==2:
        print("\nThe subjects in sem 2 are:\nMaths2, Physics, Mechanics")
        a=int(input("enter marks obtained in Maths2\n"))
        b=int(input("enter marks obtined in Physics\n"))
        c=int(input("enter marks obtained in Mechanics\n"))
        total=(a+b+c)
        per=total*100/300
        if per>=75 and a>=40 and b>=40 and c>=40:
            print('you pass with Distinction.\n Total marks obtained= ',total)
        elif per>=60 and a>=40 and b>=40 and c>=40:
            print('you passed with Meri.\n Total marks obtained= ',total)
        elif per>=50 and a>=40 and b>=40 and c>=40:
            print('you passed in pass class.\n Total marks obtained= ',total)
        elif a<40 or b<40 or c<40:
            if a<40 and b>=40 and c>=40:
                print('you failed in Maths 2, please try again.\n Total marks obtained= ',total)
            elif a<40 and b<40 and c>=40:
                print('you failed in Maths 2 and Physics, please try again.\n Total marks obtained= ',total)
            elif a<40 and b>=40 and c<40:
                print('you failed in Maths 2 and Mechanics, please try again.\n Total marks obtained= ',total)    
            elif a>=40 and b<40 and c>=40:
                print('you failed in Physics, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b<40 and c<40:
                print('you failed in Physics and Mechanics, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b>=40 and c<40:
                print('you failed in Mechanics, please try again.\n Total marks obtained= ',total)
            elif a<40 and b<40 and c<40:
                print('you failed in all the subjects, please try again.\n Total marks obtained= ',total)
            else:
                print('invalid imput')
    else:
        print("invalid entry")
elif year==2:
    print("\nSemesters are: sem 3 and sem 4")
    sem=int(input("enter the semester\n"))
    if sem==3:
        print("\nThe subjects in sem 3 are:\nCircuits and networks, DC machines and Transformers, Design engineering")
        a=int(input("enter marks obtained in Circuits and networks\n"))
        b=int(input("enter marks obtined in Electronics\n"))
        c=int(input("enter marks obtained in Engineering drawing\n"))
        total=(a+b+c)
        per=total*100/300
        if per>=75 and a>=40 and b>=40 and c>=40:
            print('you pass with Distinction.\n Total marks obtained= ',total)
        elif per>=60 and a>=40 and b>=40 and c>=40:
            print('you passed with Merit.\n Total marks obtained= ',total)
        elif per>=50 and a>=40 and b>=40 and c>=40:
            print('you passed in pass class.\n Total marks obtained= ',total)
        elif a<40 or b<40 or c<40:
            if a<40 and b>=40 and c>=40:
                print('you failed in Circuits and networks, please try again.\n Total marks obtained= ',total)
            elif a<40 and b<40 and c>=40:
                print('you failed in Circuits and networks and, DC machines and Transformers, please try again.\n Total marks obtained= ',total)
            elif a<40 and b>=40 and c<40:
                print('you failed in Circuits and networks and, Design engineering, please try again.\n Total marks obtained= ',total)    
            elif a>=40 and b<40 and c>=40:
                print('you failed in DC machines and Transformers, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b<40 and c<40:
                print('you failed in DC machines and Transformers and, Design engineering, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b>=40 and c<40:
                print('you failed in Design engineering, please try again.\n Total marks obtained= ',total)
            elif a<40 and b<40 and c<40:
                print('you failed in all the subjects, please try again.\n Total marks obtained= ',total)
            else:
                print('invalid imput')
        else:
            print('invalid input')
    elif sem==4:
        print("\nThe subjects in sem 4 are:\nField Theory, Signal & systems, Digital Electronics-1")
        a=int(input("enter marks obtained in Field Theory\n"))
        b=int(input("enter marks obtined in Signal & systems\n"))
        c=int(input("enter marks obtained in Digital Electronics-1\n"))
        total=(a+b+c)
        per=total*100/300
        if per>=75 and a>=40 and b>=40 and c>=40:
            print('you pass with Distinction.\n Total marks obtained= ',total)
        elif per>=60 and a>=40 and b>=40 and c>=40:
            print('you passed with Merit.\n Total marks obtained= ',total)
        elif per>=50 and a>=40 and b>=40 and c>=40:
            print('you passed in pass class.\n Total marks obtained= ',total)
        elif a<40 or b<40 or c<40:
            if a<40 and b>=40 and c>=40:
                print('you failed in Field Theory, please try again.\n Total marks obtained= ',total)
            elif a<40 and b<40 and c>=40:
                print('you failed in Field Theory and, Signal & systems, please try again.\n Total marks obtained= ',total)
            elif a<40 and b>=40 and c<40:
                print('you failed in Field Theory and, Digital Electronics-1, please try again.\n Total marks obtained= ',total)    
            elif a>=40 and b<40 and c>=40:
                print('you failed in Signal & systems, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b<40 and c<40:
                print('you failed in Signal & systems and, Digital Electronics-1, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b>=40 and c<40:
                print('you failed in Digital Electronics-1, please try again.\n Total marks obtained= ',total)
            elif a<40 and b<40 and c<40:
                print('you failed in all the subjects, please try again.\n Total marks obtained= ',total)
            else:
                print('invalid imput')
        else:
            print('invalid input')
    else:
        print("invalid entry")
elif year==3:
    print("\nSemesters are: sem 5 and sem 6")
    sem=int(input("enter the semester\n"))
    if sem==5:
        print("\nThe subjects in sem 5 are:\nElectrical Power System, Control System, Microprocessor & microcontroller")
        a=int(input("enter marks obtained in Electrical Power System\n"))
        b=int(input("enter marks obtined in Control System\n"))
        c=int(input("enter marks obtained inMicroprocessor & Microcontroller\n"))
        total=(a+b+c)
        per=total*100/300
        if per>=75 and a>=40 and b>=40 and c>=40:
            print('you pass with Distinction.\n Total marks obtained= ',total)
        elif per>=60 and a>=40 and b>=40 and c>=40:
            print('you passed with Merit.\n Total marks obtained= ',total)
        elif per>=50 and a>=40 and b>=40 and c>=40:
            print('you passed in pass class.\n Total marks obtained= ',total)
        elif a<40 or b<40 or c<40:
            if a<40 and b>=40 and c>=40:
                print('you failed in Electrical Power System, please try again.\n Total marks obtained= ',total)
            elif a<40 and b<40 and c>=40:
                print('you failed in Electrical Power System and, Control System, please try again.\n Total marks obtained= ',total)
            elif a<40 and b>=40 and c<40:
                print('you failed in Electrical Power System and, Microprocessor & Microcontroller, please try again.\n Total marks obtained= ',total)    
            elif a>=40 and b<40 and c>=40:
                print('you failed in Control System, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b<40 and c<40:
                print('you failed in Signal & systems and, Microprocessor & Microcontroller, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b>=40 and c<40:
                print('you failed in Microprocessor & microcontroller, please try again.\n Total marks obtained= ',total)
            elif a<40 and b<40 and c<40:
                print('you failed in all the subjects, please try again.\n Total marks obtained= ',total)
            else:
                print('invalid imput')
    elif sem==6:
        print("\nThe subjects in sem 6 are:\nHigh Voltage Engineering, Design engineering 2, Power Electronics 2")
        a=int(input("enter marks obtained in High Voltage Engineering\n"))
        b=int(input("enter marks obtined in Design engineering 2\n"))
        c=int(input("enter marks obtained in Power Electronics 2\n"))
        total=(a+b+c)
        per=total*100/300
        if per>=75 and a>=40 and b>=40 and c>=40:
            print('you pass with Distinction.\n Total marks obtained= ',total)
        elif per>=60 and a>=40 and b>=40 and c>=40:
            print('you passed with Merit.\n Total marks obtained= ',total)
        elif per>=50 and a>=40 and b>=40 and c>=40:
            print('you passed in pass class.\n Total marks obtained= ',total)
        elif a<40 or b<40 or c<40:
            if a<40 and b>=40 and c>=40:
                print('you failed in High Voltage Engineering, please try again.\n Total marks obtained= ',total)
            elif a<40 and b<40 and c>=40:
                print('you failed in High Voltage Engineering and, Design engineering 2, please try again.\n Total marks obtained= ',total)
            elif a<40 and b>=40 and c<40:
                print('you failed in High Voltage Engineering and, Power Electronics 2, please try again.\n Total marks obtained= ',total)    
            elif a>=40 and b<40 and c>=40:
                print('you failed in Design engineering 2, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b<40 and c<40:
                print('you failed in Design engineering 2 and, Power Electronics 2, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b>=40 and c<40:
                print('you failed in Power Electronics 2, please try again.\n Total marks obtained= ',total)
            elif a<40 and b<40 and c<40:
                print('you failed in all the subjects, please try again.\n Total marks obtained= ',total)
            else:
                print('invalid imput')
    else:
        print("invalid entry")
elif year==4:
    print("\nSemesters are: sem 7 and sem 8")
    sem=int(input("enter the semester\n"))
    if sem==7:
        print("\nThe subjects in sem 7 are\nInterconnected Power System, Design of AC Machines, Industrial Instrumentation")
        a=int(input("enter marks obtained in Interconnected Power System\n"))
        b=int(input("enter marks obtined in Design of AC Machines\n"))
        c=int(input("enter marks obtained in Industrial Instrumentation\n"))
        total=(a+b+c)
        per=total*100/300
        if per>=75 and a>=40 and b>=40 and c>=40:
            print('you pass with Distinction.\n Total marks obtained= ',total)
        elif per>=60 and a>=40 and b>=40 and c>=40:
            print('you passed with Merit.\n Total marks obtained= ',total)
        elif per>=50 and a>=40 and b>=40 and c>=40:
            print('you passed in pass class.\n Total marks obtained= ',total)
        elif a<40 or b<40 or c<40:
            if a<40 and b>=40 and c>=40:
                print('you failed in Interconnected Power System, please try again.\n Total marks obtained= ',total)
            elif a<40 and b<40 and c>=40:
                print('you failed in Interconnected Power System and, Design of AC Machines, please try again.\n Total marks obtained= ',total)
            elif a<40 and b>=40 and c<40:
                print('you failed in Interconnected Power System and, Industrial Instrumentation, please try again.\n Total marks obtained= ',total)    
            elif a>=40 and b<40 and c>=40:
                print('you failed in Design of AC Machines, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b<40 and c<40:
                print('you failed in Design of AC Machines and, Industrial Instrumentation, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b>=40 and c<40:
                print('you failed in Industrial Instrumentation, please try again.\n Total marks obtained= ',total)
            elif a<40 and b<40 and c<40:
                print('you failed in all the subjects, please try again.\n Total marks obtained= ',total)
            else:
                print('invalid imput')
    elif sem==8:
        print("\nThe subjects in sem 8 are\nPower system & planning, Power Quality Management, Project-2")
        a=int(input("enter marks obtained in Power system & planning\n"))
        b=int(input("enter marks obtined in Power Quality Management\n"))
        c=int(input("enter marks obtained in Project-2\n"))
        total=(a+b+c)
        per=total*100/300
        if per>=75 and a>=40 and b>=40 and c>=40:
            print('you pass with Distinction.\n Total marks obtained= ',total)
        elif per>=60 and a>=40 and b>=40 and c>=40:
            print('you passed with Merit.\n Total marks obtained= ',total)
        elif per>=50 and a>=40 and b>=40 and c>=40:
            print('you passed in pass class.\n Total marks obtained= ',total)
        elif a<40 or b<40 or c<40:
            if a<40 and b>=40 and c>=40:
                print('you failed in Power system & planning, please try again.\n Total marks obtained= ',total)
            elif a<40 and b<40 and c>=40:
                print('you failed in Power system & planning and, Power Quality Management, please try again.\n Total marks obtained= ',total)
            elif a<40 and b>=40 and c<40:
                print('you failed in Power system & planning and, Project-2, please try again.\n Total marks obtained= ',total)    
            elif a>=40 and b<40 and c>=40:
                print('you failed in Power Quality Management, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b<40 and c<40:
                print('you failed in Power Quality Management and, Project-2, please try again.\n Total marks obtained= ',total)
            elif a>=40 and b>=40 and c<40:
                print('you failed in Project-2, please try again.\n Total marks obtained= ',total)
            elif a & b & c <40:
                print('you failed in all the subjects, please try again.\n Total marks obtained= ',total)
            else:
                print('invalid input')
    else:
        print("invalid entry")
else:
    print("invalid entry")