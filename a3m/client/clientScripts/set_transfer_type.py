# This file is part of Archivematica.
#
# Copyright 2010-2013 Artefactual Systems Inc. <http://artefactual.com>
#
# Archivematica is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Archivematica is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Archivematica.  If not, see <http://www.gnu.org/licenses/>.
import logging

from django.db import transaction

from a3m.client import metrics
from a3m.main.models import Transfer


logger = logging.getLogger(__name__)


def call(jobs):
    with transaction.atomic():
        for job in jobs:
            with job.JobContext(logger=logger):
                transferUUID = job.args[1]
                transferType = job.args[2]

                Transfer.objects.filter(uuid=transferUUID, type__isnull=False).exclude(
                    type="Archivematica AIP"
                ).update(type=transferType)

    metrics.transfer_started(transferType)
