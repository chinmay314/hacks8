# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.api.v2010.account.message.feedback import FeedbackList
from twilio.rest.api.v2010.account.message.media import MediaList


class MessageList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the MessageList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource

        :returns: twilio.rest.api.v2010.account.message.MessageList
        :rtype: twilio.rest.api.v2010.account.message.MessageList
        """
        super(MessageList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, }
        self._uri = '/Accounts/{account_sid}/Messages.json'.format(**self._solution)

    def create(self, to, status_callback=values.unset, application_sid=values.unset,
               max_price=values.unset, provide_feedback=values.unset,
               attempt=values.unset, validity_period=values.unset,
               force_delivery=values.unset, content_retention=values.unset,
               address_retention=values.unset, smart_encoded=values.unset,
               persistent_action=values.unset, shorten_urls=values.unset,
               schedule_type=values.unset, send_at=values.unset,
               send_as_mms=values.unset, content_sid=values.unset,
               content_variables=values.unset, from_=values.unset,
               messaging_service_sid=values.unset, body=values.unset,
               media_url=values.unset):
        """
        Create the MessageInstance

        :param unicode to: The destination phone number
        :param unicode status_callback: The URL we should call to send status information to your application
        :param unicode application_sid: The application to use for callbacks
        :param unicode max_price: The total maximum price up to 4 decimal places in US dollars acceptable for the message to be delivered.
        :param bool provide_feedback: Whether to confirm delivery of the message
        :param unicode attempt: Total numer of attempts made , this inclusive to send out the message
        :param unicode validity_period: The number of seconds that the message can remain in our outgoing queue.
        :param bool force_delivery: Reserved
        :param MessageInstance.ContentRetention content_retention: Determines if the message content can be stored or redacted based on privacy settings
        :param MessageInstance.AddressRetention address_retention: Determines if the address can be stored or obfuscated based on privacy settings
        :param bool smart_encoded: Whether to detect Unicode characters that have a similar GSM-7 character and replace them
        :param list[unicode] persistent_action: Rich actions for Channels Messages.
        :param bool shorten_urls: Sets whether to shorten and track links included in the body of this message.
        :param MessageInstance.ScheduleType schedule_type: Pass the value `fixed` to schedule a message at a fixed time.
        :param datetime send_at: The time that Twilio will send the message. Must be in ISO 8601 format.
        :param bool send_as_mms: If set to True, Twilio will deliver the message as a single MMS message, regardless of the presence of media.
        :param unicode content_sid: The SID of the preconfigured Content object you want to associate with the message.
        :param unicode content_variables: Key-value pairs of variable names to substitution values, used alongside a content_sid.
        :param unicode from_: The phone number that initiated the message
        :param unicode messaging_service_sid: The SID of the Messaging Service you want to associate with the message.
        :param unicode body: The text of the message you want to send. Can be up to 1,600 characters in length.
        :param list[unicode] media_url: The URL of the media to send with the message

        :returns: The created MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageInstance
        """
        data = values.of({
            'To': to,
            'From': from_,
            'MessagingServiceSid': messaging_service_sid,
            'Body': body,
            'MediaUrl': serialize.map(media_url, lambda e: e),
            'StatusCallback': status_callback,
            'ApplicationSid': application_sid,
            'MaxPrice': max_price,
            'ProvideFeedback': provide_feedback,
            'Attempt': attempt,
            'ValidityPeriod': validity_period,
            'ForceDelivery': force_delivery,
            'ContentRetention': content_retention,
            'AddressRetention': address_retention,
            'SmartEncoded': smart_encoded,
            'PersistentAction': serialize.map(persistent_action, lambda e: e),
            'ShortenUrls': shorten_urls,
            'ScheduleType': schedule_type,
            'SendAt': serialize.iso8601_datetime(send_at),
            'SendAsMms': send_as_mms,
            'ContentSid': content_sid,
            'ContentVariables': content_variables,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return MessageInstance(self._version, payload, account_sid=self._solution['account_sid'], )

    def stream(self, to=values.unset, from_=values.unset,
               date_sent_before=values.unset, date_sent=values.unset,
               date_sent_after=values.unset, limit=None, page_size=None):
        """
        Streams MessageInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode to: Filter by messages sent to this number
        :param unicode from_: Filter by from number
        :param datetime date_sent_before: Filter by date sent
        :param datetime date_sent: Filter by date sent
        :param datetime date_sent_after: Filter by date sent
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.message.MessageInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            to=to,
            from_=from_,
            date_sent_before=date_sent_before,
            date_sent=date_sent,
            date_sent_after=date_sent_after,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'])

    def list(self, to=values.unset, from_=values.unset,
             date_sent_before=values.unset, date_sent=values.unset,
             date_sent_after=values.unset, limit=None, page_size=None):
        """
        Lists MessageInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode to: Filter by messages sent to this number
        :param unicode from_: Filter by from number
        :param datetime date_sent_before: Filter by date sent
        :param datetime date_sent: Filter by date sent
        :param datetime date_sent_after: Filter by date sent
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.message.MessageInstance]
        """
        return list(self.stream(
            to=to,
            from_=from_,
            date_sent_before=date_sent_before,
            date_sent=date_sent,
            date_sent_after=date_sent_after,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, to=values.unset, from_=values.unset,
             date_sent_before=values.unset, date_sent=values.unset,
             date_sent_after=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of MessageInstance records from the API.
        Request is executed immediately

        :param unicode to: Filter by messages sent to this number
        :param unicode from_: Filter by from number
        :param datetime date_sent_before: Filter by date sent
        :param datetime date_sent: Filter by date sent
        :param datetime date_sent_after: Filter by date sent
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessagePage
        """
        data = values.of({
            'To': to,
            'From': from_,
            'DateSent<': serialize.iso8601_datetime(date_sent_before),
            'DateSent': serialize.iso8601_datetime(date_sent),
            'DateSent>': serialize.iso8601_datetime(date_sent_after),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return MessagePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MessageInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessagePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return MessagePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a MessageContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.message.MessageContext
        :rtype: twilio.rest.api.v2010.account.message.MessageContext
        """
        return MessageContext(self._version, account_sid=self._solution['account_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a MessageContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.message.MessageContext
        :rtype: twilio.rest.api.v2010.account.message.MessageContext
        """
        return MessageContext(self._version, account_sid=self._solution['account_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MessageList>'


class MessagePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MessagePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The SID of the Account that created the resource

        :returns: twilio.rest.api.v2010.account.message.MessagePage
        :rtype: twilio.rest.api.v2010.account.message.MessagePage
        """
        super(MessagePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MessageInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.message.MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageInstance
        """
        return MessageInstance(self._version, payload, account_sid=self._solution['account_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MessagePage>'


class MessageContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        """
        Initialize the MessageContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource to fetch
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.message.MessageContext
        :rtype: twilio.rest.api.v2010.account.message.MessageContext
        """
        super(MessageContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'sid': sid, }
        self._uri = '/Accounts/{account_sid}/Messages/{sid}.json'.format(**self._solution)

        # Dependents
        self._media = None
        self._feedback = None

    def delete(self):
        """
        Deletes the MessageInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def fetch(self):
        """
        Fetch the MessageInstance

        :returns: The fetched MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MessageInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def update(self, body=values.unset, status=values.unset):
        """
        Update the MessageInstance

        :param unicode body: The text of the message you want to send
        :param MessageInstance.UpdateStatus status: Set as `canceled` to cancel a message from being sent.

        :returns: The updated MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageInstance
        """
        data = values.of({'Body': body, 'Status': status, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return MessageInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    @property
    def media(self):
        """
        Access the media

        :returns: twilio.rest.api.v2010.account.message.media.MediaList
        :rtype: twilio.rest.api.v2010.account.message.media.MediaList
        """
        if self._media is None:
            self._media = MediaList(
                self._version,
                account_sid=self._solution['account_sid'],
                message_sid=self._solution['sid'],
            )
        return self._media

    @property
    def feedback(self):
        """
        Access the feedback

        :returns: twilio.rest.api.v2010.account.message.feedback.FeedbackList
        :rtype: twilio.rest.api.v2010.account.message.feedback.FeedbackList
        """
        if self._feedback is None:
            self._feedback = FeedbackList(
                self._version,
                account_sid=self._solution['account_sid'],
                message_sid=self._solution['sid'],
            )
        return self._feedback

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.MessageContext {}>'.format(context)


class MessageInstance(InstanceResource):

    class Status(object):
        QUEUED = "queued"
        SENDING = "sending"
        SENT = "sent"
        FAILED = "failed"
        DELIVERED = "delivered"
        UNDELIVERED = "undelivered"
        RECEIVING = "receiving"
        RECEIVED = "received"
        ACCEPTED = "accepted"
        SCHEDULED = "scheduled"
        READ = "read"
        PARTIALLY_DELIVERED = "partially_delivered"
        CANCELED = "canceled"

    class UpdateStatus(object):
        CANCELED = "canceled"

    class Direction(object):
        INBOUND = "inbound"
        OUTBOUND_API = "outbound-api"
        OUTBOUND_CALL = "outbound-call"
        OUTBOUND_REPLY = "outbound-reply"

    class ContentRetention(object):
        RETAIN = "retain"

    class AddressRetention(object):
        RETAIN = "retain"

    class TrafficType(object):
        FREE = "free"

    class ScheduleType(object):
        FIXED = "fixed"

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the MessageInstance

        :returns: twilio.rest.api.v2010.account.message.MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageInstance
        """
        super(MessageInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'body': payload.get('body'),
            'num_segments': payload.get('num_segments'),
            'direction': payload.get('direction'),
            'from_': payload.get('from'),
            'to': payload.get('to'),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'price': payload.get('price'),
            'error_message': payload.get('error_message'),
            'uri': payload.get('uri'),
            'account_sid': payload.get('account_sid'),
            'num_media': payload.get('num_media'),
            'status': payload.get('status'),
            'messaging_service_sid': payload.get('messaging_service_sid'),
            'sid': payload.get('sid'),
            'date_sent': deserialize.rfc2822_datetime(payload.get('date_sent')),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'error_code': deserialize.integer(payload.get('error_code')),
            'price_unit': payload.get('price_unit'),
            'api_version': payload.get('api_version'),
            'subresource_uris': payload.get('subresource_uris'),
        }

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: MessageContext for this MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageContext
        """
        if self._context is None:
            self._context = MessageContext(
                self._version,
                account_sid=self._solution['account_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def body(self):
        """
        :returns: The message text
        :rtype: unicode
        """
        return self._properties['body']

    @property
    def num_segments(self):
        """
        :returns: The number of messages used to deliver the message body
        :rtype: unicode
        """
        return self._properties['num_segments']

    @property
    def direction(self):
        """
        :returns: The direction of the message
        :rtype: MessageInstance.Direction
        """
        return self._properties['direction']

    @property
    def from_(self):
        """
        :returns: The phone number that initiated the message
        :rtype: unicode
        """
        return self._properties['from_']

    @property
    def to(self):
        """
        :returns: The phone number that received the message
        :rtype: unicode
        """
        return self._properties['to']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def price(self):
        """
        :returns: The amount billed for the message
        :rtype: unicode
        """
        return self._properties['price']

    @property
    def error_message(self):
        """
        :returns: The description of the error_code
        :rtype: unicode
        """
        return self._properties['error_message']

    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`
        :rtype: unicode
        """
        return self._properties['uri']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def num_media(self):
        """
        :returns: The number of media files associated with the message
        :rtype: unicode
        """
        return self._properties['num_media']

    @property
    def status(self):
        """
        :returns: The status of the message
        :rtype: MessageInstance.Status
        """
        return self._properties['status']

    @property
    def messaging_service_sid(self):
        """
        :returns: The SID of the Messaging Service used with the message.
        :rtype: unicode
        """
        return self._properties['messaging_service_sid']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def date_sent(self):
        """
        :returns: The RFC 2822 date and time in GMT when the message was sent
        :rtype: datetime
        """
        return self._properties['date_sent']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def error_code(self):
        """
        :returns: The error code associated with the message
        :rtype: unicode
        """
        return self._properties['error_code']

    @property
    def price_unit(self):
        """
        :returns: The currency in which price is measured
        :rtype: unicode
        """
        return self._properties['price_unit']

    @property
    def api_version(self):
        """
        :returns: The API version used to process the message
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def subresource_uris(self):
        """
        :returns: A list of related resources identified by their relative URIs
        :rtype: unicode
        """
        return self._properties['subresource_uris']

    def delete(self):
        """
        Deletes the MessageInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch the MessageInstance

        :returns: The fetched MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageInstance
        """
        return self._proxy.fetch()

    def update(self, body=values.unset, status=values.unset):
        """
        Update the MessageInstance

        :param unicode body: The text of the message you want to send
        :param MessageInstance.UpdateStatus status: Set as `canceled` to cancel a message from being sent.

        :returns: The updated MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageInstance
        """
        return self._proxy.update(body=body, status=status, )

    @property
    def media(self):
        """
        Access the media

        :returns: twilio.rest.api.v2010.account.message.media.MediaList
        :rtype: twilio.rest.api.v2010.account.message.media.MediaList
        """
        return self._proxy.media

    @property
    def feedback(self):
        """
        Access the feedback

        :returns: twilio.rest.api.v2010.account.message.feedback.FeedbackList
        :rtype: twilio.rest.api.v2010.account.message.feedback.FeedbackList
        """
        return self._proxy.feedback

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.MessageInstance {}>'.format(context)
