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

import asyncio
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import hypergram


class Restart:
    async def restart(
        self: hypergram.Client, block: bool = True, clear_handlers: bool = False
    ) -> hypergram.Client:
        """Restart the Client.

        This method will first call :meth:`~hypergram.Client.stop` and then :meth:`~hypergram.Client.start` in a row in
        order to restart a client using a single method.

        Parameters:
            block (``bool``, *optional*):
                Blocks the code execution until the client has been restarted. It is useful with ``block=False`` in case
                you want to restart the own client within an handler in order not to cause a deadlock.
                Defaults to True.

            clear_handlers (``bool``, *optional*):
                Clear the already existing handlers on restart the client.
                Default to False.

        Returns:
            :obj:`~hypergram.Client`: The restarted client itself.

        Raises:
            ConnectionError: In case you try to restart a stopped Client.

        Example:
            .. code-block:: python

                import asyncio

                from hypergram import Client


                async def main():
                    app = Client("my_account")

                    await app.start()
                    ...  # Invoke API methods
                    await app.restart()
                    ...  # Invoke other API methods
                    await app.stop()

                asyncio.run(main())
        """

        async def do_it():
            await self.stop(clear_handlers=clear_handlers)
            await self.start()

        if block:
            await do_it()
        else:
            asyncio.create_task(do_it())

        