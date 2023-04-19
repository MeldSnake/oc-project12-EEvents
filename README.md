#Epic Events
![python 3.11](https://img.shields.io/badge/python-v3.11-blue)
Epic Events est un projet conçu pour aider l’entreprise “Epic Events” dans sa gestion d’événements et de fêtes. Le projet est destiné à être utilisé uniquement par les employés de l’entreprise.

##Rôles des utilisateurs
Il y a trois types d’employés qui peuvent utiliser le projet : la direction, les ventes et le support.

**Vente:** Peut créer de nouveaux modèles de clients et des contrats après des discussions marketing. Une fois qu’un contrat est signé, un nouveau modèle d’événement est créé et attribué à un employé de support.
**Support:** gèrer  des événements et mettre à jour les modèles d’événements attribué. Une fois terminé, l’événement est marqué comme terminé.
**Direction:** peut modifier tous les modèles afin de résoudre les problèmes avec le service, tel que des érreures de remplissage.

##Détails techniques
Le projet est écrit en Python et utilise Django comme framework.
Pour la journalisation(logging), [Sentry](https://sentry.io/) est utilisé.
L’authentification se fait via des jetons JWT via [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/).

##Installation
Pour configurer un environnement de développement, suivez ces étapes :

1. Créez un environnement virtuel Python :
    - `python3 -m venv venv`
2. Activez l’environnement virtuel :
    - **Linux|MacOS:** `source venv/bin/activate`
    - **Windows (powershell):** `& venv/bin/activate.ps1`
    - **Windows (cmd):** `venv/bin/activate.bat`
3. Installez les exigences :
    - `pip install -r requirements.txt`

##Demarrage
Pour démarrer le serveur, utilisez la commande suivante :
```shell
> python manage.py runserver
```

##Documentation
Une documentation Postman a été générée et peut être consultée à l’adresse suivante: [documentation](https://documenter.getpostman.com/view/26149355/2s93Y2ShSG).
