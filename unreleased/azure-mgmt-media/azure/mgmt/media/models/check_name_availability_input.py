# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CheckNameAvailabilityInput(Model):
    """The request body for CheckNameAvailability API.

    :param name: The name of the resource. A name must be globally unique.
    :type name: str
    :param type: Specifies the type of the resource.
    :type type: str
    """ 

    _validation = {
        'name': {'max_length': 24, 'min_length': 3, 'pattern': '^[a-z0-9]'},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, name=None, type=None):
        self.name = name
        self.type = type
