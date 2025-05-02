# TodoMaster

Une application de gestion de tâches développée avec Django.

## Fonctionnalités

- Création et gestion de tâches avec priorités
- Catégorisation des tâches
- Filtrage par statut, priorité et catégorie
- Interface utilisateur responsive avec Bootstrap

## Installation

1. Cloner le dépôt
   git clone https://github.com/PrincyW/todomaster.git
2. Créer et activer un environnement virtuel
   python -m venv env
   source env/bin/activate  # Sur Windows: env\Scripts\activate
3. Installer les dépendances
   pip install -r requirements.txt
4. Appliquer les migrations
   python manage.py migrate
5. Lancer le serveur de développement
   python manage.py runserver
