# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2808
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class UpsertQuoteRequest(object):
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
        'quote_id': 'QuoteId',
        'metric_value': 'MetricValue',
        'lineage': 'str',
        'scale_factor': 'float'
    }

    attribute_map = {
        'quote_id': 'quoteId',
        'metric_value': 'metricValue',
        'lineage': 'lineage',
        'scale_factor': 'scaleFactor'
    }

    required_map = {
        'quote_id': 'required',
        'metric_value': 'optional',
        'lineage': 'optional',
        'scale_factor': 'optional'
    }

    def __init__(self, quote_id=None, metric_value=None, lineage=None, scale_factor=None):  # noqa: E501
        """
        UpsertQuoteRequest - a model defined in OpenAPI

        :param quote_id:  (required)
        :type quote_id: lusid.QuoteId
        :param metric_value: 
        :type metric_value: lusid.MetricValue
        :param lineage:  Description of the quote's lineage e.g. 'FundAccountant_GreenQuality'.
        :type lineage: str
        :param scale_factor:  An optional scale factor for non-standard scaling of quotes against the instrument. If not supplied, the default ScaleFactor is 1.
        :type scale_factor: float

        """  # noqa: E501

        self._quote_id = None
        self._metric_value = None
        self._lineage = None
        self._scale_factor = None
        self.discriminator = None

        self.quote_id = quote_id
        if metric_value is not None:
            self.metric_value = metric_value
        self.lineage = lineage
        self.scale_factor = scale_factor

    @property
    def quote_id(self):
        """Gets the quote_id of this UpsertQuoteRequest.  # noqa: E501


        :return: The quote_id of this UpsertQuoteRequest.  # noqa: E501
        :rtype: QuoteId
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """Sets the quote_id of this UpsertQuoteRequest.


        :param quote_id: The quote_id of this UpsertQuoteRequest.  # noqa: E501
        :type: QuoteId
        """
        if quote_id is None:
            raise ValueError("Invalid value for `quote_id`, must not be `None`")  # noqa: E501

        self._quote_id = quote_id

    @property
    def metric_value(self):
        """Gets the metric_value of this UpsertQuoteRequest.  # noqa: E501


        :return: The metric_value of this UpsertQuoteRequest.  # noqa: E501
        :rtype: MetricValue
        """
        return self._metric_value

    @metric_value.setter
    def metric_value(self, metric_value):
        """Sets the metric_value of this UpsertQuoteRequest.


        :param metric_value: The metric_value of this UpsertQuoteRequest.  # noqa: E501
        :type: MetricValue
        """

        self._metric_value = metric_value

    @property
    def lineage(self):
        """Gets the lineage of this UpsertQuoteRequest.  # noqa: E501

        Description of the quote's lineage e.g. 'FundAccountant_GreenQuality'.  # noqa: E501

        :return: The lineage of this UpsertQuoteRequest.  # noqa: E501
        :rtype: str
        """
        return self._lineage

    @lineage.setter
    def lineage(self, lineage):
        """Sets the lineage of this UpsertQuoteRequest.

        Description of the quote's lineage e.g. 'FundAccountant_GreenQuality'.  # noqa: E501

        :param lineage: The lineage of this UpsertQuoteRequest.  # noqa: E501
        :type: str
        """

        self._lineage = lineage

    @property
    def scale_factor(self):
        """Gets the scale_factor of this UpsertQuoteRequest.  # noqa: E501

        An optional scale factor for non-standard scaling of quotes against the instrument. If not supplied, the default ScaleFactor is 1.  # noqa: E501

        :return: The scale_factor of this UpsertQuoteRequest.  # noqa: E501
        :rtype: float
        """
        return self._scale_factor

    @scale_factor.setter
    def scale_factor(self, scale_factor):
        """Sets the scale_factor of this UpsertQuoteRequest.

        An optional scale factor for non-standard scaling of quotes against the instrument. If not supplied, the default ScaleFactor is 1.  # noqa: E501

        :param scale_factor: The scale_factor of this UpsertQuoteRequest.  # noqa: E501
        :type: float
        """

        self._scale_factor = scale_factor

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
        if not isinstance(other, UpsertQuoteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
