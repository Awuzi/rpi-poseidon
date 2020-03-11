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
  - Logging.handlers
- Sqlite 3
- Observium
- HTML/CSS
- MQTT
- Bash

## **Installation et utilisation**

Pour installer la solution Poseidon, clonez le projet dans le dossier /home/pi. 
Une fois le clonage effectué, ouvrez un terminal dans ce dossier et tapez la commande ./run.sh pour démarrer la solution.
Le fichier run.sh lance la capture et le stockage des données dans la base de données et le serveur web de l'interface d'affichage des données.



