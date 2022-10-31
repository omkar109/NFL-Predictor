from sportsipy.nfl.teams import Teams
from sportsipy.nfl.boxscore import Boxscores
#above imports libraries needed

nflTeams = Teams() #sets nflTeams as a list of nfl teams
teamStats = {}

#Below creates a dictionary linking team names as they appear in the nflTeams list to team names as they appear in the imported boxscore
teamabrv = {"Tampa Bay Buccaneers":"TAM", "Arizona Cardinals":"CRD", "Los Angeles Rams":"RAM","Dallas Cowboys":"DAL","Buffalo Bills":"BUF","Tennessee Titans":"OTI","Cincinnati Bengals":"CIN","Kansas City Chiefs":"KAN","Baltimore Ravens":"RAV","Las Vegas Raiders":"RAI","New England Patriots":"NWE","Cleveland Browns":"CLE","Indianapolis Colts":"CLT","Green Bay Packers":"GNB","Philadelphia Eagles":"PHI","Seattle Seahawks":"SEA","Los Angeles Chargers":"SDG","Minnesota Vikings":"MIN","Carolina Panthers":"CAR","Washington Commanders":"WAS","New Orleans Saints":"NOR","Denver Broncos":"DEN","New York Giants":"NYG","Atlanta Falcons":"ATL","San Francisco 49ers":"SFO","Detroit Lions":"DET","Miami Dolphins":"MIA","Pittsburgh Steelers":"PIT","Jacksonville Jaguars":"JAX","Chicago Bears":"CHI","Houston Texans":"HTX","New York Jets":"NYG"}

def teamStatGenerator():
  #This function takes each nfl team and puts their point differential, offensive rating and defensive rating into variables which are stored in a dictionary linked to the team
  for team in nflTeams:
    pd = team.points_difference
    ora = team.offensive_simple_rating_system
    dra = team.defensive_simple_rating_system
  #  to = team.turnovers
  #  wp = team.win_percentage
    abrv = str(team)[-11:-8]
    teamStats[abrv] = [pd,ora,dra]

def predictor(week):
  #This function finds a dictionary of games for the user inputted week and iterates through each matchup to find the away and home teams. Then, the point differentials, offensive ratings, and defensive ratings are compared for each team and the team with the better overall stats is selected to win and then the iteration moves onto the next matchup
  sched = str(week) + "-2022"
  i = 0
  games_today = Boxscores(week,2022).games
  while i < len(games_today[sched]): #iterates through each matchup that week
    j = 0
    noAbrvHome = games_today[sched][i]['home_name']
    noAbrvAway = games_today[sched][i]['away_name']
    home_team = teamabrv[games_today[sched][i]['home_name']]
    away_team = teamabrv[games_today[sched][i]['away_name']]
    hPointDiff = teamStats[home_team][0]
    hOffRating = teamStats[home_team][1]
    hDefRating = teamStats[home_team][2]
    aPointDiff = teamStats[away_team][0]
    aOffRating = teamStats[away_team][1]
    aDefRating = teamStats[away_team][2]
    tlist = [hPointDiff,aPointDiff,hOffRating,aOffRating,hDefRating,aDefRating]
    tp = 0
    while j < (len(tlist)-1):
      if tlist[j]>tlist[j+1]:
        tp += 1
      elif tlist[j+1]>tlist[j]:
        tp -= 1
      j += 2
    if tp > 0 or tp == 0:
      print(noAbrvHome, "will win against the",noAbrvAway)
    elif tp < 0:
      print(noAbrvAway, "will win against",noAbrvHome)
    i += 1