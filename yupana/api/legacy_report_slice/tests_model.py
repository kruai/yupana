#
# Copyright 2019 Red Hat, Inc.
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
"""Test the LegacyReport API."""

import uuid
from datetime import datetime

from django.test import TestCase

from api.legacy_report_slice.model import LegacyReport, LegacyReportSlice


class LegacyReportSliceModelTest(TestCase):
    """Tests against the LegacyReportSlice model."""

    def setUp(self):
        """Create test case setup."""
        self.uuid = str(uuid.uuid4())
        self.uuid2 = str(uuid.uuid4())
        self.upload_srv_msg = {'accountid': '13423',
                               'msg_url': 'foo'}
        self.report_json = {'report_platform_id': self.uuid,
                            'report_type': 'insights',
                            'hosts': {}}
        self.date = datetime.now()
        self.report = LegacyReport(
            report_platform_id=self.uuid,
            upload_srv_kafka_msg=self.upload_srv_msg,
            account='13423',
            state=LegacyReport.NEW,
            state_info=[LegacyReport.NEW],
            retry_count=0,
            last_update_time=self.date,
            ready_to_archive=False,
            arrival_time=self.date,
            processing_start_time=self.date)
        self.report_slice = LegacyReportSlice(
            report_platform_id=self.uuid,
            report_slice_id=self.uuid2,
            account='13423',
            report_json=self.report_json,
            state=LegacyReportSlice.NEW,
            state_info=[LegacyReportSlice.NEW],
            retry_count=0,
            last_update_time=self.date,
            failed_hosts=[],
            candidate_hosts=[],
            ready_to_archive=False,
            report=self.report,
            hosts_count=10,
            creation_time=self.date,
            processing_start_time=self.date)

    def test_report_slice_fields(self):
        """Test the report slice fields."""
        self.assertEqual(self.report_slice.report_platform_id, self.uuid)
        self.assertEqual(self.report_slice.report_json, self.report_json)
        self.assertEqual(self.report_slice.state, LegacyReportSlice.NEW)
        self.assertEqual(self.report_slice.state_info, [LegacyReportSlice.NEW])
        self.assertEqual(self.report_slice.last_update_time, self.date)
        self.assertEqual(self.report_slice.report, self.report)
        # pylint: disable=line-too-long
        expected = "{report_platform_id:%s, report_slice_id: %s, account: 13423, report_json: {'report_platform_id': '%s', 'report_type': 'insights', 'hosts': {}}, git_commit: None, ready_to_archive: False, source: , state: new, state_info: ['new'], retry_count: 0, retry_type: time, last_update_time: %s, failed_hosts: [], candidate_hosts: [], hosts_count: 10, creation_time: %s, processing_start_time: %s, processing_end_time: None }" % (str(self.uuid), str(self.uuid2), str(self.uuid), self.date, self.date, self.date)  # noqa
        self.assertEqual(str(self.report_slice), expected)