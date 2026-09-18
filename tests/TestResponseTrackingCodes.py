#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Response Tracking Codes Module
Contains operations for response tracking codes. A Response Tracking Code (RTC) is an automatically generated code that represents the unique combination of items that an individual is shown.
	1. get_response_tracking_codes(self, **kwargs) -> requests.Response
	2. get_response_tracking_code(self, response_tracking_code_id: str) -> requests.Response
"""

import os
import unittest
from sasci360apimarketingexecution import response_tracking_codes


class TestResponseTrackingCodes(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingExecution"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.response_tracking_codes = response_tracking_codes.ResponseTrackingCodes(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_response_tracking_codes_task_id(self):
		"""
		1. get_response_tracking_codes(self, **kwargs) -> requests.Response
		"""
		task_id = 0
		result = self.response_tracking_codes.get_response_tracking_codes(task_id=task_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_response_tracking_codes_occurrence_id(self):
		"""
		1. get_response_tracking_codes(self, **kwargs) -> requests.Response
		"""
		occurrence_id = 0
		result = self.response_tracking_codes.get_response_tracking_codes(occurrence_id=occurrence_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_response_tracking_codes_task_version_id(self):
		"""
		1. get_response_tracking_codes(self, **kwargs) -> requests.Response
		"""
		task_version_id = 0
		result = self.response_tracking_codes.get_response_tracking_codes(task_version_id=task_version_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_response_tracking_codes_from_dt(self):
		"""
		1. get_response_tracking_codes(self, **kwargs) -> requests.Response
		"""
		from_dt = 0
		result = self.response_tracking_codes.get_response_tracking_codes(from_dt=from_dt)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_response_tracking_codes_to_dt(self):
		"""
		1. get_response_tracking_codes(self, **kwargs) -> requests.Response
		"""
		to_dt = 0
		result = self.response_tracking_codes.get_response_tracking_codes(to_dt=to_dt)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_response_tracking_codes_limit(self):
		"""
		1. get_response_tracking_codes(self, **kwargs) -> requests.Response
		"""
		limit = 0
		result = self.response_tracking_codes.get_response_tracking_codes(limit=limit)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_response_tracking_codes_start(self):
		"""
		1. get_response_tracking_codes(self, **kwargs) -> requests.Response
		"""
		start = 0
		result = self.response_tracking_codes.get_response_tracking_codes(start=start)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_response_tracking_codes_to_file(self):
		"""
		1. get_response_tracking_codes(self, **kwargs) -> requests.Response
		"""
		to_file = 0
		result = self.response_tracking_codes.get_response_tracking_codes(to_file=to_file)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_response_tracking_codes_delimiter_param(self):
		"""
		1. get_response_tracking_codes(self, **kwargs) -> requests.Response
		"""
		delimiter_param = 0
		result = self.response_tracking_codes.get_response_tracking_codes(delimiter_param=delimiter_param)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_response_tracking_codes_include_header_row_param(self):
		"""
		1. get_response_tracking_codes(self, **kwargs) -> requests.Response
		"""
		include_header_row_param = 0
		result = self.response_tracking_codes.get_response_tracking_codes(include_header_row_param=include_header_row_param)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_response_tracking_codes(self):
		"""
		1. get_response_tracking_codes(self, **kwargs) -> requests.Response
		"""
		result = self.response_tracking_codes.get_response_tracking_codes()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_response_tracking_code(self):
		"""
		2. get_response_tracking_code(self, response_tracking_code_id: str) -> requests.Response
		"""
		response_tracking_code_id = "0"
		result = self.response_tracking_codes.get_response_tracking_code(response_tracking_code_id=response_tracking_code_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
