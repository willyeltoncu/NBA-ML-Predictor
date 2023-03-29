from turtle import home
import pandas as pd


df_teams = pd.read_csv("archive/teams.csv")
df_games = pd.read_csv("archive/games.csv")
print(df_teams.head(5))
print(df_games.head(5))
rename_dict = {'NICKNAME' : "HOME_TEAM_NAME"}


def get_team_with_id(team_id):
    # print(df_teams.query("TEAM_ID == @team_id")['NICKNAME'].values)
    return df_teams.query("TEAM_ID == @team_id")['NICKNAME'].values[0]




home_teams_join = df_teams.join(df_games.set_index('HOME_TEAM_ID'), on='TEAM_ID')

home_teams_join = home_teams_join.rename(rename_dict, axis=1)
print(home_teams_join.columns)
home_teams_join["AWAY_TEAM_NAME"] = home_teams_join['VISITOR_TEAM_ID'].apply(get_team_with_id)

print(home_teams_join.columns)
print(home_teams_join[['HOME_TEAM_NAME', 'AWAY_TEAM_NAME', 'TEAM_ID', 'VISITOR_TEAM_ID', 'GAME_ID', 'GAME_STATUS_TEXT',  'PTS_home', 'FG_PCT_home', 'PTS_away','FG_PCT_away']].head()) 
       
       
       ##Print out stats that would be releavent to game outcome