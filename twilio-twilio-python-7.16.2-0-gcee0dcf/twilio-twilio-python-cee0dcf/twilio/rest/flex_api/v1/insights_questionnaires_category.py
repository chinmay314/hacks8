# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class InsightsQuestionnairesCategoryList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the InsightsQuestionnairesCategoryList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryList
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryList
        """
        super(InsightsQuestionnairesCategoryList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Insights/QM/Categories'.format(**self._solution)

    def create(self, name, token=values.unset):
        """
        Create the InsightsQuestionnairesCategoryInstance

        :param unicode name: The category name.
        :param unicode token: The Token HTTP request header

        :returns: The created InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        """
        data = values.of({'Name': name, })
        headers = values.of({'Token': token, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers, )

        return InsightsQuestionnairesCategoryInstance(self._version, payload, )

    def get(self, category_id):
        """
        Constructs a InsightsQuestionnairesCategoryContext

        :param category_id: Category ID to update

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryContext
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryContext
        """
        return InsightsQuestionnairesCategoryContext(self._version, category_id=category_id, )

    def __call__(self, category_id):
        """
        Constructs a InsightsQuestionnairesCategoryContext

        :param category_id: Category ID to update

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryContext
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryContext
        """
        return InsightsQuestionnairesCategoryContext(self._version, category_id=category_id, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesCategoryList>'


class InsightsQuestionnairesCategoryPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the InsightsQuestionnairesCategoryPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryPage
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryPage
        """
        super(InsightsQuestionnairesCategoryPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of InsightsQuestionnairesCategoryInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        """
        return InsightsQuestionnairesCategoryInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesCategoryPage>'


class InsightsQuestionnairesCategoryContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, category_id):
        """
        Initialize the InsightsQuestionnairesCategoryContext

        :param Version version: Version that contains the resource
        :param category_id: Category ID to update

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryContext
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryContext
        """
        super(InsightsQuestionnairesCategoryContext, self).__init__(version)

        # Path Solution
        self._solution = {'category_id': category_id, }
        self._uri = '/Insights/QM/Categories/{category_id}'.format(**self._solution)

    def update(self, name, token=values.unset):
        """
        Update the InsightsQuestionnairesCategoryInstance

        :param unicode name: The category name.
        :param unicode token: The Token HTTP request header

        :returns: The updated InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        """
        data = values.of({'Name': name, })
        headers = values.of({'Token': token, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers, )

        return InsightsQuestionnairesCategoryInstance(
            self._version,
            payload,
            category_id=self._solution['category_id'],
        )

    def delete(self, token=values.unset):
        """
        Deletes the InsightsQuestionnairesCategoryInstance

        :param unicode token: The Token HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'Token': token, })

        return self._version.delete(method='DELETE', uri=self._uri, headers=headers, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesCategoryContext {}>'.format(context)


class InsightsQuestionnairesCategoryInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, category_id=None):
        """
        Initialize the InsightsQuestionnairesCategoryInstance

        :returns: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        """
        super(InsightsQuestionnairesCategoryInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'category_id': payload.get('category_id'),
            'name': payload.get('name'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'category_id': category_id or self._properties['category_id'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: InsightsQuestionnairesCategoryContext for this InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryContext
        """
        if self._context is None:
            self._context = InsightsQuestionnairesCategoryContext(
                self._version,
                category_id=self._solution['category_id'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource and owns this Flex Insights
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def category_id(self):
        """
        :returns: Unique category ID
        :rtype: unicode
        """
        return self._properties['category_id']

    @property
    def name(self):
        """
        :returns: The category name.
        :rtype: unicode
        """
        return self._properties['name']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def update(self, name, token=values.unset):
        """
        Update the InsightsQuestionnairesCategoryInstance

        :param unicode name: The category name.
        :param unicode token: The Token HTTP request header

        :returns: The updated InsightsQuestionnairesCategoryInstance
        :rtype: twilio.rest.flex_api.v1.insights_questionnaires_category.InsightsQuestionnairesCategoryInstance
        """
        return self._proxy.update(name, token=token, )

    def delete(self, token=values.unset):
        """
        Deletes the InsightsQuestionnairesCategoryInstance

        :param unicode token: The Token HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(token=token, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsQuestionnairesCategoryInstance {}>'.format(context)
