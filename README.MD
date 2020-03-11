<img src="Poseidon.png" align="left" width="120px"/>
<img align="left" width="0" height="192px" hspace="10"/>

> # **POSEIDON - RASPBERRY PI**

Gestion des paramètres environnementaux (Température, Pression de l'air, Humidité) d'une salle serveur, avec interface et système de notification par email, ainsi que sauvegarde sur base de données distante via MQTT.

<br>

## **Technologies utilisées**

- Python 3
  - Flask
  - Paho-MQTT
  - Pygal
  - SQLite3
  - Logging.handlers
- SQLite 3
- Observium
- HTML/CSS
- MQTT
- Bash

## **Installation et utilisation**

Pour installer la solution Poseidon, clonez le projet dans le dossier /home/pi. 
Une fois le clonage effectué, ouvrez un terminal dans ce dossier et tapez la commande ./run.sh pour démarrer la solution.
Le fichier run.sh lance la capture et le stockage des données dans la base de données et le serveur web de l'interface d'affichage des données.

## ***Première ébauche :***

**1)	Installer et configurer la base de données SQLite sur le Raspberry PI. Cette base doit enregistrer les données de la température, du taux d’humidité et de la pression dans une table. Ces données doivent être horodatées.**

Afin de mettre en place SQLite il faut passer par les commandes :
```
$ >     sudo apt-get install sqlite3
$ >     sqlite3 poseidon.db
sqlite> CREATE TABLE data_poseidon(ID INTEGER PRIMARY KEY AUTOINCREMENT, Pression INTEGER, Humidity INTEGER, Temperature INTEGER, Timestamp DATETIME DEFAULT current_timestamp);
```


**2)	Proposer une solution permettant d’afficher cette historique sous forme de courbes.**

Après avoir ajouté les données dans la base de données sqlite3, nous pouvons maintenant grâce à la librarie **Pygal** mettre en place l'affichage de graphes et de courbes sur nos pages HTML
Pour se faire : 
```
$ > sudo pip3 install pygal
```
Dans le code (exemple pour recuperer la température) :
```python
import pygal

[...]

@app.route('/temperature/')
def tempGraph():
    temp = pygal.Line()
    temp.title = 'Temperatures of the Server Room'
    temp.x_labels = get_datas_by_name('Timestamp')
    temp.add('Temperature', get_datas_by_name('Temperature'))
    temp_data = temp.render_data_uri()
    
    return render_template("graphingTemp.html", temp=temp_data)
```
Dans le fichier HTML afficher les données de cette manière 

```html
<embed type="image/svg+xml" src={{temp|safe}} style='max-width:1000px; border-radius: 10px; background-color: lavender'/>	
```




**3)	Installer et configurer une solution avec MQTT permettant de transmettre les paramètres environnementaux à un serveur de base de données (MariaDB / MySQL). Cette solution devra être mise en place sur le Raspberry PI. La communication dans les deux sens devra être possible.**



**4)	Proposer une solution permettant d’afficher cette historique sous forme de courbes.**


https://puu.sh/FjxxG/460cc109ad.png
