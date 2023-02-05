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


class MessageTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .messages.create(x_twilio_webhook_enabled="true")

        headers = {'X-Twilio-Webhook-Enabled': "true", }
        self.holodeck.assert_has_request(Request(
            'post',
            'https://conversations.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conversations/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages',
            headers=headers,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "body": "Hello",
                "media": null,
                "author": "message author",
                "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "attributes": "{ \\"importance\\": \\"high\\" }",
                "date_created": "2015-12-16T22:18:37Z",
                "date_updated": "2015-12-16T22:18:38Z",
                "index": 0,
                "delivery": {
                    "total": 2,
                    "sent": "all",
                    "delivered": "some",
                    "read": "some",
                    "failed": "none",
                    "undelivered": "none"
                },
                "content_sid": null,
                "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts"
                }
            }
            '''
        ))

        actual = self.client.conversations.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .messages.create()

        self.assertIsNotNone(actual)

    def test_create_with_media_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "body": null,
                "media": [
                    {
                        "sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "size": 42056,
                        "content_type": "image/jpeg",
                        "filename": "car.jpg"
                    }
                ],
                "author": "message author",
                "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "attributes": "{ \\"importance\\": \\"high\\" }",
                "date_created": "2015-12-16T22:18:37Z",
                "date_updated": "2015-12-16T22:18:38Z",
                "index": 0,
                "delivery": {
                    "total": 2,
                    "sent": "all",
                    "delivered": "some",
                    "read": "some",
                    "failed": "none",
                    "undelivered": "none"
                },
                "content_sid": null,
                "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts"
                }
            }
            '''
        ))

        actual = self.client.conversations.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .messages.create()

        self.assertIsNotNone(actual)

    def test_create_no_attributes_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "body": "Hello",
                "media": null,
                "author": "message author",
                "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "attributes": "{}",
                "date_created": "2020-07-01T22:18:37Z",
                "date_updated": "2020-07-01T22:18:37Z",
                "index": 0,
                "delivery": {
                    "total": 2,
                    "sent": "all",
                    "delivered": "some",
                    "read": "some",
                    "failed": "none",
                    "undelivered": "none"
                },
                "content_sid": null,
                "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts"
                }
            }
            '''
        ))

        actual = self.client.conversations.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .messages.create()

        self.assertIsNotNone(actual)

    def test_create_with_content_sid_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "body": "Hello John",
                "media": null,
                "author": "message author",
                "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "attributes": "{}",
                "date_created": "2015-12-16T22:18:37Z",
                "date_updated": "2015-12-16T22:18:38Z",
                "index": 0,
                "delivery": {
                    "total": 2,
                    "sent": "all",
                    "delivered": "some",
                    "read": "some",
                    "failed": "none",
                    "undelivered": "none"
                },
                "content_sid": "HXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts"
                }
            }
            '''
        ))

        actual = self.client.conversations.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .messages.create()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .messages("IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(x_twilio_webhook_enabled="true")

        headers = {'X-Twilio-Webhook-Enabled': "true", }
        self.holodeck.assert_has_request(Request(
            'post',
            'https://conversations.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conversations/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            headers=headers,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "body": "Hello",
                "media": null,
                "author": "message author",
                "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "attributes": "{ \\"importance\\": \\"high\\" }",
                "date_created": "2015-12-16T22:18:37Z",
                "date_updated": "2015-12-16T22:18:38Z",
                "index": 0,
                "delivery": {
                    "total": 2,
                    "sent": "all",
                    "delivered": "some",
                    "read": "some",
                    "failed": "none",
                    "undelivered": "none"
                },
                "content_sid": null,
                "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts"
                }
            }
            '''
        ))

        actual = self.client.conversations.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .messages("IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .messages("IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete(x_twilio_webhook_enabled="true")

        headers = {'X-Twilio-Webhook-Enabled': "true", }
        self.holodeck.assert_has_request(Request(
            'delete',
            'https://conversations.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conversations/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            headers=headers,
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.conversations.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .messages("IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .messages("IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://conversations.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conversations/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "body": "Welcome!",
                "media": null,
                "author": "system",
                "participant_sid": null,
                "attributes": "{ \\"importance\\": \\"high\\" }",
                "date_created": "2016-03-24T20:37:57Z",
                "date_updated": "2016-03-24T20:37:57Z",
                "index": 0,
                "delivery": {
                    "total": 2,
                    "sent": "all",
                    "delivered": "some",
                    "read": "some",
                    "failed": "none",
                    "undelivered": "none"
                },
                "content_sid": null,
                "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts"
                }
            }
            '''
        ))

        actual = self.client.conversations.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .messages("IMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.conversations.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .messages.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://conversations.twilio.com/v1/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Conversations/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "messages"
                },
                "messages": [
                    {
                        "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "body": "I like pie.",
                        "media": null,
                        "author": "pie_preferrer",
                        "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "attributes": "{ \\"importance\\": \\"high\\" }",
                        "date_created": "2016-03-24T20:37:57Z",
                        "date_updated": "2016-03-24T20:37:57Z",
                        "index": 0,
                        "delivery": {
                            "total": 2,
                            "sent": "all",
                            "delivered": "some",
                            "read": "some",
                            "failed": "none",
                            "undelivered": "none"
                        },
                        "content_sid": null,
                        "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts"
                        }
                    },
                    {
                        "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "body": "Cake is my favorite!",
                        "media": null,
                        "author": "cake_lover",
                        "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "attributes": "{ \\"importance\\": \\"high\\" }",
                        "date_created": "2016-03-24T20:38:21Z",
                        "date_updated": "2016-03-24T20:38:21Z",
                        "index": 0,
                        "delivery": {
                            "total": 2,
                            "sent": "all",
                            "delivered": "some",
                            "read": "some",
                            "failed": "none",
                            "undelivered": "none"
                        },
                        "content_sid": null,
                        "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts"
                        }
                    },
                    {
                        "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "body": null,
                        "media": [
                            {
                                "sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                "size": 42056,
                                "content_type": "image/jpeg",
                                "filename": "car.jpg"
                            }
                        ],
                        "author": "cake_lover",
                        "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "attributes": "{ \\"importance\\": \\"high\\" }",
                        "date_created": "2016-03-24T20:38:21Z",
                        "date_updated": "2016-03-24T20:38:21Z",
                        "index": 0,
                        "delivery": {
                            "total": 2,
                            "sent": "all",
                            "delivered": "some",
                            "read": "some",
                            "failed": "none",
                            "undelivered": "none"
                        },
                        "content_sid": null,
                        "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts"
                        }
                    }
                ]
            }
            '''
        ))

        actual = self.client.conversations.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .messages.list()

        self.assertIsNotNone(actual)

    def test_read_last_message_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 1,
                    "first_page_url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages?Order=desc&PageSize=1&Page=0",
                    "previous_page_url": null,
                    "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages?Order=desc&PageSize=1&Page=0",
                    "next_page_url": null,
                    "key": "messages"
                },
                "messages": [
                    {
                        "sid": "IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "chat_service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "conversation_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "body": null,
                        "media": [
                            {
                                "sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                                "size": 42056,
                                "content_type": "image/jpeg",
                                "filename": "car.jpg"
                            }
                        ],
                        "author": "cake_lover",
                        "participant_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "attributes": "{ \\"importance\\": \\"high\\" }",
                        "date_created": "2016-03-24T20:38:21Z",
                        "date_updated": "2016-03-24T20:38:21Z",
                        "index": 9,
                        "delivery": {
                            "total": 2,
                            "sent": "all",
                            "delivered": "some",
                            "read": "some",
                            "failed": "none",
                            "undelivered": "none"
                        },
                        "content_sid": null,
                        "url": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "delivery_receipts": "https://conversations.twilio.com/v1/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Conversations/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Messages/IMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Receipts"
                        }
                    }
                ]
            }
            '''
        ))

        actual = self.client.conversations.v1.services("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .conversations("CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                             .messages.list()

        self.assertIsNotNone(actual)
