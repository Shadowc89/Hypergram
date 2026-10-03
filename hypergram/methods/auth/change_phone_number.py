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

import logging
import re

import hypergram
from hypergram import raw, types, utils

log = logging.getLogger(__name__)


class ChangePhoneNumber:
    async def change_phone_number(
        self: hypergram.Client, phone_number: str, phone_code_hash: str, phone_code: str
    ) -> types.User:
        """Change a user phone number in Telegram with a valid confirmation code.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            phone_number (``str``):
                Phone number in international format (includes the country prefix).

            phone_code_hash (``str``):
                Code identifier taken from the result of :meth:`~hypergram.Client.send_phone_number_code`.

            phone_code (``str``):
                The valid confirmation code you received from SMS in your phone number.

        Returns:
            :obj:`~hypergram.types.User`: On success, in case the change completed, the user is returned.
        """
        phone_number = re.sub(r"\D", "", phone_number)

        r = await self.invoke(
            raw.functions.account.ChangePhone(
                phone_number=phone_number, phone_code_hash=phone_code_hash, phone_code=phone_code
            )
        )

        return utils.require_parsed(await types.User._parse(