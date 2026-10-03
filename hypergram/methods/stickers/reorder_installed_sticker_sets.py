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
from hypergram import raw, enums


class ReorderInstalledStickerSets:
    async def reorder_installed_sticker_sets(
        self: hypergram.Client,
        sticker_type: enums.StickerType,
        sticker_set_ids: list[int],
    ) -> bool:
        """Changes the order of installed sticker sets.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            sticker_type (:obj:`~hypergram.enums.StickerType`):
                Type of the sticker sets to reorder.

            sticker_set_ids (List of ``int``):
                Identifiers of installed sticker sets in the new correct order.

        Returns:
            ``bool``: True, on success.
        """
        r = await self.invoke(
            raw.functions.messages.ReorderStickerSets(
                order=sticker_set_ids,
                masks=sticker_type == enums.StickerType.MASK,
                emojis=sticker_type == enums.StickerType.CUSTOM_EMOJI,
            )
        )

        return bool(r)
