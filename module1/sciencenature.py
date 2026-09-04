def energie_kinetique(masse, vitesse):
    """
    La fonction calcule l'énergie cinétique d'un objet en mouvement.
    e = 1/2(masse * vitesse^2)
    masse : La masse de l'objet en kilogrammes.
    vitesse : La vitesse de l'objet en mètres par seconde.
    retourne : L'énergie cinétique en joules.
    """
    e = masse * vitesse ** 2 * 1/2 
    return e