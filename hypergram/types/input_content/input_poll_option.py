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


class InputPollOption(Object):
    """This object contains information about one answer option in a poll to be sent.

    Parameters:
        text (``str`` | :obj:`~hypergram.types.FormattedText`, *optional*):
            Option text, 1-100 characters.

        media (:obj:`~hypergram.types.InputPollOptionMedia`, *optional*):
            Option media.
            Currently, can be only of the types Animation, Location, Photo, Sticker, Venue, or Video without caption.
    """

    def __init__(
        self,
        *,
        text: str | types.FormattedText,
        media: types.InputPollOptionMedia | None = None,
    ):
        super().__init__()

        self.text = text
        self.media = media

    async def write(self, client: hypergram.Client) -> raw.types.InputPollAnswer:
        if isinstance(self.text, str):
            self.text = types.FormattedText(text=self.text)

        return raw.types.InputPollAnswer(
            text=await self.text.write(client),
            media=await self.media.write(client=client) if self.media is not None else None,
        )
