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

import hypergram
from hypergram import raw

from .input_media import InputMedia

if TYPE_CHECKING:
    from collections.abc import Callable


class InputMediaLink(InputMedia):
    """Represents an HTTP link to be sent.

    Parameters:
        url (``str``):
            HTTP URL of the link.
    """

    def __init__(
        self,
        url: str,
    ):
        super().__init__()

        self.url = url

    async def write(
        self,
        *,
        client: hypergram.Client,
        chat_id: int | str | None = None,
        progress: Callable | None = None,
        progress_args: tuple = (),
        **kwargs,
    ) -> raw.base.InputMedia:
        return raw.types.InputMediaWebPage(url=self.url)
