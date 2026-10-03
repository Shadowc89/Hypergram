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
from hypergram.filters import Filter
from .unbound_arguments import unbound_arguments

if TYPE_CHECKING:
    from collections.abc import Callable

    from .handler_type import HandlerType


class OnDeletedBusinessMessages:
    def on_deleted_business_messages(
        self: OnDeletedBusinessMessages | Filter | None = None,
        filters: Filter | None = None,
        group: int = 0,
    ) -> Callable[[HandlerType], HandlerType]:
        """Decorator for handling deleted messages from business connection.

        This does the same thing as :meth:`~hypergram.Client.add_handler` using the
        :obj:`~hypergram.handlers.DeletedBusinessMessagesHandler`.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            filters (:obj:`~hypergram.filters`, *optional*):
                Pass one or more filters to allow only a subset of messages to be passed
                in your function.

            group (``int``, *optional*):
                The group identifier, defaults to 0.
        """

        def decorator(func: HandlerType) -> HandlerType:
            if isinstance(self, hypergram.Client):
                self.add_handler(
                    hypergram.handlers.DeletedBusinessMessagesHandler(func, filters), group
                )
            elif isinstance(self, Filter) or self is None:
                if not hasattr(func, "handlers"):
                    func.handlers = []

                arguments = unbound_arguments(self, filters=filters, group=group)

                func.handlers.append(
                    (
                        hypergram.handlers.DeletedBusinessMessagesHandler(func, arguments.filters),
                        arguments.group,
                    )
                )

            return func

        return decorator
