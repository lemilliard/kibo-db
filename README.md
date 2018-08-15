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

## Lancer KiboDB à l'aide de Docker

Une image Docker a été créée afin de simplifier son utilisation sans avoir à installer l'environnement de 
développement.

Pour cela, il suffit de cloner le projet et de lancer les commandes suivantes dans un terminal à la racine 
du projet.

Pour le shell Windows, faire:
```
start ./scriptDocker.sh
```

Sur Git Bash, faire
```
sh ./scriptDocker.sh
```

## Tests unitaires

NB: Vous pouvez lancer les scripts et obtenir un rapport en faisant ceci:
```
sh ./test_runner.sh
```

<br/>

Pour lancer les tests unitaires, faire la commande suivante depuis la racine:
```
python -m unittest -s src/test
```

Pour lancer les tests unitaires avec la couverture de tests, faire la commande suivante depuis la racine:
```
coverage run -m unittest discover src/test/
```

Pour récupérer le rapport de couverture de test:
```
coverage report -m
```

Pour générer le rapport de couverture en html:
```
coverage html
```
