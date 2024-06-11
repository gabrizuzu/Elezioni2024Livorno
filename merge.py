import pandas as pd
import glob
import os

# Ottieni una lista di tutti i file CSV nella cartella 'output'
csv_files = glob.glob('output/*.csv')

# Leggi il primo file CSV e aggiungilo alla lista dei DataFrame
df = pd.read_csv(csv_files[0], dtype={'Voti': int})
df = df.rename(columns={'Voti': os.path.basename(csv_files[0]).split('.')[0]})
dfs = [df]

# Leggi ogni file CSV successivo, rinomina la colonna 'Voti' e unisci il DataFrame con il precedente
for file in csv_files[1:]:
    df = pd.read_csv(file, usecols=['Sezione', 'Ubicazione', 'Voti'], dtype={'Voti': int})
    df = df.rename(columns={'Voti': os.path.basename(file).split('.')[0]})
    dfs[0] = pd.merge(dfs[0], df, on=['Sezione', 'Ubicazione'])

# Salva il risultato in un nuovo file CSV
dfs[0].to_csv('merged_output.csv', index=False)

print("Dati combinati salvati in merged_output.csv")