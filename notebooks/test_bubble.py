##%
import pandas as pd

df = pd.read_csv("/Users/florianlorisch/PycharmProjects/open-discourse-dynamic-topic-model/corpus/speeches/speeches_preprocessed.csv")

df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

##%
df['faction'].replace({"CDU/CSU": "CDU_CSU ", "DIE LINKE.": "DIE LINKE", "GB/BHE":"GB_BHE" }, inplace=True)

##%
df['faction'].value_counts()

##%
df_test = df.sample(n=50)

##%
import os
import shutil
from tqdm import tqdm
def create_folders(df, rootpath, clean = False):
    os.makedirs(rootpath, exist_ok=True) #directory wird angelegt, es gibt aber kein Fehler wenn es bereits existiert
    if clean:# wenn clean = True werden alle Ordner und Files die vorhanden sind gelöscht. WIchtig, wenn neuer Ergebnisse gescrhieben werden sollen
        shutil.rmtree(rootpath, ignore_errors=True)
    progress_bar = tqdm(iterable=df.iterrows(), unit = "speech", desc= "write speeches", total= len(df)) #itterows iteriert über einzelne Zeilen, wird in progressbar eingebettet. Progressbar wird im forloop aufgerufen
    for index, row in progress_bar: # index könnte auch durch _ genutzt werden, weil es für uns nicht relevant ist
        year = row['year'] #extrahiert das entsprechend Jahr aus der Zeile
        factionId = row['factionId'] #siehe oben
        politicianId = row['politicianId']
        id = row['id']
        speechContent = row['speechContent']
        result_sub_directory = os.path.join(rootpath, str(year)) #Zeigt an wo das Ergebnis directory angelegt werden soll
        if not os.path.exists(result_sub_directory):   #wenn ein Ordner mit dem entsprechenden Jahr bereits exsitiert, nicht anlegen, ansonsten Ordner anlegen
            os.makedirs(result_sub_directory)
        completeName = os.path.join(result_sub_directory,str(id)+"_"+str(factionId)+"_"+str(politicianId)+".txt") #der absolute pfad jedes einzelnen text files folgt dieser struktur
        with open(completeName,'w') as file:  #txt mit dem entsprechenden pfad wird geöffnet/angelegt
            file.write(speechContent) # inhalt der spalte speechcontent wird für die entsprechende Zeile in txt geschrieben

file_path = os.path.realpath(__file__)
script_path = os.path.dirname(file_path)
results_path = os.path.join(script_path,"corpus","raw_corpus")

create_folders(df, results_path, clean = True)

print("done")

##






