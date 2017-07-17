from hc.api.models import Check
from hc.test import BaseTestCase


class AddCheckTestCase(BaseTestCase):

    def test_it_works(self):
        url = "/checks/add/"
        self.client.login(username="alice@example.org", password="password")
        r = self.client.post(url)
        self.assertRedirects(r, "/checks/")
        assert Check.objects.count() == 1

<<<<<<< HEAD
    ### Test that team access works
=======
    def test_team_access_works(self):
        ### Test that team access works

        url = "/checks/add/"
        self.client.login(username="alice@example.org", password="password")
        self.client.post(url)
        check = Check.objects.first()
        check_code = check.code

        url = "/checks/"
        self.client.login(username="bob@example.org", password="password")
        response = self.client.post(url)
        self.assertIn(str(check_code), response.content.decode('utf-8'))
>>>>>>> develop
