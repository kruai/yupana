#
# Copyright 2018 Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

"""Settings file meant for local development."""
# pylint: disable=wildcard-import, unused-wildcard-import
from .base import *  # noqa: F401,F403
from .env import ENVIRONMENT

DEBUG = ENVIRONMENT.bool('DJANGO_DEBUG', default=True)
SECRET_KEY = ENVIRONMENT.get_value('DJANGO_SECRET_KEY', default='local')
