# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2753
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ReferencePortfolioConstituent(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'instrument_identifiers': 'dict(str, str)',
        'instrument_uid': 'str',
        'currency': 'str',
        'properties': 'dict(str, PerpetualProperty)',
        'weight': 'float',
        'floating_weight': 'float'
    }

    attribute_map = {
        'instrument_identifiers': 'instrumentIdentifiers',
        'instrument_uid': 'instrumentUid',
        'currency': 'currency',
        'properties': 'properties',
        'weight': 'weight',
        'floating_weight': 'floatingWeight'
    }

    required_map = {
        'instrument_identifiers': 'optional',
        'instrument_uid': 'required',
        'currency': 'required',
        'properties': 'optional',
        'weight': 'required',
        'floating_weight': 'optional'
    }

    def __init__(self, instrument_identifiers=None, instrument_uid=None, currency=None, properties=None, weight=None, floating_weight=None):  # noqa: E501
        """
        ReferencePortfolioConstituent - a model defined in OpenAPI

        :param instrument_identifiers:  Unique instrument identifiers
        :type instrument_identifiers: dict(str, str)
        :param instrument_uid:  LUSID's internal unique instrument identifier, resolved from the instrument identifiers (required)
        :type instrument_uid: str
        :param currency:  (required)
        :type currency: str
        :param properties:  Properties associated with the constituent
        :type properties: dict[str, lusid.PerpetualProperty]
        :param weight:  (required)
        :type weight: float
        :param floating_weight: 
        :type floating_weight: float

        """  # noqa: E501

        self._instrument_identifiers = None
        self._instrument_uid = None
        self._currency = None
        self._properties = None
        self._weight = None
        self._floating_weight = None
        self.discriminator = None

        self.instrument_identifiers = instrument_identifiers
        self.instrument_uid = instrument_uid
        self.currency = currency
        self.properties = properties
        self.weight = weight
        self.floating_weight = floating_weight

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this ReferencePortfolioConstituent.  # noqa: E501

        Unique instrument identifiers  # noqa: E501

        :return: The instrument_identifiers of this ReferencePortfolioConstituent.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this ReferencePortfolioConstituent.

        Unique instrument identifiers  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this ReferencePortfolioConstituent.  # noqa: E501
        :type: dict(str, str)
        """

        self._instrument_identifiers = instrument_identifiers

    @property
    def instrument_uid(self):
        """Gets the instrument_uid of this ReferencePortfolioConstituent.  # noqa: E501

        LUSID's internal unique instrument identifier, resolved from the instrument identifiers  # noqa: E501

        :return: The instrument_uid of this ReferencePortfolioConstituent.  # noqa: E501
        :rtype: str
        """
        return self._instrument_uid

    @instrument_uid.setter
    def instrument_uid(self, instrument_uid):
        """Sets the instrument_uid of this ReferencePortfolioConstituent.

        LUSID's internal unique instrument identifier, resolved from the instrument identifiers  # noqa: E501

        :param instrument_uid: The instrument_uid of this ReferencePortfolioConstituent.  # noqa: E501
        :type: str
        """
        if instrument_uid is None:
            raise ValueError("Invalid value for `instrument_uid`, must not be `None`")  # noqa: E501

        self._instrument_uid = instrument_uid

    @property
    def currency(self):
        """Gets the currency of this ReferencePortfolioConstituent.  # noqa: E501


        :return: The currency of this ReferencePortfolioConstituent.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ReferencePortfolioConstituent.


        :param currency: The currency of this ReferencePortfolioConstituent.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def properties(self):
        """Gets the properties of this ReferencePortfolioConstituent.  # noqa: E501

        Properties associated with the constituent  # noqa: E501

        :return: The properties of this ReferencePortfolioConstituent.  # noqa: E501
        :rtype: dict(str, PerpetualProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ReferencePortfolioConstituent.

        Properties associated with the constituent  # noqa: E501

        :param properties: The properties of this ReferencePortfolioConstituent.  # noqa: E501
        :type: dict(str, PerpetualProperty)
        """

        self._properties = properties

    @property
    def weight(self):
        """Gets the weight of this ReferencePortfolioConstituent.  # noqa: E501


        :return: The weight of this ReferencePortfolioConstituent.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ReferencePortfolioConstituent.


        :param weight: The weight of this ReferencePortfolioConstituent.  # noqa: E501
        :type: float
        """
        if weight is None:
            raise ValueError("Invalid value for `weight`, must not be `None`")  # noqa: E501

        self._weight = weight

    @property
    def floating_weight(self):
        """Gets the floating_weight of this ReferencePortfolioConstituent.  # noqa: E501


        :return: The floating_weight of this ReferencePortfolioConstituent.  # noqa: E501
        :rtype: float
        """
        return self._floating_weight

    @floating_weight.setter
    def floating_weight(self, floating_weight):
        """Sets the floating_weight of this ReferencePortfolioConstituent.


        :param floating_weight: The floating_weight of this ReferencePortfolioConstituent.  # noqa: E501
        :type: float
        """

        self._floating_weight = floating_weight

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReferencePortfolioConstituent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
