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

venv\Scripts\activate

pip install -r requirements.txt
```

Enregistrer une nouvelle dépendances dans le fichier 'requirements.txt'
```
pip freeze > requirements.txt
```

Les requêtes seraient de type suivant:

##### GET ALL
```
GET http://localhost:8080/{bdd}/{table}
```

Elle renverrait tous les enregistrement de la table.

##### GET BY ID
```
GET http://localhost:8080/{bdd}/{table}/{value}
```

Elle renverrait l'enregistrement dont l'id correspond à la valeur donnée.

##### GET BY CONDITION
```
POST http://localhost:8080/{bdd}/{table}
```

L'objet passé en body, serait ainsi fait:
```
{
	champs: [id, nom, prenom],
	condition: {
		nom: 'Robert',
		AND: [
			{
				prenom: 'George',
				OR: {
					anneeNaissance: [12, 1980]
				}
			},
			{
				taille: 180
			}
		]
	}
}
```

Cette condition donnerait en langage SQL classique:
```
SELECT
  id,
  nom,
  prenom
FROM {table}
WHERE
  (nom = 'Robert')
  AND (prenom = 'George'
    OR (anneeNaissance IN (12, 1980)))
  AND (taille = 180)
```

#### Les fichiers

Marque:
```
{
	id: ,
	intitule: '',
	slogan: '',
	fabriquant: '',
	reference: ['Voiture', 'Caravane'],
}
```

Voiture:
```
{
	id: ,
	marque: {
		id: ,
		intitule: '',
		slogan: '',
		fabriquant: '',
		reference: ['Voiture', 'Caravane']
	}
}
```

Caravane:
```
{
	id: ,
	marque: {
		id: ,
		intitule: '',
		slogan: '',
		fabriquant: '',
		reference: ['Voiture', 'Caravane']
	}
}
```

Au moment de la création d'une nouvelle table, par exemple Chaussure, embarquant une Marque
avec les mêmes champs id, intitule, slogan et fabriquant qu'une Marque voiture ou caravane, 
on ajoute Chaussure dans la reference de la marque et on met à jour toutes les voitures et caravanes
de la marque pour modifier la marque dedans

```
{
  "champs": [
    "id"
  ],
  "condition": {
    "nationalite": "France",
    "OR": {
      "id": 2
    },
    "AND": [
      {
        "marque": "Adria",
        "OR": {
          "annee": [
            2004,
            2014
          ]
        }
      },
      {
        "largeur": 12
      }
    ]
  }
}
```