<h2 align="center">
 Calculatrice NPI (Notation Polonaise Inverse)
</h2>

* [Capture 1](./images/calculatrice.png) 
* [Capture 2](./images/calculatrice2.png)

## Description

La notation polonaise inverse (NPI) (en anglais RPN pour Reverse Polish Notation), également connue sous le nom de notation post-fixée, permet d'écrire de façon non ambiguë les formules arithmétiques sans utiliser de parenthèses. Dérivée de la notation polonaise présentée en 1924 par le mathématicien polonais Jan Łukasiewicz, elle s’en différencie par l’ordre des termes, les opérandes y étant présentés avant les opérateurs et non l’inverse.

## Configuration

### Technologies/Librairies

* Linux/Ubuntu
* Visual Studio Code
* Python 3.10
* Flask 2.2.3
* Unittest 3.11.2
* Waitress 2.1.2
* SQLite 3.41.2
* Docker
* HTML5
* Bootstrap 3.3.2 

### Installation

#### Clone depuis github

```
git clone https://github.com/mtbinds/NPI.git 
cd NPI
``` 
#### Création d'un environnement python et l'activer 

```
git clone https://github.com/mtbinds/NPI.git 
cd NPI
python -m venv env
source env/bin/activate
```

### Installation des libairies Python

```
pip3 install -r requirements.txt
```

## Création de la base de données SQLite

```
python3 SQLITE_BD.py
```

## Démarrage de l'API Flask avec le serveur waitress

```
python3 NPI.py
```
* Vous pouvez maintenant accéder à l'application web [http://localhost:5000](http://localhost:5000)

## Utilisation de docker compose 

```
docker compose up
```
* Vous pouvez maintenant accéder à l'application web [http://localhost:5000](http://localhost:5000) 

## Auteur

Madjid TAOUALIT  
[Site Web](https://madjidportfolio.vercel.app/)

## Version History

* 0.1
    * Various bug fixes and optimizations
    * Voir [commit change]() ou Voir [release history]()


## License

This project is licensed under the MIT License - voir le fichier LICENSE.md pour plus de détails
