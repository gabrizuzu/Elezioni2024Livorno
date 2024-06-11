import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# URL della pagina web contenente la tabella
partiti = ['FratelliDItalia', 'PD', 'MV5S', 'Lega', 'avs', 'PCD', 'ForzaItalia', 'StatiUnitiDeuropa', 'Azione'] 
urls = ['http://www.comune.livorno.it/risultati-elettorali/VL4412302.htm','http://www.comune.livorno.it/risultati-elettorali/VL4412311.htm', 'http://www.comune.livorno.it/risultati-elettorali/VL4412306.htm', 'http://www.comune.livorno.it/risultati-elettorali/VL4412304.htm','http://www.comune.livorno.it/risultati-elettorali/VL4412305.htm',
       'http://www.comune.livorno.it/risultati-elettorali/VL4412310.htm', 'http://www.comune.livorno.it/risultati-elettorali/VL4412308.htm', 'http://www.comune.livorno.it/risultati-elettorali/VL4412312.htm']
i = 0
for url in urls:
    # Scarica il contenuto della pagina web
    response = requests.get(url)
    html_content = response.content

    # Parsing dell'HTML con BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Trova la tabella. Potrebbe essere necessario modificare il selettore per trovare la tabella giusta
    table = soup.find('table')

    # Estrai le righe della tabella
    rows = table.find_all('tr')

    # Apri un file CSV per scrivere i dati
    with open('output/{}.csv'.format(partiti[i]), 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Scrivi le righe della tabella nel file CSV
        for row in rows:
            cells = row.find_all(['td', 'th'])
            cell_texts = [cell.get_text(strip=True) for cell in cells]
            csvwriter.writerow(cell_texts)
        # Leggi il file CSV saltando le prime tre righe
    # Leggi il file CSV saltando le prime tre righe
    df = pd.read_csv('output/{}.csv'.format(partiti[i]), skiprows=3)

    # Elimina l'ultima riga
    df = df.drop(df.tail(1).index)

    # Sovrascrivi il file CSV originale
    df.to_csv('output/{}.csv'.format(partiti[i]), index=False)
    i+=1
    print("Dati salvati in output.csv")
