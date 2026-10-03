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

if TYPE_CHECKING:
    from collections.abc import Callable

    from .handler_type import HandlerType


class OnStart:
    def on_start(self: OnStart | None = None) -> Callable[[HandlerType], HandlerType]:
        """Decorator for handling client start.

        This does the same thing as :meth:`~hypergram.Client.add_handler` using the
        :obj:`~hypergram.handlers.StartHandler`.

        .. include:: /_includes/usable-by/users-bots.rst
        """

        def decorator(func: HandlerType) -> HandlerType:
            if isinstance(self, hypergram.Client):
                self.add_handler(hypergram.handlers.StartHandler(func))
            else:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                func.handlers.append((hypergram.handlers.StartHandler(func), 0))

            return func

        return decorator
