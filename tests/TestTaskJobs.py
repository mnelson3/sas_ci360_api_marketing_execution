#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Task Jobs Module
Contains operations for tasks' execution jobs.
	1. get_task_jobs(self, task_job_id: str) -> requests.Response
	2. create_task_jobs(self, payload: dict) -> requests.Response
"""

import os
import unittest
from sasci360apimarketingexecution import task_jobs


class TestTaskJobs(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingExecution"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.task_jobs = task_jobs.TaskJobs(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_task_jobs(self):
		"""
		1. get_task_jobs(self, task_job_id: str) -> requests.Response
		"""
		task_job_id = "0"
		result = self.task_jobs.get_task_jobs(task_job_id=task_job_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_task_jobs(self):
		"""
		2. create_task_jobs(self, payload: dict) -> requests.Response
		"""
		payload = {
			"taskId": "string",
			"taskName": "string",
			"folderPath": "string",
			"version": 1,
			"overrideSchedule": False
		}
		result = self.task_jobs.create_task_jobs(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
