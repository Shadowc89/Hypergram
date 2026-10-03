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

import hypergram
from hypergram import raw, types


class GetPersonalChannels:
    async def get_personal_channels(self: hypergram.Client) -> list[types.Chat] | None:
        """Get all your public channels.

        .. include:: /_includes/usable-by/users.rst

        Returns:
            List of :obj:`~hypergram.types.Chat` | ``None``: On success, a list of personal channels is
            returned, otherwise, in case there is no personal channel, None is returned.

        Example:
            .. code-block:: python

                # Get all your personal channels
                await app.get_personal_channels()
        """
        r = await self.invoke(raw.functions.channels.GetAdminedPublicChannels(for_personal=True))

        return types.List([await types.Chat._parse_chat(self, i) for i in r.chats]) or None
