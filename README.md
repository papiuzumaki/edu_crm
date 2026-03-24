# Edu.CRM

Application de gestion scolaire développée avec Flask et Blueprints dans le cadre d'un projet de groupe.

## Membres du groupe

- **Pape Oumar Ndiaye** — Auth, Gestion des étudiants, Dashboard & UI
- **Abdoul Salif Diallo** — Gestion des enseignants, Gestion des cours

## Ce que fait l'application

- Connexion / déconnexion avec protection des routes
- Ajouter, modifier et supprimer des étudiants
- Ajouter, modifier et supprimer des enseignants
- Créer des cours, inscrire et désinscrire des étudiants
- Dashboard avec les statistiques générales
---

**6. Ouvrir dans le navigateur**
```
http://127.0.0.1:5000
```

Identifiants de connexion : **admin** / **admin123**

---

## Réponses aux questions

**Pourquoi utiliser Application Factory ?**
Pour créer l'app dans une fonction `create_app()`, ce qui facilite la configuration et évite les imports circulaires.

**Pourquoi séparer routes et services ?**
Les routes gèrent les requêtes HTTP, les services gèrent la logique métier. C'est plus propre et plus facile à maintenir.

**Que se passe-t-il si un blueprint n'est pas enregistré ?**
Ses routes n'existent pas, Flask retourne une erreur 404 et `url_for()` plante.

**Pourquoi utiliser url_prefix ?**
Pour regrouper les routes d'un blueprint sous un même chemin (ex: `/students`) et éviter les conflits.

**Où doit se trouver la logique métier ?**
Dans les fichiers `*_service.py`, pas dans les routes.
