import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

#matches=pd.read_csv("matches.csv");
#deliveries=pd.read_csv("deliveries.csv");
matches    = pd.read_csv(r"C:\Users\admin\OneDrive\Desktop\python\project\matches.csv")
deliveries = pd.read_csv(r"C:\Users\admin\OneDrive\Desktop\python\project\deliveries.csv")

print("matches dataframe shape: ", matches.shape);
print("deliveries dataframe shape: ", deliveries.shape);
print("matches dataframe columns: ", matches.columns.tolist());
print("deliveries dataframe columns: ", deliveries.columns.tolist());

# most successful teams by win

team_wins=matches['winner'].value_counts().head(10);
plt.figure(figsize=(10,5));
sns.barplot(x=team_wins.index, y=team_wins.values, palette='viridis');
plt.title("Most Successful Teams by Wins");
plt.xlabel("Teams");
plt.ylabel("Number of Wins");
plt.tight_layout();
plt.savefig("most_successful_teams_by_wins.png");
plt.show();

#most successful teams by win percentage
team_matches=matches.groupby('team1').size() + matches.groupby('team2').size();
team_wins_percentage=(matches['winner'].value_counts()/team_matches*100).sort_values(ascending=False).head(10);
plt.figure(figsize=(10,5));
sns.barplot(x=team_wins_percentage.index, y=team_wins_percentage.values, palette='magma');
plt.title("Most Successful Teams by Win Percentage");
plt.xlabel("Teams");
plt.ylabel("Win Percentage");
plt.tight_layout();
plt.savefig("most_successful_teams_by_win_percentage.png");
plt.show();###

#toss decision analysis
toss_decision=matches['toss_decision'].value_counts();
plt.figure(figsize=(6,6));
plt.pie(toss_decision.values, labels=toss_decision.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff']);
plt.title("Toss Decision Analysis");
plt.tight_layout();
plt.savefig("toss_decision_analysis.png");
plt.show();

#top 10 batman by runs
top_batsmen=deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10);
plt.figure(figsize=(10,5));
sns.barplot(x=top_batsmen.index, y=top_batsmen.values, palette='coolwarm');
plt.title("Top 10 Batsmen by Runs");
plt.xlabel("Batsmen");
plt.ylabel("Total Runs");
plt.tight_layout();
plt.savefig("top_10_batsmen_by_runs.png");
plt.show();
#top 10 bowlers by wickets
top_bowlers=deliveries[deliveries['is_wicket']==1].groupby('bowler').size().sort_values(ascending=False).head(10);
plt.figure(figsize=(10,5));
sns.barplot(x=top_bowlers.index, y=top_bowlers.values, palette='coolwarm');
plt.title("Top 10 Bowlers by Wickets");
plt.xlabel("Bowlers");
plt.ylabel("Total Wickets");
plt.tight_layout();
plt.savefig("top_10_bowlers_by_wickets.png");
plt.show();
