# Explication des choix
### Préparation des données

Nous avons construit deux matrices X et y. 
- X est de la forme `(len(data) x 12, 9, 9, 2)` et correspond aux données d'entrée (le plateau) ainsi que les rotations et symétries possibles du plateau.
- y est de la forme  `len(data) x 12, 2)`  et correspond aux probabilités de victoire de chacun des joueurs. 

### Réseau de Neurones

Celui-ci est composé de 10 couches.
- des couches `Conv2D` permettant de créer un noyau de convolution.
- des couches `BatchNormalization`pour normaliser les entrées. 
- des couches `Flatten` pour aplatir les données.
- des couches `Dense` pour relier les neurones avec `softmax`. 
- des couches `Droupout`pour ignorer certaines valeurs et éviter l'overfitting. 

# Contributeurs

Ce projet a été réalisé par :
- Saad MARGOUM (G4)
- Jalal IZEKKI (G1)
