# Mbarara > 4000000
# kampala , 10000000 and above >= 100000000
# any other >= 6000000
# space >= 0
# enter location, pay

job_loc = input("Enter location:")

job_pay = input("Enter amount paid:")

# we use the if statement and the len() function to check whether the user entered something

if len(job_loc) > 0 and len(job_pay) > 0:

    try:

        final_wage = int(job_pay)

        if job_loc.capitalize() == "Mbarara" and final_wage > 4000000:
            print("Without doubt i will take it!")
        else:
            if job_loc.capitalize() == "Mbarara" and final_wage <= 4000000:
                print("no thanks i will find something  better")
            else:
                if job_loc.capitalize() == "Kamapala" and final_wage >= 10000000:
                    print("Without doubt i will take it")
                else:
                    if job_loc.capitalize() == "Kampala" and final_wage < 10000000:
                        print("No way!")
                    else:
                        if (job_loc.capitalize() != "Mbarara" and job_loc.capitalize() != "Kampala" and job_loc.capitalize() != "Space") and final_wage >= 6000000:
                            print("Sure i can work with this!")
                        else:
                            if (job_loc.capitalize() != "Mbarara" and job_loc.capitalize() != "Kampala" and job_loc.capitalize() != "Space") and final_wage < 6000000:
                                print("No thanks i can find something better")
                            else:
                                if job_loc.capitalize() == "Space" and final_wage >= 0:
                                    print("without doubt i will take it!")




    except:
        print("Error, hey enter the required numeric input for the wage!")

else:
    print("Hey enter something!")