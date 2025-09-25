students = []

while True:
    print("\nMeny:")
    print("1. Lägg till student")
    print("2. Lista alla studenter")
    print("3. Avsluta")
    choice = input("Välj ett alternativ (1-3): ")

    if choice == "1":
        namn = input("Ange studentens namn: ")
        ålder = input("Ange studentens ålder: ")
        student = {"namn": namn, "ålder": ålder}
        students.append(student)
        print(f"Studenten {namn} har lagts till.")
    elif choice == "2":
        print("\nLista över studenter:")
        for i, student in enumerate(students, 1):
            print(f"{i}. Namn: {student['namn']}, Ålder: {student['ålder']}")
        if not students:
            print("Inga studenter tillagda.")
    elif choice == "3":
        print("Avslutar programmet.")
        break
    else:
        print("Ogiltigt val, försök igen.")
