#zip demo

state = ["Kranataka","Rajsthan","MP","UP"]
capital = ["Bangalore","Jaipur","Bhopal"]

#use zip to combine two lists
state_capital = zip(state,capital)
for i in state_capital:
    print(i)

