def grades():
    grades=["A", "A", "B", "A", "C", "B", "C", "F", "B", "B", "A", "A", "C", "C", "C"]
    total = len(grades)
    
    grade=input("Enter grade letter: ")
    
    count=grades.count(grade)
    percentage=(count/total)*100

    print(f"{percentage:.1f}")

grades()