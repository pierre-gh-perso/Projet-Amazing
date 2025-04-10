# Projet Amazing

Ce projet vise à concevoir, entraîner et industrialiser un modèle de **segmentation client** pour la plateforme e-commerce *Amazing*. Il repose sur une approche **non supervisée (K-means)**, enrichie d’une **ACP** pour la réduction de dimensionnalité, et s’intègre dans une architecture technique exploitable à l’échelle de l’entreprise.

---

## Structure du projet

```
📦 amazing-segmentation/
├── data/
│   ├── raw/              # Données brutes initiales
│   ├── cleaned/          # Données nettoyées
│   ├── processed/        # Données vectorisées, PCA, clustering
│   └── output/           # Résultats finaux (user_features, clusters, modèles .pkl)
│
├── notebooks/
│   ├── 1- feature_engineering.ipynb
│   ├── 2- ACP_amélioré.ipynb
│   ├── 3.1- add_new_data.ipynb
│   ├── 3.2- prediction_nouveau_user.ipynb
│   └── 4- test_promotion.ipynb
│
├── src/
│   ├── preprocessing/        # Fonctions de préparation des données
│   ├── clustering/           # ACP, K-means, sauvegarde du modèle
│   ├── prediction/           # Pipeline de prédiction pour nouveaux utilisateurs
│   └── utils.py              # Fonctions utilitaires communes
│
├── docker/
│   └── Dockerfile            # Image Docker avec tous les packages nécessaires
│
├── requirements.txt          # Dépendances Python
├── README.md                 # Ce fichier
└── .gitignore
```

---

## Objectifs

- Construire un **modèle de clustering robuste** à partir des données comportementales des utilisateurs.
- Permettre l’analyse et la visualisation des **profils clients typiques** (radar chart, barplot, PCA).
- Simuler des **scénarios marketing** et mesurer leur impact sur les groupes (AB testing).
- Industrialiser le pipeline via **Docker** et envisager un déploiement sur **Kubernetes**.
- Intégrer les résultats dans le **SI de l’entreprise (Redshift / BI / CRM)**.

---

## Mise en place du projet

### 1. Cloner le repo

```bash
git clone https://github.com/<ton-nom-utilisateur>/amazing-segmentation.git
cd amazing-segmentation
```

### 2. Créer un environnement Python

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Lancer les notebooks

Les notebooks sont à exécuter dans cet ordre :
1. `0- Transformation parquet.ipynb`
2. `1- data_cleaning.ipynb`
3. `3.1- add_new_data.ipynb` #Seulement la deuxième partie du code

---

## Dockerisation

### 1. Build de l’image

```bash
docker build -t amazing-segmentation .
```

### 2. Lancer le container

```bash
docker run -p 8888:8888 amazing-segmentation
```

Le projet est accessible sur [http://localhost:8888](http://localhost:8888).

---

## Intégration dans le SI

- Les modèles (.pkl) sont prêts à être utilisés dans un **microservice** de prédiction.
- Le pipeline est conçu pour être orchestré via **Kubernetes**.
- Les résultats peuvent être injectés dans **Redshift** pour exploitation par les équipes marketing.

---

## Exemple de résultats

- 4 clusters identifiés avec des profils distincts
- Analyse de scénarios : impact des promotions, recommandations, offres urgentes
- Visualisations : PCA 2D, radar charts par cluster, barplots comparatifs

---

## Technologies utilisées

- Python, Pandas, Scikit-learn
- Jupyter Notebooks
- Docker, Kubernetes
- Matplotlib, Seaborn, Plotly
- Redshift (prévu pour intégration)

---

## Auteur

Projet réalisé dans le cadre du MSPR "Modèle IA" – 2025  
Pierre-Alexandre Simonnet – Junia XP  
Contact : [pierrealexandre.simonnet@gmail.com]

---
