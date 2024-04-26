scorecard = [
    {"batter": "Kohli", "dismissal": "c Abdul Samad b Jaydev Unadkat", "runs": 51, "4s": 4, "6s": 1, "strike_rate": 118.60},
    {"batter": "du Plessis (c)", "dismissal": "c Markram b T Natarajan", "runs": 25, "4s": 1, "6s": 0, "strike_rate": 208.33},
    {"batter": "Will Jacks", "dismissal": "b Markande", "runs": 6, "4s": 0, "6s": 0, "strike_rate": 66.67},
    {"batter": "Rajat Patidar", "dismissal": "c Abdul Samad b Jaydev Unadkat", "runs": 50, "4s": 2, "6s": 5, "strike_rate": 250.00},
    {"batter": "Green", "dismissal": "not out", "runs": 37, "4s": 2, "6s": 0, "strike_rate": 185.00},
    {"batter": "Lomror", "dismissal": "c Cummins b Jaydev Unadkat", "runs": 74, "4s": 10, "6s": 1, "strike_rate": 175.00},
    {"batter": "Karthik (wk)", "dismissal": "c Abdul Samad b Cummins", "runs": 11, "4s": 1, "6s": 0, "strike_rate": 183.33},
    {"batter": "Swapnil", "dismissal": 0, "runs": 0, "4s": 0, "6s": 0, "strike_rate": 0}
]

#print(scorecard)

#find all player who not hit any six 

np = filter(lambda x:x["6s"]==1,scorecard)
#print(list(np))

#find all player who have played 30 and more balls and hit 4 and 6 both

fap = filter(lambda x:x["4s"]>0 and x["6s"]>0,scorecard)
print(list(fap))
