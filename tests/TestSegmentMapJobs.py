#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Segment Map Jobs Module
Contains operations for segment maps' execution jobs.
	1. get_segment_map_jobs(self, segment_map_job_id: str) -> requests.Response
	2. create_segment_map_jobs(self, payload: dict) -> requests.Response
"""

import os
import unittest
from sasci360apimarketingexecution import segment_map_jobs


class TestSegmentMapJobs(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingExecution"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.segment_map_jobs = segment_map_jobs.SegmentMapJobs(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_segment_map_jobs(self):
		"""
		1. get_segment_map_jobs(self, segment_map_job_id: str) -> requests.Response
		"""
		segment_map_job_id = "0"
		result = self.segment_map_jobs.get_segment_map_jobs(segment_map_job_id=segment_map_job_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_segment_map_jobs(self):
		"""
		2. create_segment_map_jobs(self, payload: dict) -> requests.Response
		"""
		payload = {
			"segmentMapId": "string",
			"segmentMapName": "string",
			"folderPath": "string",
			"version": 1
		}
		result = self.segment_map_jobs.create_segment_map_jobs(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
