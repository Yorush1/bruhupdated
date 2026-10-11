studs = {}

while True:    
    print("╔══════════════════════════════════════════════════════╗")
    print("║              ATTENDANCE MANAGEMENT SYSTEM            ║")
    print("╠══════════════════════════════════════════════════════╣")
    print("║             !! ENTER CHOICE : 1 to 5!!               ║")
    print("║   [1] Add Student                                    ║")
    print("║   [2] Mark Attendance                                ║")
    print("║   [3] Enter Time of Arrival                          ║")
    print("║   [4] View Attendance                                ║")
    print("║   [5] Exit                                           ║")
    print("╚══════════════════════════════════════════════════════╝")



    try:
        choice = int(input("> Enter choice: "))

        if choice == 1:
            print("╔══════════════════════════════════════════════╗")
            print("║                 ADD STUDENT                  ║")
            print("╚══════════════════════════════════════════════╝")
            name = input("  Student name: > ")

            if name == "":
                print("╔══════════════════════════════════════════════╗")
                print("║             !NAME CAN'T BE EMPTY!            ║")
                print("╚══════════════════════════════════════════════╝")
            elif name in studs:
                print("╔══════════════════════════════╗")
                print("║      STUDENT IS ALREADY      ║")
                print("║             HERE             ║")
                print("╚══════════════════════════════╝")
            else:
                studs[name] = {
                    "Attendance": "Not Marked",   #just added this function that lets the user see if the student is present and late
                    "Arrival": "Not Recorded"
                }
                print("╔══════════════════════════════════════════════╗")
                print("║                 STUDENT ADDED                ║")
                print("╚══════════════════════════════════════════════╝")
                print("")

                
        elif choice == 2:
            print("╔══════════════════════════════════════════════╗")
            print("║             ENTER STUDENT NAME               ║")
            print("╚══════════════════════════════════════════════╝")
            name = input("  Student name: > ")

            if name in studs:
                print("╔══════════════════════════════════════════════╗")
                print("║             PRESENT OR ABSENT?               ║")
                print("╚══════════════════════════════════════════════╝")
                status = input("  Present or Absent: > ").lower()

                if status == "present":
                    studs[name]["Attendance"] = "Present"
                elif status == "absent":
                    studs[name]["Attendance"] = "Absent"
                else:
                    print("╔═══════════════════════════════════╗")
                    print("║           INVALID INPUT           ║")
                    print("╚═══════════════════════════════════╝")
            else:
                print("Student not found")

        elif choice == 3:
            print("╔══════════════════════════════════════════════╗")
            print("║             ENTER STUDENT NAME               ║")
            print("╚══════════════════════════════════════════════╝")
            name = input("  Student name: > ")

            if name in studs:
                if studs[name]["Attendance"] == "Absent":
                    print("Student is absent. Cannot record arrival time.")

                else:
                    print("╔═══════════════════════════════════╗")
                    print("║       ENTER TIME OF ARRIVAL       ║")
                    print("╚═══════════════════════════════════╝")
                    time = input("Enter Time of arrival (H:M): > ")

                    try:
                        hour, minute = map(int, time.split(":")) 
                        total_min = hour * 60 + minute

                        if total_min > 420:   #
                            studs[name]["Arrival"] = "Late"
                            print("╔═════════════════════════════╗")
                            print("║       STUDENT IS LATE       ║")
                            print("╚═════════════════════════════╝")
                        else:
                            studs[name]["Arrival"] = "On time"

                    except ValueError:  
                        print("╔═══════════════════════════════╗")
                        print("║         INVALID FORMAT        ║")
                        print("╚═══════════════════════════════╝")
            else:
                print("╔═══════════════════════════════╗")
                print("║       STUDENT NOT FOUND       ║")
                print("╚═══════════════════════════════╝")
        
        elif choice == 4:
            if not studs:
                print("╔════════════════════════════════════════╗")
                print("║          THERE'S NO STUDENTS           ║")
                print("╚════════════════════════════════════════╝")
            else:           
                print("╔═══════════════════════════════════════╗")
                print("║            ATTENDANCE LIST            ║")
                print("╚═══════════════════════════════════════╝")
                for name, info in studs.items():

                    print("      *", name, "-", info["Attendance"], "-", info["Arrival"])

        elif choice == 5:
            break

        else:
                print("╔════════════════════════════════════╗")
                print("║          INVALID OPTION            ║")
                print("╚════════════════════════════════════╝")
    except ValueError:
        print("╔══════════════════════════════╗")
        print("║       !Invalid choice!       ║")
        print("║         !TRY AGAIN!          ║")
        print("╚══════════════════════════════╝")
        continue
