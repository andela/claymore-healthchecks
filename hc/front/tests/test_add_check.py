from hc.api.models import Check
from hc.test import BaseTestCase


class AddCheckTestCase(BaseTestCase):

    def test_it_works(self):
        url = "/checks/add/"
        self.client.login(username="alice@example.org", password="password")
        r = self.client.post(url)
        self.assertRedirects(r, "/checks/")
        assert Check.objects.count() == 1

    def test_team_access_works(self):
        url = "/checks/add/"
        self.client.login(username="alice@example.org", password="password")
        self.client.post(url)
        check = Check.objects.filter()
        check_code = list(check)[0].code

        url = "/checks/"
        self.client.login(username="bob@example.org", password="password")
        response = self.client.post(url)
        self.assertIn(str(check_code), response.content.decode('utf-8'))
