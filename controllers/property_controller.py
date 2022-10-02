from utils.menus import Menu
from views.home_menu_view import HomeMenuView
from views.view import View
from views.grab import Input
import csv
import os
import sys


class PropertyController:

    """
        Création de l'instance de propriété.
    """
    def __init__(self):
        self.property = None
        self.view = View()
        self.input = Input()
        self.menu = Menu()
        self.view_menu = HomeMenuView(self.menu)

        self.display_info = "tapez l'information :"

    def display_property_from_csv(self):
        """
            Méthode qui récupére la liste des biens immobiliers.
        """
        rez = list()
        initial_count = 0
        dir = "C:/OpenClassrooms/exo_q1c1/data"
        for path in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, path)):
                initial_count += 1
        for i in range(0, initial_count - 1):
            f = open(r'C:/OpenClassrooms/exo_q1c1/data/dataset_' +
                     str(i) + '.csv', newline='')
            myReader = csv.reader(f,)
            for row in myReader:
                if not row:
                    pass
                elif row[0] == 'property':
                    pass
                else:
                    rez.append(row)
        sort_list = sorted(rez, key=lambda x: (x[1], x[6]))
        for elem in sort_list:
            (property, building_id, owner_acquisition_date, street1, city, zip,
             lastname, firstname, email) = elem
            print("{:<6}{:<6}{:<12}{:<31}{:<25}{:<7}{:<25}{:<24}{:<6}".format(
                property, building_id, owner_acquisition_date, street1, city,
                zip, lastname, firstname, email))
        return sort_list

    def find_property_from_csv(self, choice):

        """
            Méthode qui récupére un ou des biens immobiliers selon critère.
        """

        rez = list()
        self.view.show("Tape le " + choice)
        info = self.input.get_input_str()
        initial_count = 0
        dir = "C:/OpenClassrooms/exo_q1c1/data"
        for path in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, path)):
                initial_count += 1
        for i in range(0, initial_count - 1):
            f = open(r'C:/OpenClassrooms/exo_q1c1/data/dataset_' +
                     str(i) + '.csv', newline='')
            myReader = csv.DictReader(f,)
            for row in myReader:
                if row[str(choice)] == info:
                    row.update({'files': 'dataset_' +
                                str(i) + '.csv'})
                    rez.append(row)
        for i in rez:
            print()
            for key, item in i.items():
                print(key, ":", item)
        print()

    def add_properties_to_bdd(self):
        """
            Ajoute les propriétés a la bdd
        """
        sys.path.insert(0, 'C:/OpenClassrooms/exo_q1c1/q1c1')
        sys.path.append("C:/OpenClassrooms/exo_q1c1/q1c1/property")
        import property

        os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'q1c1.settings')
        import django
        django.setup()
        from property.models import Property
        initial_count = 0
        dir = "C:/OpenClassrooms/exo_q1c1/data"
        for path in os.listdir(dir):
            if os.path.isfile(os.path.join(dir, path)):
                initial_count += 1
        for i in range(0, initial_count - 1):
            f = open(r'C:/OpenClassrooms/exo_q1c1/data/dataset_' +
                     str(i) + '.csv', newline='')
            myReader = csv.DictReader(f,)
            print('dataset_' +
                  str(i) + '.csv')
            for row in myReader:
                if not row:
                    pass
                else:
                    instance = Property(property=int(row['property']),
                                        building_id=int(row['building_id']),
                                        owner_acquisition_date=row['owner_acquisition_date'],
                                        street1=row['street1'],
                                        city=row['city'],
                                        zip=int(row['zip']),
                                        last_name=row['lastname'],
                                        first_name=row['firstname'],
                                        email=row['email']
                                        )
                    instance.save()
                    print(instance)
