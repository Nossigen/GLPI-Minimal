# GLPI Minimal

## Objectif

Developper un site lie au CRM permettant la gestion du parc informatique.
(Exemple https://materiel.actecil.fr)

Le site en question devra avoir ces fonctionnalites:

<strong>Commande</strong>

> - Une commande est une liste d'objets
> - Chaque commande a un status: En cours/Recue
> - Chaque commande a un commentaire facultatif
> - Une commande avec le status recu rajoute les objets indique dans la liste des objets disponible
> - Une commande est editable
> Facultatif:
> - Il est possible qu'une commande soit recu en partie

<strong>Objet</strong>

>- Un objet commande est un paquet contenenant plusieurs elements (Par exemple un ordinateur est une carte mere, avec de la ram, un ecran, une sacoche, un windows, un souris, clavier ...)
> - Un objet est soit en stock, soit il est liste comme appartenant a une personne
> - Un objet appartenant a une personne a une date de don ainsi qu'un etat au moment du don
> - Un objet rendu doit etre mis a jour avec un nouvel etat
> - L'action de donner/rendre un objet est suivit de la creation d'un fichier pdf definissant l'action executer

<strong>Fournisseurs</strong>

>- Les fournisseurs sont defini par un contact (adresse, email, nom), les commandes effectue ainsi qu'un commentaire facultatif

Dans le cas ou un bug informatique ou un probleme est decouvert, <strong>l'administrateur a la possibilite de forcer l'ajout d'objets</strong>

## Cible

Personnes charge de la gestion du parc informatique au sein de/des agences actecil

## Budget

Fait en interne, il n'y a donc pas de budget

## Arborescence

![arborescence](./img/arborescence.png)

## BDD

En cour de creation

## Maquette

Non disponible

## Techo utlise

| Techno' |Version|But|
|---|---|---|
| Python | 3 | Langage backend
|Django | 1.9 ou derniere version | Framework backend 
| Html - Css | 5 - 3 | Langage structurel frontend 
| Ajax | ? | Mise a jour du site sans rechargement de page

## Site en ligne

Site d'origine: 

[GLPI](https://demo.glpi-project.org/index.php?noAUTO=1)

## Historique de modification

- 14/09/18: Creation du concept, du depot ainsi que l'arborescence du projet