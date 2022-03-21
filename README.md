# Coding test - Spinergie
Voici le resultat de mon test.

Vous trouverez le fichier 'response.py' qui prend en argument un CONFIG_FILE
et un MODIFS_FILE

# Feature implémenté
- La premiere partie fonctionne totalement.
- La deuxieme partie fonctionne partiellement, en effet il existe des injections
de JSON qui ne fonctionne toujours pas.
- La troisieme partie fonctionne totalement.


## Remarque
### Securité
Apres avoir travailler sur cet exos. Il est important à noter qu'il y a un
vrai problème de sécurité. En effet, l'utilisation d'un ```py exec``` ou d'un
```py eval ``` est une trés mauvaise idée puisqu'on ne connais pas l'origine
du fichier (back ou front).

### JSON de départ
#### Dash
Afin de facilité l'utilisation de cette dernière il serait peut être judicieux
de remplacer les '-' par des '_' puisque le compilo de python n'aime pas
beaucoup les dash en tant que methode de class

#### Pagination
L'utilisation de pages en tant qu'attributs n'est pas une bonne idée selon moi,
en effet j'ai été forcé de passer par SimpleNamespace qui (toujours selon moi)
manque d'abstraction.

### Modifs file
Le modif file donné en exemple n'est pas un JSON. Je suis donc parti du principe
que l'exemple été correct et donc j'ai du pratiquement parser "a la main".
Si le file en question été un JSON, la tâche aurait pu être bien plus simple.



# Authors
Yassine Damiri
