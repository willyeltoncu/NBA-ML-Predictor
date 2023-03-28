import pandas as pd



df_teams = pd.read_csv("archive/teams.csv")
df_games = pd.read_csv("archive/games.csv")
print(df_teams.head(5))
print(df_games.head(5))
rename_dict = {'NICKNAME' : "HOME TEAM"}

home_teams_join = df_teams.join(df_games.set_index('HOME_TEAM_ID'), on='TEAM_ID')
away_teams_join = df_teams.join(df_games.set_index('VISITOR_TEAM_ID') , on='TEAM_ID')
print(home_teams_join.head(5))
print(away_teams_join.head(5))
print(teams_games_join.columns)
# teams_games_join = teams_games_join.rename(rename_dict, axis=1)
# print(teams_games_join.columns)
# print(df)