studs = {} #ts stands for students not actual studs

while True:
    print("╔══════════════════════════════════════════════════════╗")
    print("║              ATTENDANCE MANAGEMENT SYSTEM            ║")
    print("╠══════════════════════════════════════════════════════╣")
    print("║             !! ENTER CHOICE : 1 to 4!!               ║")
    print("║   [1] Add Student                                    ║")
    print("║   [2] Mark Attendance                                ║")
    print("║   [3] Enter Time of Arrival                          ║")
    print("║   [4] View Attendance                                ║")
    print("║   [5] Exit                                           ║")
    print("╚══════════════════════════════════════════════════════╝")
    
    try:
        choice = int(input("> Enter choice: "))  #the choice mentioned in multiple args

        if choice == 1:
            print("╔══════════════════════════════════════════════╗")
            print("║                 ADD STUDENT                  ║")
            print("╚══════════════════════════════════════════════╝")
            name = input("  Student name: > ")

            if name == "":   #stops user from entering a no name idk
                print("╔══════════════════════════════════════════════╗")
                print("║             !NAME CAN'T BE EMPTY!            ║")
                print("╚══════════════════════════════════════════════╝")
            elif name in studs:       #stops user from entering the same name if its already in studs
                print("╔══════════════════════════════╗")
                print("║      STUDENT IS ALREADY      ║")
                print("║             HERE             ║")
                print("╚══════════════════════════════╝")
            else:
                studs[name] = "Not marked"
                print("╔══════════════════════════════════════════════╗")
                print("║                 STUDENT ADDED                ║")
                print("╚══════════════════════════════════════════════╝")
                print("")

                
        elif choice == 2:
            print("╔══════════════════════════════════════════════╗")
            print("║             ENTER STUDENT NAME               ║")
            print("╚══════════════════════════════════════════════╝")
            name = input("  Student name: > ")

            if name in studs:   #checks if student exists
                print("╔══════════════════════════════════════════════╗")
                print("║             PRESENT OR ABSENT?               ║")
                print("╚══════════════════════════════════════════════╝")
                status = input("  Present or Absent: > ").lower()

                if status == "present":     #marks student present if present is typed
                    studs[name] = "Present"
                elif status == "absent":   #same here vruv
                    studs[name] = "Absnet"
                else:
                    print("╔═══════════════════════════════════╗")
                    print("║           INVALID INPUT           ║")
                    print("╚═══════════════════════════════════╝")
            else:
                print("Student not found") #shows when student aint found

        elif choice == 3:
            name = input("  Student Name: > ")

            if name in studs:
                time = input("Enter Time of arrival (H:M): > ")

                try:
                    hour, minute = map(int, time.split(":")) #splits the string after the colon, also map int converts each peace to int
                    total_min = hour * 60 + minute      #then puts it into two var, and this line multiplies the hour to 60

                    if total_min > 420:   #
                        studs[name] = "Late"
                        print("Student is late")
                    else:
                        studs[name] = "Present"

                except ValueError:  
                    print("Invalid format")
            else:
                print("Student not found.")
        
        elif choice == 4:
            if not studs:  #if there's nothing in the studs dict, this code runs
                print("╔════════════════════════════════════════╗")
                print("║          THERE'S NO STUDENTS           ║")
                print("╚════════════════════════════════════════╝")
            else:           
                print("╔═══════════════════════════════════════╗")
                print("║            ATTENDANCE LIST            ║")
                print("╚═══════════════════════════════════════╝")
                for name, status in studs.items(): #but if there is, it prints the name and status if absent/presnet

                    print("      *", name, "-", status)

        elif choice == 5:
            break

    except ValueError:
        print("╔══════════════════════════════╗")
        print("║       !Invalid choice!       ║")
        print("║         !TRY AGAIN!          ║")
        print("╚══════════════════════════════╝")
        continue