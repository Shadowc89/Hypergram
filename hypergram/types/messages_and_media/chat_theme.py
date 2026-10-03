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

from hypergram import raw, types
import hypergram

from ..object import Object


class ChatTheme(Object):
    """Describes a chat theme.

    Parameters:
        name (``str``, *optional*):
            Theme name.
            For themes based on an emoji.

        gift (:obj:`~hypergram.types.Gift`, *optional*):
            Gift that was used to change the theme.
            For themes based on an upgraded gifts.
    """

    def __init__(self, *, name: str | None = None, gift: types.Gift | None = None):
        super().__init__()

        self.name = name
        self.gift = gift

    @staticmethod
    async def _parse(client: hypergram.Client, theme: raw.base.ChatTheme) -> ChatTheme:
        if isinstance(theme, raw.types.ChatTheme):
            return ChatTheme(name=theme.emoticon)
        elif isinstance(theme, raw.types.ChatThemeUniqueGift):
            return ChatTheme(gift=await types.Gift._parse(client, theme.gift))
