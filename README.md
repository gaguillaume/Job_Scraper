# app_dataenginnering
Projet de l'unité Data Engineering

**Infos partie Scraping :**  
Les fichiers utiles sont tous dans le dossier Scraping/Scraper/Scraper/ et le fichier scrapy.cfg.  
Il y a 2 spiders, indeed et indeed2. Indeed2 utilise des Items --> meilleur.  
Pour lancer le scraping manuellement, lancer `scrapy crawl indeed2`.

**Infos start appli :**
Dans le répertoire courant de "app_dataengineering", `docker-compose up -d --build`.
Puis `docker exec -it mongodb bash`.
Puis `mongo`.
Puis `use mongodb`.
Puis `db.createcollection("Indeed")` afin d'avoir la bonne table créée.

L'appli flask se trouve sur "localhost:5000".
Le scraper Real Time sur `localhost:9080 + requete` (inutile d'y toucher).
La db sur `localhost:27017` (inutile d'y aller aussi).

