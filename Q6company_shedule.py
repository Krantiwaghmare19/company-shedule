company_name=input("enter the company name")
shedule_time=int(input("enter start shedule at time"))
if shedule_time==9:
    print("I am reached in company")
    Todays_Task=input("you are late:yes or no")
    if Todays_Task=="no":
        print("I will start my shedule ")
        per=input("can I do my task: yes or no")
        if per=="yes":
            print("you can do your task")
            print("ask to boss for help")
            per2=input("my task is completed:yes or no")
            if per2=="yes":
                print("you can go to home our task is completed")
            else:
                print("Then you can do tommarow")
        else:
            print("you can go to home")
    else:
        print("boss:you can go")
elif shedule_time!=9:
    print("ask to boss")
    per=input("you can join the shedule:yes or no")
    if per=="yes":
        print("you can do your work")
    else:
        print("you can go home")
else:
    print("you do not go to company")