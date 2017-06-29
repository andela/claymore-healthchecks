from django.conf import settings
from django.core.signing import base64_hmac

from hc.api.models import Check
from hc.test import BaseTestCase


class BadgeTestCase(BaseTestCase):

    def setUp(self):
        super(BadgeTestCase, self).setUp()
        self.check = Check.objects.create(user=self.alice, tags="foo bar")

    def test_it_rejects_bad_signature(self):
        response = self.client.get("/badge/%s/12345678/foo.svg" % self.alice.username)
        ### Assert the expected response status code
        self.assertEqual(400, response.status_code, msg='should return 404 error on bad signature')

    def test_it_returns_svg(self):
        sign = base64_hmac(str(self.alice.username), "foo", settings.SECRET_KEY)
        sign = sign[:8].decode("utf-8")
        url = "/badge/%s/%s/foo.svg" % (self.alice.username, sign)
        response = self.client.get(url)

        ### Assert that the svg is returned
        self.assertIn('foo', response.content.decode("utf-8"))


