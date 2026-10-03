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

from typing import TYPE_CHECKING, BinaryIO

from .input_media import InputMedia

if TYPE_CHECKING:
    from hypergram import raw

    from ..._typing import PathType
    from ..messages_and_media import MessageEntity


class InputPollOptionMedia(InputMedia):
    """Content of a media message to be sent.

    It should be one of:

    - :obj:`~hypergram.types.InputMediaAnimation`
    - :obj:`~hypergram.types.InputMediaLink`
    - :obj:`~hypergram.types.InputMediaLivePhoto`
    - :obj:`~hypergram.types.InputMediaLocation`
    - :obj:`~hypergram.types.InputMediaPhoto`
    - :obj:`~hypergram.types.InputMediaVenue`
    - :obj:`~hypergram.types.InputMediaVideo`
    """

    def __init__(
        self,
        media: PathType | BinaryIO | None = None,
        caption: str = "",
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
    ):
        super().__init__()

        self.media = media
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities

    async def write(self, **kwargs) -> raw.base.InputMedia:
        raise NotImplementedError
