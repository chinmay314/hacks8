# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class OauthTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.oauth.v1.oauth().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://oauth.twilio.com/v1/certs',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "keys": [
                    {
                        "alg": "ES256",
                        "kid": "IC10c8172f35dd36f20d9ed2fcc0b818c7",
                        "key_ops": [],
                        "use": "sig",
                        "crv": "P-256",
                        "x": "hrJ4NKauVYBiREgIY_EPPj10zHIiOHeIf3-LGODt_KM",
                        "y": "c3IcyhpvfMIMpqd_ku9Q_4n20nMlelUF-zSmRXEIFEU",
                        "kty": "EC"
                    }
                ],
                "url": "https://oauth.twilio.com/v1/certs"
            }
            '''
        ))

        actual = self.client.oauth.v1.oauth().fetch()

        self.assertIsNotNone(actual)
