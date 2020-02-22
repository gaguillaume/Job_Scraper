# app_dataenginnering
Projet de l'unité Data Engineering

L'objectif de notre projet est de pouvoir scraper et aggreger dans une seule et même application les offres d'emplois de plusieurs sites spécialisés. Pour le moment, nous récupérons les offres sur Indeed et Monster.  
  
Le Dashboard a pour objectif de créer une interface simple d'utilisation. Nous voulions également y intégrer de la visualisation des données comme des graphiques sur les salaires ou la possibilité d'analyser la donnée selon le type de société qui propose l'emploi mais nous avons manqué de temps pour le faire. Cela aurait permis par la suite de faire de la prédiction sur nos données et pourquoi pas permettre de mieux comprendre l'évolution du marché du travail.  
  
Nous avons également entrepris de faire un moteur de recherche pour nos annonces scrappées. Nous avons d'abord essayé de faire la recherche directement sur la base de données Mongo mais mongodb n'est pas intéressant pour faire cela. Nous nous sommes tournés vers Elasticsearch pour indexer les documents. L'indexation est faite mais il nous reste encore à faire les requêtes dans la page 'search engine'.

**Pour démarrer l'application Flask :**  
Dans le répertoire courant de "app_dataengineering", `docker-compose up -d --build`.  
  
*Puis on crée la base de donnée nommée Indeed :*
- `docker exec -it mongodb bash`.
- `mongo`.
- `use mongodb`.
- `db.createcollection("Indeed")` afin d'avoir la bonne table créée dans la bonne db.  
  
*Pour vider la base de donnée complètement :*  
- `docker exec -it mongodb bash`.
- `mongo`.
- `use mongodb`.
- `db.Indeed.deleteMany({})

**Infos partie Scraping :**  
Les fichiers utiles sont situés dans le dossier `Scraper/Scraper/`.  
Il y a 2 spiders, indeed et monster. Elles renvoient des Items qui contiennent le titre de l'annonce, la société, les liens du sites et de la page crawlée et, si disponible, un résumé de l'annonce, le salaire, et le lieu.  
  
Pour lancer le scraping manuellement, lancer `scrapy crawl <spider name>`. Il faudra au préalable retirer les allusions à Mongo et Elasticsearch dans le fichier `pipelines.py`.  

**Infos partie Flask :**
Le seul fichier à exécuter est `run.py`. L'application est de type MVC et nous retrouvons l'architecture classique d'une application Flask de ce type. A la racine se trouvent le `run.py`qui lance l'application, le `requirements.txt`contenant toutes les bibliothèques nécessaires ainsi que le Pipfile et Pipfile.lock pour l'utilisation de pipenv dans le Docker. Au sein du dossier de l'application en elle-même (`app`), nous retrouvons le `__init__.py` dans lequel sont instanciés l'application, l'admin et nos deux bases de données (mongodb pour la conservation long terme des éléments et elasticsearch pour le search engine que nous n'avons pas eu le temps de développer). Nous retrouvons ensuite le fichier `models.py` dans lequel se trouvent nos différents formulaires et la classe permettant l'affichage de nos données dans l'admin ainsi que l'ajout et suppression de celles-ci. Finalement nous avons le fichier `views.py`dans lequel se trouvent nos routes et les fonctions associées (backend de l'application). Dans le dossier `templates`se trouvent nos fichier html (frontend de l'application) et dans le dossier `static`l'ensemble des fichiers utiles au design (Bootstrap notamment). 

**Infos partie Docker :**  

  
**Infos partie Dashboard :**  
  
------
L'appli flask se trouve sur "localhost:5000".
Le scraper Real Time sur `localhost:9080 + requete` (inutile d'y toucher).
La db sur `localhost:27017` (inutile d'y aller aussi).  
Elasticsearch se trouve sur le port `localhopst:9200`. L'index se nomme 'annonces' et se trouve sur `localhopst:9200/annonces`.
