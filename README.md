# Generatepassword
Générer un générateur de mots de passe 
Le but de cet exercice était de générer un mot de passe aléatoire.

Le mot de passe devait être d'une longueur définie dans la variable "taille".

La première chose à faire était de récupérer toutes les lettres de l'alphabet, les nombres et tous les symboles.

Pour récupérer ces informations, nous utilisons le module string :

    >>> symboles = string.ascii_letters + string.digits + string.punctuation
    >>> symboles
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

On utilise ensuite le module random et la fonction choice comme vu dans un exercice précédent. Cette fonction va nous permettre de sélectionner une lettre aléatoire parmi la chaîne de caractère "symboles" que nous avons déclaré plus haut.

Pour répéter l'opération autant de fois que nécessaire, on utilise une boucle et une compréhension de liste :

    random.choice(symboles) for _ in range(taille)

Pour terminer, nous joignons ensemble tous les éléments aléatoires récupérés grâce à la fonction join :

    mot_de_passe = ''.join(random.choice(symboles) for _ in range(taille))
