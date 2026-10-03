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


class GetGiftUpgradeVariants:
    async def get_gift_upgrade_variants(
        self: hypergram.Client, gift_id: int
    ) -> types.GiftUpgradeVariants:
        """Returns all possible variants of upgraded gifts for a regular gift.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            gift_id (``int``):
                Identifier of the gift.

        Returns:
            :obj:`~hypergram.types.GiftUpgradeVariants`: On success, returns all possible variants of upgraded gifts for the given regular gift.
        """
        r = await self.invoke(raw.functions.payments.GetStarGiftUpgradeAttributes(gift_id=gift_id))

        return await types.GiftUpgradeVariants._parse(self, r)
