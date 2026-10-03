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


class GiftUpgradePreview(Object):
    """Contains examples of possible upgraded gifts for the given regular gift.

    Parameters:
        models (List of :obj:`~hypergram.types.GiftAttribute`):
            Examples of possible models that can be chosen for the gift after upgrade.

        symbols (List of :obj:`~hypergram.types.GiftAttribute`):
            Examples of possible symbols that can be chosen for the gift after upgrade.

        backdrops (List of :obj:`~hypergram.types.GiftAttribute`):
            Examples of possible backdrops that can be chosen for the gift after upgrade.

        prices (List of :obj:`~hypergram.types.GiftUpgradePrice`):
            Examples of price for gift upgrade from the maximum price to the minimum price.

        next_prices (List of :obj:`~hypergram.types.GiftUpgradePrice`):
            Next changes for the price for gift upgrade with more granularity than in prices.
    """

    def __init__(
        self,
        *,
        models: list[types.GiftAttribute] | None = None,
        symbols: list[types.GiftAttribute] | None = None,
        backdrops: list[types.GiftAttribute] | None = None,
        prices: list[types.GiftUpgradePrice] | None = None,
        next_prices: list[types.GiftUpgradePrice] | None = None,
    ):
        super().__init__()

        self.models = models
        self.symbols = symbols
        self.backdrops = backdrops
        self.prices = prices
        self.next_prices = next_prices

    @staticmethod
    async def _parse(
        client: hypergram.Client, gift_preview: raw.base.payments.StarGiftUpgradePreview
    ):
        models = types.List()
        symbols = types.List()
        backdrops = types.List()

        for attr in gift_preview.sample_attributes:
            if isinstance(attr, raw.types.StarGiftAttributeModel):
                models.append(await types.GiftAttribute._parse(client, attr, {}, {}))
            elif isinstance(attr, raw.types.StarGiftAttributePattern):
                symbols.append(await types.GiftAttribute._parse(client, attr, {}, {}))
            elif isinstance(attr, raw.types.StarGiftAttributeBackdrop):
                backdrops.append(await types.GiftAttribute._parse(client, attr, {}, {}))

        return GiftUpgradePreview(
            models=models,
            symbols=symbols,
            backdrops=backdrops,
            prices=types.List(types.GiftUpgradePrice._parse(p) for p in gift_preview.prices),
            next_prices=types.List(
                types.GiftUpgradePrice._parse(p) for p in gift_preview.next_prices
            ),
        )
