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

from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from hypergram import types

from .handler import Handler

if TYPE_CHECKING:
    import hypergram
    from hypergram.filters import Filter

ManagedBotUpdatedCallbackType = Callable[["hypergram.Client", types.ManagedBotUpdated], Any]


class ManagedBotUpdatedHandler(Handler[ManagedBotUpdatedCallbackType]):
    """The ManagedBotUpdated handler class. Used to handle new managed bot creation updates.
    It is intended to be used with :meth:`~hypergram.Client.add_handler`.

    For a nicer way to register this handler, have a look at the :meth:`~hypergram.Client.on_managed_bot` decorator.

    Parameters:
        callback (``Callable``):
            Pass a function that will be called when a new managed bot creation update arrives. It takes *(client, managed_bot_updated)*
            as positional arguments (look at the section below for a detailed description).

        filters (:obj:`~hypergram.filters.Filter`):
            Pass one or more filters to allow only a subset of users to be passed in your callback function.

    Other parameters:
        client (:obj:`~hypergram.Client`):
            The Client itself, useful when you want to call other API methods inside the handler.

        managed_bot_updated (:obj:`~hypergram.types.ManagedBotUpdated`):
            A new bot was created to be managed by the bot or token of a bot was changed.
    """

    def __init__(
        self,
        callback: ManagedBotUpdatedCallbackType,
        filters: Filter | None = None,
    ) -> None:
        super().__init__(callback, filters)
