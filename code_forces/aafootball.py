l = int(raw_input())
counter = [0,0]
teamnames = []
for i in range(l):
    names = raw_input()
    if i == 0:
        counter[0] = counter[0] + 1
        teamnames.append(names)
    elif (len(teamnames)==1)and (names != teamnames[0]):
        teamnames.append(names)
        counter[1] = counter[1] + 1
    elif (teamnames[0] == names):
        counter[0] = counter[0] + 1
    elif (teamnames[1] == names):
        counter[1] = counter[1] + 1
if (len(teamnames) == 1):
    print teamnames[0]
elif counter[0] > counter[1]:
    print teamnames[0]
elif counter[1] > counter[0]:
    print teamnames[1]
