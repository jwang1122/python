months = ["January",'Febuary','March','April','May','June','July','August','September','October','Novenber',"December"]

with open('months.txt', "w") as myfile:
        for m in months:
                myfile.write("%s\n" % m)

content = open('months.txt')
print(content.read())