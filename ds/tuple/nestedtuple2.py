teamData = [("ms","kohli"),("ram","lakshman"),("sita","gita")]
teamData.append(("laxman","bharat"))
print(teamData)


team1list = list(teamData[1])
team1list[1] = "lakshmi"
print(team1list)

teamData[1] = tuple(team1list)
print(teamData)

