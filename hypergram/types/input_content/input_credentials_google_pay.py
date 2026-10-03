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
from hypergram import raw

from .input_credentials import InputCredentials


class InputCredentialsGooglePay(InputCredentials):
    """Applies if a user enters new credentials using Google Pay.

    Parameters:
        data (``str``):
            JSON-encoded data with the credential identifier.
    """

    def __init__(
        self,
        data: str,
    ):
        super().__init__()

        self.data = data

    async def write(self, client: hypergram.Client):
        return raw.types.InputPaymentCredentialsGooglePay(
            payment_token=raw.types.DataJSON(data=self.data)
        )
