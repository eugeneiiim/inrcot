#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Greg Albrecht <oss@undef.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author:: Greg Albrecht W2GMD <oss@undef.net>
#

"""
inReach to Cursor-on-Target Gateway.
~~~~

:author: Greg Albrecht W2GMD <oss@undef.net>
:copyright: Copyright 2021 Greg Albrecht
:license: Apache License, Version 2.0
:source: <https://github.com/ampledata/inrcot>
"""

from .constants import (LOG_FORMAT, LOG_LEVEL, DEFAULT_POLL_INTERVAL,  # NOQA
                        DEFAULT_COT_STALE, DEFAULT_COT_TYPE)

from .functions import inreach_to_cot, split_feed  # NOQA

from .classes import InrWorker  # NOQA

__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2022 Greg Albrecht"
__license__ = "Apache License, Version 2.0"
