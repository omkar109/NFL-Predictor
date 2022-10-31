import functions #imports other file full of functions
functions.teamStatGenerator() 
while True: #Makes it so it always asks
  nflweek = int(input("What NFl week do you want predictions for? ")) #Lets you enter an input a week for predictions
  functions.predictor(nflweek)
  print(" ") #Leaves an empty line between each week

#Link to info:
#https://sportsreference.readthedocs.io/en/stable/nfl.html#sportsipy.nfl.teams.Team.points_against
