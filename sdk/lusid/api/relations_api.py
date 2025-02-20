# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2808
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid.api_client import ApiClient
from lusid.exceptions import (
    ApiTypeError,
    ApiValueError
)


class RelationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_relation(self, scope, code, create_relation_request, **kwargs):  # noqa: E501
        """[DEPRECATED] Create Relation  # noqa: E501

        Create a relation between two entity objects by their identifiers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_relation(scope, code, create_relation_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the relation definition (required)
        :param str code: The code of the relation definition (required)
        :param CreateRelationRequest create_relation_request: The details of the relation to create. (required)
        :param str effective_at: The effective datetime or cut label at which the relation should be effective from. Defaults to the current LUSID system datetime if not specified.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CompleteRelation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_relation_with_http_info(scope, code, create_relation_request, **kwargs)  # noqa: E501

    def create_relation_with_http_info(self, scope, code, create_relation_request, **kwargs):  # noqa: E501
        """[DEPRECATED] Create Relation  # noqa: E501

        Create a relation between two entity objects by their identifiers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_relation_with_http_info(scope, code, create_relation_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the relation definition (required)
        :param str code: The code of the relation definition (required)
        :param CreateRelationRequest create_relation_request: The details of the relation to create. (required)
        :param str effective_at: The effective datetime or cut label at which the relation should be effective from. Defaults to the current LUSID system datetime if not specified.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CompleteRelation, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'create_relation_request', 'effective_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_relation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_relation_request' is set
        if ('create_relation_request' not in local_var_params or
                local_var_params['create_relation_request'] is None):
            raise ApiValueError("Missing the required parameter `create_relation_request` when calling `create_relation`")  # noqa: E501

        if ('scope' in local_var_params and
                len(local_var_params['scope']) > 64):
            raise ApiValueError("Invalid value for parameter `scope` when calling `create_relation`, length must be less than or equal to `64`")  # noqa: E501
        if ('scope' in local_var_params and
                len(local_var_params['scope']) < 1):
            raise ApiValueError("Invalid value for parameter `scope` when calling `create_relation`, length must be greater than or equal to `1`")  # noqa: E501
        if 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `create_relation`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) > 64):
            raise ApiValueError("Invalid value for parameter `code` when calling `create_relation`, length must be less than or equal to `64`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) < 1):
            raise ApiValueError("Invalid value for parameter `code` when calling `create_relation`, length must be greater than or equal to `1`")  # noqa: E501
        if 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `create_relation`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'effective_at' in local_var_params:
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_relation_request' in local_var_params:
            body_params = local_var_params['create_relation_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.2808'

        return self.api_client.call_api(
            '/api/relations/{scope}/{code}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CompleteRelation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_relation(self, scope, code, delete_relation_request, **kwargs):  # noqa: E501
        """[DEPRECATED] Delete a relation  # noqa: E501

        Delete a relation between two entity objects represented by their identifiers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_relation(scope, code, delete_relation_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the relation definition (required)
        :param str code: The code of the relation definition (required)
        :param DeleteRelationRequest delete_relation_request: The details of the relation to delete. (required)
        :param str effective_at: The effective datetime or cut label at which the relation should the deletion be effective from. Defaults to the current LUSID system datetime if not specified.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DeletedEntityResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_relation_with_http_info(scope, code, delete_relation_request, **kwargs)  # noqa: E501

    def delete_relation_with_http_info(self, scope, code, delete_relation_request, **kwargs):  # noqa: E501
        """[DEPRECATED] Delete a relation  # noqa: E501

        Delete a relation between two entity objects represented by their identifiers  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_relation_with_http_info(scope, code, delete_relation_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the relation definition (required)
        :param str code: The code of the relation definition (required)
        :param DeleteRelationRequest delete_relation_request: The details of the relation to delete. (required)
        :param str effective_at: The effective datetime or cut label at which the relation should the deletion be effective from. Defaults to the current LUSID system datetime if not specified.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DeletedEntityResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'delete_relation_request', 'effective_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_relation" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'delete_relation_request' is set
        if ('delete_relation_request' not in local_var_params or
                local_var_params['delete_relation_request'] is None):
            raise ApiValueError("Missing the required parameter `delete_relation_request` when calling `delete_relation`")  # noqa: E501

        if ('scope' in local_var_params and
                len(local_var_params['scope']) > 64):
            raise ApiValueError("Invalid value for parameter `scope` when calling `delete_relation`, length must be less than or equal to `64`")  # noqa: E501
        if ('scope' in local_var_params and
                len(local_var_params['scope']) < 1):
            raise ApiValueError("Invalid value for parameter `scope` when calling `delete_relation`, length must be greater than or equal to `1`")  # noqa: E501
        if 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `delete_relation`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) > 64):
            raise ApiValueError("Invalid value for parameter `code` when calling `delete_relation`, length must be less than or equal to `64`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) < 1):
            raise ApiValueError("Invalid value for parameter `code` when calling `delete_relation`, length must be greater than or equal to `1`")  # noqa: E501
        if 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `delete_relation`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'effective_at' in local_var_params:
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'delete_relation_request' in local_var_params:
            body_params = local_var_params['delete_relation_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.2808'

        return self.api_client.call_api(
            '/api/relations/{scope}/{code}/$delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeletedEntityResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
