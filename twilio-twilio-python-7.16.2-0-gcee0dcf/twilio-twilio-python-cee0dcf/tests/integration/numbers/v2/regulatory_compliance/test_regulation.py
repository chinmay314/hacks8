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


class RegulationTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.numbers.v2.regulatory_compliance \
                                  .regulations.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "results": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations?IsoCountry=US&EndUserType=business&NumberType=mobile&PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations?IsoCountry=US&EndUserType=business&NumberType=mobile&PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "results"
                }
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .regulations.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "results": [
                    {
                        "sid": "RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "Australia: Local - Individual",
                        "iso_country": "AU",
                        "number_type": "local",
                        "end_user_type": "individual",
                        "requirements": {
                            "end_user": [
                                {
                                    "name": "Individual",
                                    "type": "individual",
                                    "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations/individual",
                                    "fields": [
                                        "first_name",
                                        "last_name"
                                    ]
                                }
                            ],
                            "supporting_document": [
                                [
                                    {
                                        "name": "Address",
                                        "type": "document",
                                        "description": "The physical location of the individual or business. Must be within locality or region covered by the phone numbers prefix; a PO Box is not acceptable where a local address is required.",
                                        "accepted_documents": [
                                            {
                                                "name": "Address Validation",
                                                "type": "address",
                                                "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/DocumentTypes/address",
                                                "fields": []
                                            }
                                        ]
                                    }
                                ]
                            ]
                        },
                        "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations/RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "results"
                }
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .regulations.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.numbers.v2.regulatory_compliance \
                                  .regulations("RNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations/RNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "Australia: Local - Individual",
                "iso_country": "AU",
                "number_type": "local",
                "end_user_type": "individual",
                "requirements": {
                    "end_user": [
                        {
                            "name": "Individual",
                            "type": "individual",
                            "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations/individual",
                            "fields": [
                                "first_name",
                                "last_name"
                            ]
                        }
                    ],
                    "supporting_document": [
                        [
                            {
                                "name": "Address",
                                "type": "document",
                                "description": "The physical location of the individual or business. Must be within locality or region covered by the phone numbers prefix; a PO Box is not acceptable where a local address is required.",
                                "accepted_documents": [
                                    {
                                        "name": "Address Validation",
                                        "type": "address",
                                        "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/DocumentTypes/address",
                                        "fields": []
                                    }
                                ]
                            }
                        ]
                    ]
                },
                "url": "https://numbers.twilio.com/v2/RegulatoryCompliance/Regulations/RNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.numbers.v2.regulatory_compliance \
                                       .regulations("RNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)
