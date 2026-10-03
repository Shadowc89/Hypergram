#  hypergram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of hypergram.
#
#  hypergram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  hypergram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with hypergram.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import annotations as _annotations

from typing import TYPE_CHECKING

from ..object import Object

if TYPE_CHECKING:
    import hypergram


class InputPrivacyRule(Object):
    """Content of a privacy rule.

    It should be one of:

    - :obj:`~hypergram.types.InputPrivacyRuleAllowAll`
    - :obj:`~hypergram.types.InputPrivacyRuleAllowContacts`
    - :obj:`~hypergram.types.InputPrivacyRuleAllowPremium`
    - :obj:`~hypergram.types.InputPrivacyRuleAllowUsers`
    - :obj:`~hypergram.types.InputPrivacyRuleAllowChats`
    - :obj:`~hypergram.types.InputPrivacyRuleDisallowAll`
    - :obj:`~hypergram.types.InputPrivacyRuleDisallowContacts`
    - :obj:`~hypergram.types.InputPrivacyRuleDisallowUsers`
    - :obj:`~hypergram.types.InputPrivacyRuleDisallowChats`
    """

    def __init__(self):
        super().__init__()

    async def write(self, client: hypergram.Client):
        raise NotImplementedError
