from views.view import View


class Input:

    """
        Classe qui gère toutes les entrées utilisateur.
    """

    def __init__(self):
        self.view = View()
        self.display_info = {"error": "L'information n'est pas valide :"}

    def get_input_str(self):

        """
            Méthode qui gère toutes les valeurs de type
            'str' demandées à l'utilisateur.
            Renvoie une valeur de type 'str'.
        """

        while True:
            try:
                value = str(input("--> "))
                break
            except ValueError:
                self.view.show(self.display_info["error"])
        return value.capitalize()
