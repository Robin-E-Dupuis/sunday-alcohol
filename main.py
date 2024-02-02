occupied = input("Are you busy :")

if(("yes")) in occupied:
 print("Too bad")

if(("no")) in occupied:
    print("cool that means you can code")


print()
print("this program will tell you if you can or cannot buy alcohol on sunday depending on the state you are in.")
print()

state = input("what state do you live in? :")

if(("louisiana") or ("arkansas")
        or ("kentucky") or ("alabama")  or ("georgia")  or ("south carolina")
              or("florida") or("nebraska") or ("idaho"))in state:

    print("Liquor stores are closed on sundays in certain counties")

elif(("utah") or ("texas") or ("mississippi") or ("north carolina"))in state:
    print("All liquor stores are closed on sundays")

elif(("washington" or "oregon" or "california" or "nevada" or "arizona"
                      or "new mexico" or "colorado" or "wyoming" or "montana" or "north dakota"
                      or "south dakota" or "kansas" or "oklahoma" or "minnesota" or "iowa"
                      or "missouri" or "wisconsin" or "tennessee" or "indiana" or "ohio"
                      or "michigan" or "west virginia" or "virginia" or "maryland" or "delaware"
                      or "new jersey" or "pennsylvania" or "new york" or "rhode island" or "connecticut"
                      or "massachusetts" or "vermont" or "new hampshire" or "maine" or "alaska" ))in state:
    print("You can buy alcohol on sunday")
