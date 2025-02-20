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

class LegalEntity(object):
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
        'display_name': 'str',
        'description': 'str',
        'href': 'str',
        'lusid_legal_entity_id': 'str',
        'identifiers': 'dict(str, ModelProperty)',
        'properties': 'dict(str, ModelProperty)',
        'version': 'Version',
        'links': 'list[Link]'
    }

    attribute_map = {
        'display_name': 'displayName',
        'description': 'description',
        'href': 'href',
        'lusid_legal_entity_id': 'lusidLegalEntityId',
        'identifiers': 'identifiers',
        'properties': 'properties',
        'version': 'version',
        'links': 'links'
    }

    required_map = {
        'display_name': 'optional',
        'description': 'optional',
        'href': 'optional',
        'lusid_legal_entity_id': 'optional',
        'identifiers': 'optional',
        'properties': 'optional',
        'version': 'optional',
        'links': 'optional'
    }

    def __init__(self, display_name=None, description=None, href=None, lusid_legal_entity_id=None, identifiers=None, properties=None, version=None, links=None):  # noqa: E501
        """
        LegalEntity - a model defined in OpenAPI

        :param display_name:  The display name of the Legal Entity
        :type display_name: str
        :param description:  The description of the Legal Entity
        :type description: str
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param lusid_legal_entity_id:  The unique LUSID Legal Entity Identifier (LULEID) of the Legal Entity. This field is not populated until further notice.
        :type lusid_legal_entity_id: str
        :param identifiers:  Unique client-defined identifiers of the Legal Entity.
        :type identifiers: dict[str, lusid.ModelProperty]
        :param properties:  A set of properties associated to the Legal Entity.
        :type properties: dict[str, lusid.ModelProperty]
        :param version: 
        :type version: lusid.Version
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._display_name = None
        self._description = None
        self._href = None
        self._lusid_legal_entity_id = None
        self._identifiers = None
        self._properties = None
        self._version = None
        self._links = None
        self.discriminator = None

        self.display_name = display_name
        self.description = description
        self.href = href
        self.lusid_legal_entity_id = lusid_legal_entity_id
        self.identifiers = identifiers
        self.properties = properties
        if version is not None:
            self.version = version
        self.links = links

    @property
    def display_name(self):
        """Gets the display_name of this LegalEntity.  # noqa: E501

        The display name of the Legal Entity  # noqa: E501

        :return: The display_name of this LegalEntity.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this LegalEntity.

        The display name of the Legal Entity  # noqa: E501

        :param display_name: The display_name of this LegalEntity.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this LegalEntity.  # noqa: E501

        The description of the Legal Entity  # noqa: E501

        :return: The description of this LegalEntity.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LegalEntity.

        The description of the Legal Entity  # noqa: E501

        :param description: The description of this LegalEntity.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def href(self):
        """Gets the href of this LegalEntity.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this LegalEntity.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this LegalEntity.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this LegalEntity.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def lusid_legal_entity_id(self):
        """Gets the lusid_legal_entity_id of this LegalEntity.  # noqa: E501

        The unique LUSID Legal Entity Identifier (LULEID) of the Legal Entity. This field is not populated until further notice.  # noqa: E501

        :return: The lusid_legal_entity_id of this LegalEntity.  # noqa: E501
        :rtype: str
        """
        return self._lusid_legal_entity_id

    @lusid_legal_entity_id.setter
    def lusid_legal_entity_id(self, lusid_legal_entity_id):
        """Sets the lusid_legal_entity_id of this LegalEntity.

        The unique LUSID Legal Entity Identifier (LULEID) of the Legal Entity. This field is not populated until further notice.  # noqa: E501

        :param lusid_legal_entity_id: The lusid_legal_entity_id of this LegalEntity.  # noqa: E501
        :type: str
        """

        self._lusid_legal_entity_id = lusid_legal_entity_id

    @property
    def identifiers(self):
        """Gets the identifiers of this LegalEntity.  # noqa: E501

        Unique client-defined identifiers of the Legal Entity.  # noqa: E501

        :return: The identifiers of this LegalEntity.  # noqa: E501
        :rtype: dict(str, ModelProperty)
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this LegalEntity.

        Unique client-defined identifiers of the Legal Entity.  # noqa: E501

        :param identifiers: The identifiers of this LegalEntity.  # noqa: E501
        :type: dict(str, ModelProperty)
        """

        self._identifiers = identifiers

    @property
    def properties(self):
        """Gets the properties of this LegalEntity.  # noqa: E501

        A set of properties associated to the Legal Entity.  # noqa: E501

        :return: The properties of this LegalEntity.  # noqa: E501
        :rtype: dict(str, ModelProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this LegalEntity.

        A set of properties associated to the Legal Entity.  # noqa: E501

        :param properties: The properties of this LegalEntity.  # noqa: E501
        :type: dict(str, ModelProperty)
        """

        self._properties = properties

    @property
    def version(self):
        """Gets the version of this LegalEntity.  # noqa: E501


        :return: The version of this LegalEntity.  # noqa: E501
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this LegalEntity.


        :param version: The version of this LegalEntity.  # noqa: E501
        :type: Version
        """

        self._version = version

    @property
    def links(self):
        """Gets the links of this LegalEntity.  # noqa: E501


        :return: The links of this LegalEntity.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this LegalEntity.


        :param links: The links of this LegalEntity.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if not isinstance(other, LegalEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
