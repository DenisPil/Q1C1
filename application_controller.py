from views.home_menu_view import HomeMenuView
from utils.menus import Menu
from controllers.property_controller import PropertyController


class ApplicationController:

    """
        Contrôleur principal de l'application qui déclenche toutes les étapes
    """

    def __init__(self):
        self.controller = None
        self.choice = 0

    def start(self):
        """
         Méthode qui gère la navigation dans le menu.
         Créer l'instance de mes contrôleurs en "cascade".
        """
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()


class HomeMenuController:

    """
        Affiche le menu principal et demande à
        l'utilisateur de choisir une option
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):

        """
            Méthode qui ajoute les entrées au menu de cette classe.
            Affiche le menu et demande à l'utilisateur de choisir une option.
            Renvoie l'instance du contrôleur choisi par l'utilisateur
        """

        self.menu.header("_________________________________", "")
        self.menu.header("Menu", "Principal.")
        self.menu.add("auto", "Afficher les immeubles.",
                      ShowAllPropertiesMenuController)
        self.menu.add("auto", "Recherche.", PropertySearchMenuController)
        self.menu.add("auto", "Charger les données.", LoadIntoBdd)
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class ShowAllPropertiesMenuController:
    """
        Contrôleur qui permet d'afficher
        toutes les propriétés.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.property_controller = PropertyController()

    def __call__(self):

        self.property_controller.display_property_from_csv()
        self.menu.header("_________________________________", "")
        self.menu.header("Menu", "Afficher les immeubles.")
        self.menu.add("auto", "Recherche.", PropertySearchMenuController)
        self.menu.add("auto", "Charger les données.", LoadIntoBdd)
        self.menu.add("auto", "Retour au menu.", HomeMenuController)
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class PropertySearchMenuController():
    """
        Contrôleur qui permet de choisir avec quel information
        on va trouver une propriété.
    """

    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.property_controller = PropertyController()

    def __call__(self):
        self.menu.header("_________________________________", "")
        self.menu.header("Menu", "Recherche.")
        self.menu.add("auto", "building_id",
                      FindPropertyController)
        self.menu.add("auto", "property",
                      FindPropertyController)
        self.menu.add("auto", "firstname",
                      FindPropertyController)
        self.menu.add("auto", "lastname",
                      FindPropertyController)
        self.menu.add("auto", "email",
                      FindPropertyController)
        self.menu.add("auto", "street1",
                      FindPropertyController)
        self.menu.add("auto", "city",
                      FindPropertyController)
        self.menu.add("auto", "zip",
                      FindPropertyController)
        self.menu.add("auto", "owner_acquisition_date",
                      FindPropertyController)
        self.menu.add("auto", "Afficher les immeubles.",
                      ShowAllPropertiesMenuController)
        self.menu.add("auto", "Charger les données.", LoadIntoBdd)
        self.menu.add("auto", "Retour au menu.", HomeMenuController)
        user_choice = self.view.get_user_choice()
        ApplicationController.choice = user_choice
        return user_choice.handler


class FindPropertyController():
    """
        Contrôleur qui permet de chercher
        des propriétés.
    """
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.property_controller = PropertyController()

    def __call__(self):
        choice = ApplicationController.choice
        self.property_controller.find_property_from_csv(str(choice))
        self.menu.add("auto", "Afficher les immeubles.",
                      ShowAllPropertiesMenuController)
        self.menu.add("auto", "Charger les données.", LoadIntoBdd)
        self.menu.add("auto", "Retour au menu.", HomeMenuController)
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class LoadIntoBdd():
    """
        Contrôleur qui permet de sauvegarder
        toutes les propriétés dans la base de donée.
    """
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
        self.property_controller = PropertyController()

    def __call__(self):
        self.property_controller.add_properties_to_bdd()
        self.menu.add("auto", "Afficher les immeubles.",
                      ShowAllPropertiesMenuController)
        self.menu.add("auto", "Recherche.", PropertySearchMenuController)
        self.menu.add("auto", "Retour au menu.", HomeMenuController)
        user_choice = self.view.get_user_choice()
        return user_choice.handler
