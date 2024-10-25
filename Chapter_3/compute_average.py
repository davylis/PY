def compute_avg():
    sum=0.0
    count=0

    num=float(input("Enter first number: "))

    while num !=0:
        sum+=num
        count+=1

        num=(float(input("Enter next number: ")))

    if count == 0:
        print("Nothing to be calculated")

    else:
        avg=sum/count
        print(f"The average is {avg:.2f}")

compute_avg()
