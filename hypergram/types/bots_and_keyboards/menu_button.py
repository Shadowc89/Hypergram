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
    from hypergram import raw


class MenuButton(Object):
    """Describes the bot's menu button in a private chat.

    It should be one of:

    - :obj:`~hypergram.types.MenuButtonCommands`
    - :obj:`~hypergram.types.MenuButtonWebApp`
    - :obj:`~hypergram.types.MenuButtonDefault`

    If a menu button other than :obj:`~hypergram.types.MenuButtonDefault` is set for a private chat, then it is applied
    in the chat. Otherwise the default menu button is applied. By default, the menu button opens the list of bot
    commands.
    """

    def __init__(self, type: str):
        super().__init__()

        self.type = type

    async def write(self, client: hypergram.Client) -> raw.base.BotMenuButton:
        raise NotImplementedError
