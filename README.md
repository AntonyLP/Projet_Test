[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/works-on-my-machine.svg)](https://forthebadge.com)

# Projet Universitaire Django - IUT Aix-Marseille 2023

Ce dépôt contient le code source du projet universitaire réalisé à l'IUT Aix-Marseille.

## Technologies utilisées

* [Django](https://www.djangoproject.com/) : Framework web en Python (4.1.3)
* [Python](https://www.python.org/) : Langage de programmation (3.10)
* [HTML/CSS/JS](https://developer.mozilla.org/fr/docs/Web) : Technologies du web pour la création de l'interface utilisateur


## Prérequis
* Avoir Python 3.10
* Avoir un environnement virtuel (venv) configuré pour ce projet


## Installation
1. Clonez ce dépôt en utilisant la commande suivante :
```bash
git clone https://github.com/AntonyLP/Projet_Test.git
```

2. Accédez au répertoire du projet avec la commande :
```bash
cd /Projet_Test
```

3. Installez les dépendances nécessaires avec la commande :
```bash
pip install -r requirements.txt
```

4. Effectuez les migrations nécessaires avec les commandes suivantes :
```bash
python manage.py migrate
```

5. Lancez le serveur de développement avec la commande :
```bash
python manage.py runserver
```

L'application sera alors disponible à l'adresse http://localhost:8000/ dans votre navigateur.

***

### Webhook

Pour l'envoi de webhook vers votre serveur Discord et donc cliqué sur le bouton d'envoi, il est important d'avoir créé et remplit son profil.
Il vous suffit de cliquer sur `Profil` et d'y renseigner les champs. 

Vous reportez à l'explication de Discord pour la [création d'un webhook](https://support.discord.com/hc/fr/articles/228383668-Introduction-aux-Webhooks).

***

## Auteur
DECROIX Antony
