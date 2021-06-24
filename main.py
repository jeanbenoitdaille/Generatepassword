import string
import random
     
taille = 8
     
symboles = string.ascii_letters + string.digits + string.punctuation
mot_de_passe = ''.join(random.choice(symboles) for _ in range(taille))
     
print(mot_de_passe)