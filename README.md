# KiboDB

## Description

KiboDB est un SGBD dont l'objectif est principalement d'exposer une API plutôt que de nécessiter l'utilisation d'un
langage de requêtes comme le SQL.

KiboDB expose une API et utilise le format JSON pour l'ensemble de ses échanges avec les applications externes.

## Préparer l'environnement

Utiliser python 3.0.6
```
pip install virtualenv

virtualenv venv
```

Sur une invite de commande Windows:
```
venv\Scripts\activate
```

Sur Git Bash:
```
. venv/Scripts/activate
```

Pour finir, faire:
```
pip install -r requirements.txt
```

Enregistrer une nouvelle dépendances dans le fichier 'requirements.txt'
```
pip freeze > requirements.txt
```
