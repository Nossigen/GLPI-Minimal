# Ajout d'objets

## Bonne pratique

La manière dont a été pensé l'ajout d'objets est le suivant:

- L'administrateur passe commande d'un certains nombre d'objets auprès d'un fournisseur, à ce moment là, la commande a le status 'en attente'
- Une fois la commande reçue, l'administrateur passe la commande de 'en attente' à 'reçu'. Ce qui fait en sorte que ces objets soient en Stock.
- L'administrateur peut alors faire passer les objets du stock au utilisateurs.

## Ce qu'il ne faut pas faire

L'ajout forcé d'objet fait parti du site pour les cas où des objets sont en stock mais n'ont pas été commandé (lors de l'implémentation de ce site par exemple).

Si l'ajout d'un objet est forcé, il n'a pas de commande et par conséquent, pas de fournisseurs.