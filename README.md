# Calcul approché d'intégrales

## Présentation du problème

Ce projet présente plusieurs méthodes de calcul d'intégrales, autrement dit des méthodes donnant une approximation de l'intégrale
$I = \displaystyle \int_{a}^{b} f(t) dt$ où $\displaystyle [a, b]$ est un segment et $\displaystyle f$ une fonction continue.
Je me suis penché sur plusieurs méthodes : rectangles à gauche et à droite, trapèzes, point milieu. Les méthodes de Simpson et de Newton-Cotes suivront prochainement.

## Pré-requis

- Calcul de primitives des fonctions usuelles : polynomiales, exponentielles etc.
- Interpolation polynomiale : optionnel, bon à savoir pour les méthodes de Simpson et de Newton-Cotes.

## Structure du projet

Ce fichier README.md contient le détail mathématique du projet ainsi que certains résultats à l'avenir concernant le calcul approché d'intégrales de fonctions polynomiales, exponentielles et sinusoïdales.

Les différentes méthodes sont codées dans le fichier Methodes.py et appliquées sur ces exemples dans le Jupyter Notebook Integrales.ipynb

## Décomposition d'un segment

Toutes les méthodes que je présente dans ce projet font appel à la décomposition du segment $\displaystyle J = [a, b]$ en $\displaystyle n$ sous-segments de même longueur identique $\displaystyle h = \frac{b - a}{n}$

On note $\displaystyle \forall k \in [\![0, n]\!] , t_k = a+kh$ et $\displaystyle \forall k \in [\![0, n-1]\!]  , J_k = [t_k, t_{k+1}] = [a+kh, a+(k+1)h]$

L'intégrale de la fonction $f$ est d'abord approchée sur chaque segment $\displaystyle [t_k, t_{k+1}]$ puis la relation $\displaystyle \int_{a}^{b} f(t) dt = \sum_{k = 0}^{n-1} \int_{t_k}^{t_{k+1}} f(t) dt$ permet de donner une approximation de l'intégrale sur le segment $[a, b]$ en entier en additionnant toutes les valeurs approchées des intégrales sur les sous-segments $J_k$

## Approximation de $\displaystyle \int_{t_k}^{t_{k+1}} f(t) dt$

Toute la difficulté du problème se trouve dans l'approximation de $\displaystyle \int_{t_k}^{t_{k+1}} f(t) dt$ ou encore dans l'approximation de $\displaystyle m_k$, où $\displaystyle m_k$ est la valeur moyenne de la fonction $\displaystyle f$ sur le segment $\displaystyle J_k$ étant donné que $\displaystyle \int_{t_k}^{t_{k+1}} f(t) dt = m_kh$ par définition.
On notera $\displaystyle \hat m_k$ la valeur approchée de $\displaystyle m_k$ par la suite.

## Méthodes utilisées

### Méthode des rectangles

La méthode des rectangles consiste à approcher la valeur moyenne de $f$ sur $J_k$ par la valeur de $f$ en l'une des extrémités du segment.
Comme le nom de ces méthodes l'indique, la méthode des rectangles à gauche utilise la valeur de $f$ en $t_k$ , autrement dit $\hat m_k = f(t_k)$ tandis que la méthode des rectangles à droite utilise la valeur de $f$ en $t_{k+1}$ , autrement dit $\hat m_k = f(t_{k+1})$

Sur l'ensemble du segment $[a, b]$ , ces méthodes donnent comme approximations
$I_{r, g} = \displaystyle\frac{b-a}{n} \sum_{k = 0}^{n-1} f(t_k)$ et $I_{r, d} = \displaystyle\frac{b-a}{n} \sum_{k = 1}^{n} f(t_k)$

### Méthode des trapèzes

La méthode des trapèzes est en quelque sorte la moyenne arithmétique de la méthode des rectangles à gauche et à droite, étant donné qu'ici $\displaystyle \hat m_k = \frac{f(t_k)+f(t_{k+1})}{2}$

Sur le segment $[a, b]$ , il vient
$\displaystyle I_t = \frac{b-a}{n} \sum_{k=0}^{n-1} \frac{f(t_k)+f(t_{k+1})}{2}$
Comme mentionné précédemment, $\displaystyle I_t = \frac{I_{r, g}+I_{r, d}}{2}$
On remarque ici que les valeurs de $f$ en chacun des points intermédiaires comptent $2$ fois plus que les valeurs de $f$ en $a$ et en $b$ , car
$\displaystyle \frac{b-a}{n} \sum_{k=0}^{n-1} \frac{f(t_k)+f(t_{k+1})}{2} = \frac{b-a}{n} \left( \frac{f(a)}{2} + \sum_{k=1}^{n-1} f(t_k) + \frac{f(b)}{2} \right)$

### Méthode du point milieu

Dans la méthode du point milieu, $m_k$ est approchée par la valeur de $f$ au milieu du segment $J_k$ comme son nom l'indique, c'est-à-dire $\hat m_k = f(t_{k+\frac{1}{2}})$ en introduisant la notation $t_{k+\frac{1}{2}} = \displaystyle\frac{t_k+{t_{k+1}}}{2}$

L'approximation de l'intégrale sur le segment $[a, b]$ est donc
$\displaystyle I_{pm} = \frac{b-a}{n} \sum_{k = 0}^{n-1} f(t_{k+\frac{1}{2}})$

### Méthodes de Simpson et de Newton-Cotes

À venir.

## Application sur des fonctions usuelles

### Fonction polynomiale de degré 2

À venir.

### Fonction exponentielle

À venir.

### Fonction sinusoïdale

À venir.