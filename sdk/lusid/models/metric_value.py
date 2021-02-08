# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2568
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class MetricValue(object):
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
        'value': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'value': 'value',
        'unit': 'unit'
    }

    required_map = {
        'value': 'optional',
        'unit': 'optional'
    }

    def __init__(self, value=None, unit=None):  # noqa: E501
        """
        MetricValue - a model defined in OpenAPI

        :param value:  The numerical value of the property.
        :type value: float
        :param unit: 
        :type unit: str

        """  # noqa: E501

        self._value = None
        self._unit = None
        self.discriminator = None

        if value is not None:
            self.value = value
        self.unit = unit

    @property
    def value(self):
        """Gets the value of this MetricValue.  # noqa: E501

        The numerical value of the property.  # noqa: E501

        :return: The value of this MetricValue.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MetricValue.

        The numerical value of the property.  # noqa: E501

        :param value: The value of this MetricValue.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def unit(self):
        """Gets the unit of this MetricValue.  # noqa: E501


        :return: The unit of this MetricValue.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this MetricValue.


        :param unit: The unit of this MetricValue.  # noqa: E501
        :type: str
        """

        self._unit = unit

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
        if not isinstance(other, MetricValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
