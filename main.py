from turtle import home
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df_teams = pd.read_csv("archive/teams.csv")
df_games = pd.read_csv("archive/games.csv")
print(df_teams.head(5))
print(df_games.head(5))
rename_dict = {'NICKNAME' : "HOME_TEAM_NAME"}


def get_team_with_id(team_id):
    # print(df_teams.query("TEAM_ID == @team_id")['NICKNAME'].values)
    return df_teams.query("TEAM_ID == @team_id")['NICKNAME'].values[0]


def get_team_stats_id(team_id):
    pass



home_teams_join = df_teams.join(df_games.set_index('HOME_TEAM_ID'), on='TEAM_ID')

home_teams_join = home_teams_join.rename(rename_dict, axis=1)
# print(home_teams_join.columns)
home_teams_join["AWAY_TEAM_NAME"] = home_teams_join['VISITOR_TEAM_ID'].apply(get_team_with_id)

print(home_teams_join.columns)
# print(home_teams_join[['HOME_TEAM_NAME', 'AWAY_TEAM_NAME', 'TEAM_ID', 'VISITOR_TEAM_ID', 'GAME_ID', 'GAME_STATUS_TEXT',  'PTS_home', 'FG_PCT_home', 'PTS_away','FG_PCT_away']].head()) 




true_y = home_teams_join["HOME_TEAM_WINS"]
print(true_y.head)

##26651 total entries so (26651 * .8 =  21,321) for training data... 
#Test data is what is remaining, will be 5330

my_features = ['FG_PCT_home', 'FT_PCT_home', 'FG3_PCT_home', 'AST_home', 'REB_home', 'TEAM_ID_away', \
    'FG_PCT_away', 'FT_PCT_away', 'FG3_PCT_away', 'AST_away', 'REB_away']


df_train = home_teams_join[:21321]
y_train = true_y[:21321]

df_test = home_teams_join[21321:]
y_test = true_y[21321:]

print(len(df_train))
print(len(y_train))

print(len(df_test))
print(len(y_test))

##TRAIN MODEL HERE 

##First I will try DECISIONTREE CLASSIFIER 
my_model = DecisionTreeClassifier(max_depth=5)


df_train_input = df_train[my_features].copy()
df_test_input = df_test[my_features].copy()


my_model.fit(df_train_input, y_train)

predict = my_model.predict(df_test)

print(predict)