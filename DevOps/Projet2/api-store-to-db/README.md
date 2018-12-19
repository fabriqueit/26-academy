# API utilisé en relais afin de pousser les données des bracelés de santé connectés vers une base de donnée MongoDB
Projet tutoré n°2 concernant le parcours DevOps

## Installer les dépendances du projet python
pip install -r requirements.txt

## Démarer l'API 
python \_\_main\_\_.py -H mon_serveur_mongo -P 27017 -D ma_database_mongo -u mon_user_mongo -p mon_password_mongo -A mon_api_bracelet
