import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read in annual population data for Virginia
# source: https://fred.stlouisfed.org/series/VAPOP
df = pd.read_csv("VAPOP.csv")
df = df.loc[76:]
df['VAPOP'] = df['VAPOP']*1000
df = df.iloc[::4, :]
df['DATE'] = pd.to_datetime(df['DATE'])
df['DATE'] = df['DATE'].dt.strftime('%Y')
df.set_index('DATE',inplace=True)
print(df)

# read in second data source: voter turnout in VA
# source: https://www.elections.virginia.gov/resultsreports/registration-statistics/registrationturnout-statistics/index.html
voter_df = pd.read_csv("VA_Voter_Turnout.csv",encoding='latin1',thousands=',')
voter_df = voter_df[['Year','Total Voting']]
voter_df['Year'].replace('\*','',regex=True,inplace=True)
voter_df = voter_df.iloc[::4, :]
voter_df.set_index('Year',inplace=True)

# create figure, set basic parameters
fig = plt.figure(figsize=(14,6))
plt.gca().set_facecolor('lightgrey')
plt.gca().xaxis.grid()
plt.gca().yaxis.grid()
plt.title("Population and Voter Turnout in Presidential Election Years in Virginia since 1976")

# plot data, show graph
plt.plot(df,c='darkblue',linewidth=2,label='Population of Virginia')
plt.plot(voter_df,c='darkgreen',linewidth=2,label='Voter Turnout')
plt.gca().set_yticklabels(['{:,}'.format(int(x)) for x in plt.gca().get_yticks().tolist()])
plt.legend()
plt.show()
