#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Occurrences Module
Contains operations for occurrences
	1. get_occurrences(self, **kwargs) -> requests.Response
	2. get_occurrence(self, occurrence_id: str) -> requests.Response
"""

import os
import unittest
from sasci360apimarketingexecution import occurrences


class TestOccurrences(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingExecution"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.occurrences = occurrences.Occurrences(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_occurrences_task_id(self):
		"""
		1. get_occurrences(self, **kwargs) -> requests.Response
		"""
		task_id = 0
		result = self.occurrences.get_occurrences(task_id=task_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_occurrences_segment_map_id(self):
		"""
		1. get_occurrences(self, **kwargs) -> requests.Response
		"""
		segment_map_id = 0
		result = self.occurrences.get_occurrences(segment_map_id=segment_map_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_occurrences_type(self):
		"""
		1. get_occurrences(self, **kwargs) -> requests.Response
		"""
		type_ = 0
		result = self.occurrences.get_occurrences(type=type_)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_occurrences_status(self):
		"""
		1. get_occurrences(self, **kwargs) -> requests.Response
		"""
		status = 0
		result = self.occurrences.get_occurrences(status=status)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_occurrences_from_dt(self):
		"""
		1. get_occurrences(self, **kwargs) -> requests.Response
		"""
		from_dt = 0
		result = self.occurrences.get_occurrences(from_dt=from_dt)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_occurrences_to_dt(self):
		"""
		1. get_occurrences(self, **kwargs) -> requests.Response
		"""
		to_dt = 0
		result = self.occurrences.get_occurrences(to_dt=to_dt)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_occurrences_start_time_from(self):
		"""
		1. get_occurrences(self, **kwargs) -> requests.Response
		"""
		start_time_from = 0
		result = self.occurrences.get_occurrences(start_time_from=start_time_from)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_occurrences_start_time_to(self):
		"""
		1. get_occurrences(self, **kwargs) -> requests.Response
		"""
		start_time_to = 0
		result = self.occurrences.get_occurrences(start_time_to=start_time_to)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_occurrences_limit(self):
		"""
		1. get_occurrences(self, **kwargs) -> requests.Response
		"""
		limit = 0
		result = self.occurrences.get_occurrences(limit=limit)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_occurrences_start(self):
		"""
		1. get_occurrences(self, **kwargs) -> requests.Response
		"""
		start = 0
		result = self.occurrences.get_occurrences(start=start)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_occurrences_to_file(self):
		"""
		1. get_occurrences(self, **kwargs) -> requests.Response
		"""
		to_file = 0
		result = self.occurrences.get_occurrences(to_file=to_file)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_occurrences_delimiter_param(self):
		"""
		1. get_occurrences(self, **kwargs) -> requests.Response
		"""
		delimiter_param = 0
		result = self.occurrences.get_occurrences(delimiter_param=delimiter_param)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_occurrences_include_header_row_param(self):
		"""
		1. get_occurrences(self, **kwargs) -> requests.Response
		"""
		include_header_row_param = 0
		result = self.occurrences.get_occurrences(include_header_row_param=include_header_row_param)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_occurrences(self):
		"""
		1. get_occurrences(self, **kwargs) -> requests.Response
		"""
		result = self.occurrences.get_occurrences()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_occurrence(self):
		"""
		2. get_occurrence(self, occurrence_id: str) -> requests.Response
		"""
		occurrence_id = "0"
		result = self.occurrences.get_occurrence(occurrence_id=occurrence_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
