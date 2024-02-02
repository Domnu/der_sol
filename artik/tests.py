from django.test import TestCase
from .models import PageWeb


class PageWebTestCase(TestCase):
    def setUp(self):
        PageWeb.objects.create(url='https://example1.com', contenu='Contenu de la première page.')
        PageWeb.objects.create(url='https://example2.com', contenu='Contenu de la deuxième page.')

    def test_recherche_page_web(self):
        # Votre test ici
        # Récupérez une instance de PageWeb par URL
        page1 = PageWeb.objects.get(url='https://example1.com')
        page2 = PageWeb.objects.get(url='https://example2.com')

        # Vérifiez que le contenu est correct pour chaque page
        self.assertEqual(page1.contenu, 'Contenu de la première page.')
        self.assertEqual(page2.contenu, 'Contenu de la deuxième page.')

        # Vous pouvez ajouter d'autres assertions pour effectuer d'autres tests

        # Par exemple, testez que la page 1 a une URL valide
        self.assertTrue(page1.url.startswith('https://'))

        # Ou testez que la page 2 n'a pas de contenu vide
        self.assertNotEqual(page2.contenu, '')

        # Vous pouvez ajouter autant de tests que nécessaire pour vos besoins

        # Assurez-vous d'exécuter les tests en utilisant la commande `python manage.py test`


if __name__ == '__main__':
    p = PageWebTestCase()
    q = p.test_recherche_page_web

    print('Lin 21 - p =', p)
    print('Lin 22 - q =', q)

p = PageWebTestCase()
q = p.test_recherche_page_web

print('Lin 28 - p =', p)
print('Lin 29 - q =', q)
