Question à ChatGPT: 
Comment réduire le container sur le pc

Pour réduire la largeur du conteneur sur un ordinateur de bureau, vous pouvez utiliser des règles CSS pour définir une largeur maximale. Voici comment vous pouvez le faire :

1. Modifiez la classe `.container` dans le CSS pour inclure une largeur maximale. 
   Par exemple, vous pouvez définir une largeur maximale de 800 pixels.

```css
.container {
    max-width: 800px; /* Largeur maximale de 800 pixels */
    margin: 0 auto; /* Pour centrer le contenu horizontalement */
    padding: 20px;
}
```

2. Ajoutez un ajustement pour le texte et les éléments de la page pour s'adapter 
   à la nouvelle largeur maximale, en modifiant les tailles de police ou 
   les marges si nécessaire.

Votre code CSS mis à jour ressemblera à ceci :

```css
.container {
    max-width: 800px; /* Largeur maximale de 800 pixels */
    margin: 0 auto; /* Pour centrer le contenu horizontalement */
    padding: 20px;
}

h1 {
    font-size: 24px; /* Ajustement de la taille de la police pour l'en-tête */
}

p {
    font-size: 16px; /* Ajustement de la taille de la police pour les paragraphes */
}
```

Avec ces modifications, la largeur du conteneur sera réduite à 800 pixels 
sur un ordinateur de bureau. Vous pouvez ajuster la valeur de `max-width` 
en fonction de la largeur souhaitée pour le conteneur.