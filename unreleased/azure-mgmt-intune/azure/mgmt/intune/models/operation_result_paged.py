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

from msrest.paging import Paged


class OperationResultPaged(Paged):
    """
    A paging container for iterating over a list of OperationResult object
    """

    _attribute_map = {
        'next_link': {'key': 'nextlink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[OperationResult]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationResultPaged, self).__init__(*args, **kwargs)
