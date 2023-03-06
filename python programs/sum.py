
sum=0;
print("do you want to continue ,enter yes or no ?");
choice = input("Enter the choice: ");
while (choice == "no" ):
    choice="yes"
    while(choice == "yes"):
        n=int(input("Enter the number: "))
        if(n%4==0):
            sum=sum+n;
            if(n/4==0):
                print("final sum is :",sum)

