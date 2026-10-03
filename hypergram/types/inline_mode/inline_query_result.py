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
from uuid import uuid4

from ..object import Object

if TYPE_CHECKING:
    import hypergram
    from hypergram import types


class InlineQueryResult(Object):
    """One result of an inline query.

    - :obj:`~hypergram.types.InlineQueryResultCachedAudio`
    - :obj:`~hypergram.types.InlineQueryResultCachedDocument`
    - :obj:`~hypergram.types.InlineQueryResultCachedAnimation`
    - :obj:`~hypergram.types.InlineQueryResultCachedPhoto`
    - :obj:`~hypergram.types.InlineQueryResultCachedSticker`
    - :obj:`~hypergram.types.InlineQueryResultCachedVideo`
    - :obj:`~hypergram.types.InlineQueryResultCachedVoice`
    - :obj:`~hypergram.types.InlineQueryResultArticle`
    - :obj:`~hypergram.types.InlineQueryResultAudio`
    - :obj:`~hypergram.types.InlineQueryResultContact`
    - :obj:`~hypergram.types.InlineQueryResultDocument`
    - :obj:`~hypergram.types.InlineQueryResultAnimation`
    - :obj:`~hypergram.types.InlineQueryResultLocation`
    - :obj:`~hypergram.types.InlineQueryResultPhoto`
    - :obj:`~hypergram.types.InlineQueryResultVenue`
    - :obj:`~hypergram.types.InlineQueryResultVideo`
    - :obj:`~hypergram.types.InlineQueryResultVoice`
    """

    def __init__(
        self,
        type: str,
        id: str,
        input_message_content: types.InputMessageContent,
        reply_markup: types.keyborad,
    ):
        super().__init__()

        self.type = type
        self.id = str(uuid4()) if id is None else str(id)
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup

    async def write(self, client: hypergram.Client):
        pass
