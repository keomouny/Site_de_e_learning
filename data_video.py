import logging


class DataVideo:

    def __init__(self):
        self.data = self.get_data()

    def get_data(self):
        logging.info('instanciation DataVideo class et get data')
        try:
            return [
                ('<iframe width = "560" height = "315" src = "https://www.youtube.com/embed/bd0fwri-0No" frameborder = "0" allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen > </iframe >',
                 'ECMAScript 6 - 1 - Introduction(Tutoriel Français)', 'les teachers du net', '6m04', 9008, 'javascript'),
                ('<iframe width = "560" height = "315" src = "https://www.youtube.com/embed/1ODCRIsktWE" frameborder = "0" allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen > </iframe >',
                 'ECMAScript 6 - 2 - Compatibilité au niveau des différents navigateurs(Tutoriel Français)', 'les teachers du net', '1m43', 2723, 'javascript'),
                ('<iframe width="560" height="315" src="https://www.youtube.com/embed/63s2BNrL0IQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
                 'ECMAScript 6 - 3 - Le transcompilateur Babel', 'les teachers du net', '1m19', 2375, 'javascript'),
                ('<iframe width="560" height="315" src="https://www.youtube.com/embed/oUJolR5bX6g" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
                 'APPRENDRE LE PYTHON #1 ? LES BASES & PREREQUIS', 'Graven - Développement', '9m26', 9008, 'python'),
                ('<iframe width="560" height="315" src="https://www.youtube.com/embed/psaDHhZ0cPs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
                 'Learn Python - Full Course for Beginners [Tutorial]', 'freeCodeCamp.org', '4h26m56', 2723, 'python'),
                ('<iframe width="560" height="315" src="https://www.youtube.com/embed/VmOPhT4HFNE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
                 '5 mini-projets python pour les débutants', 'FORMASYS', '1h13m08', 2375, 'python'),
                ('<iframe width="560" height="315" src="https://www.youtube.com/embed/SXB6KJ4u5vg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
                 'Docker: Débuter de zéro avec Docker en français - Tutoriel 1/3', 'cocadmin', '5min', 76571, 'docker'),
                ('<iframe width="560" height="315" src="https://www.youtube.com/embed/cWkmqZPWwiw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
                 'Apprendre Docker #2 - Créer ses propres images Docker', 'cocadmin', '7min19', 45751, 'docker'),
                ('<iframe width="560" height="315" src="https://www.youtube.com/embed/dWcoIxRfs8Y" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
                 'Déployer une app avec Docker compose - Apprendre Docker  # 3', 'cocadmin', '7min46', 28822, 'docker')
            ]
        except Exception as e:
            logging.error("error lors de l'insertion")
