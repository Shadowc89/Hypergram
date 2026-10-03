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

from ..object import Object


class RichMessage(Object):
    """Rich formatted message.

    Parameters:
        blocks (List of :obj:`hypergram.types.RichBlock`):
            Content of the message.

        is_rtl (``bool``, *optional*):
            True, if the rich message must be shown right-to-left.

        is_partial (``bool``, *optional*):
            True, if the rich message is one part of a larger one.
    """

    def __init__(
        self,
        *,
        blocks: list[types.RichBlock],
        is_rtl: bool | None = None,
        is_partial: bool | None = None,
    ) -> None:
        super().__init__()

        self.blocks = blocks
        self.is_rtl = is_rtl
        self.is_partial = is_partial

    @staticmethod
    async def _parse(
        client: hypergram.Client,
        rich_message: raw.types.RichMessage,
        users: dict[int, raw.base.User] | None = None,
        chats: dict[int, raw.base.Chat] | None = None,
    ) -> RichMessage:
        users = users or {}
        chats = chats or {}

        if isinstance(rich_message, raw.types.RichMessage):
            photos = {photo.id: photo for photo in rich_message.photos}
            documents = {document.id: document for document in rich_message.documents}

            return RichMessage(
                blocks=types.List(
                    [
                        await types.RichBlock._parse(
                            client,
                            block,
                            photos,
                            documents,
                            users,
                            chats,
                        )
                        for block in rich_message.blocks
                    ]
                ),
                is_rtl=rich_message.rtl,
                is_partial=rich_message.part,
            )
