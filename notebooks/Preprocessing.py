import pandas as pd
import feather
#import os
##
df = pd.read_feather("/Users/florianlorisch/PycharmProjects/open-discourse-dynamic-topic-model/corpus/speeches.feather")
print(df.head(10))
##
convert_dict = {'id': int,
                'session': int,
                'electoralTerm': int,
                'politicianId': int,
                'factionId': int
                }
df = df.astype(convert_dict)
print(df.dtypes)
## Change date type and sort by date
df['date'] = pd.to_datetime(df['date'])
print(df.sort_values(by=['date']))
print(df.shape[0])
#%% Delete irrelevant datapoints
df = df.drop(df.loc[df['factionId']==-1].index) #dropping all except MEP --> From 899526 speeches to 370153
print(df.shape[0])
#%% drop speeches with less than 1000 characters
df=df.drop(df.loc[df['speechContent'].str.len() < 1000].index) #214478
#%% Regex
df.replace({'speechContent': '(\\n)'}, {'speechContent': ' '}, regex=True, inplace=True)

df.replace({'speechContent': '(\.\B)'}, {'speechContent': ' . '}, regex=True, inplace=True)

df.replace({'speechContent': '(\!)'}, {'speechContent': ' ! '}, regex=True, inplace=True)

df.replace({'speechContent': '(\?)'}, {'speechContent': ' ? '}, regex=True, inplace=True)

df.replace({'speechContent': '(\,)'}, {'speechContent': ' , '}, regex=True, inplace=True)

df.replace({'speechContent': '(\(\{\S*\}\))'}, {'speechContent': ' '}, regex=True, inplace=True)

df.replace({'speechContent': '(\\xa0–)'}, {'speechContent': ''}, regex=True, inplace=True)

df.replace({'speechContent': '(\\xa0)'}, {'speechContent': ' '}, regex=True, inplace=True) # Check ist Okay

df.replace({'speechContent': '(\–\\xa0)'}, {'speechContent': ''}, regex=True, inplace=True)

df.replace({'speechContent': '(\\xad)'}, {'speechContent': ''}, regex=True, inplace=True)




#%% Zuordnung zwischen Fraktion und FactionID

factions_dict = {
     0 : "AFD",
     1 : "BHE",
     2 : "BP",
     3 : "Grüne",
     4 : "CDU/CSU",
     5 : "DA",
     7 : "DP",
     6 : "DIE LINKE.",
     8 : "DP", #Deutsche Partei Bayern zu DP
     9 : "DP/FVP",
     10 : "DP", #Deutsche Partei Bayern zu DP
     11 : "DRP",
     12 : "NR", #Deutsche Reichspartei/NR konsolidiert zu NR
     13 : "FDP",
     14 : "FU",
     15 : "FVP",
     16 : "Fraktionslos",
     17 : "GB/BHE",
     18 : "Gast",
     19 : "KO", #kraft oberländergruppe ggf. im Nachgang noch löschen
     20 : "KPD",
     21 : "NR",
     22 : "PDS",
     23 : "SPD",
     24 : "SSW",
     25 : "WAV",
     26 : "Z"
}
df['faction'] = df['factionId'].map(factions_dict)
#del df['factionId']

#%%

df.reset_index().to_feather("/Users/florianlorisch/PycharmProjects/scientificProject/corpus/speeches/speeches_preprocessed.feather")
print("feather: Done")

df.to_csv("/Users/florianlorisch/PycharmProjects/scientificProject/corpus/speeches/speeches_preprocessed.csv")
print("csv: Done")

df_csv = pd.read_csv("/Users/florianlorisch/PycharmProjects/scientificProject/corpus/speeches/speeches_preprocessed.csv")
speechList = []
for i in range(len(df_csv.speechContent)):
     speechList.append(df_csv.speechContent[i])
with open("/Users/florianlorisch/PycharmProjects/scientificProject/corpus/speeches/speeches_preprocessed.txt", 'w') as filehandle:
     for listitem in speechList:
         filehandle.write('%s' % listitem)
print("txt: Done")
## just the greens
df_grüne = df[df["faction"] == "Grüne"]
df_grüne.to_csv("/Users/florianlorisch/PycharmProjects/scientificProject/corpus/speeches/speeches_preprocessed_grüne.csv")
print("csv Grüne: Done")
print("preprocessing complete motherfucker!")
