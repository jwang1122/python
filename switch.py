def switch(argument):
    mydict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return mydict.get(argument,"No such month.")

print(switch(2))
print(switch(13))
print("Done.")
