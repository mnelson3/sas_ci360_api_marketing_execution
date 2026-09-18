#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apimarketingexecution.base import Base


class TaskJobs(Base):
	"""
	Task Jobs Module
	Contains operations for tasks' execution jobs.
		1. get_task_jobs(self, task_job_id: str) -> requests.Response
		2. create_task_jobs(self, payload: dict) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_task_jobs(self, task_job_id: str) -> requests.Response:
		"""
		Get a task job
		:param task_job_id: required - The unique identifier for the task job
		:return: Gets a task job details based on the task job ID that is specified. The job definition is based on the JSON body in the request.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if task_job_id is None:
			raise Exception("Task Job ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/taskJobs/{0}".format(task_job_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_task_jobs(self, payload: dict) -> requests.Response:
		"""
		Create a job to execute a bulk task
		:param payload: required - The representation of a task job
		:return: Creates a job to execute a bulk task based on the task ID that is specified. The job definition is based on the JSON body in the request.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/taskJobs"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	TaskJobs()
