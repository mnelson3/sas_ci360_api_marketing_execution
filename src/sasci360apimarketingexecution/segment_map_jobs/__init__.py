#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apimarketingexecution.base import Base


class SegmentMapJobs(Base):
	"""
	Segment Map Jobs Module
	Contains operations for segment maps' execution jobs.
		1. get_segment_map_jobs(self, segment_map_job_id: str) -> requests.Response
		2. create_segment_map_jobs(self, payload: dict) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_segment_map_jobs(self, segment_map_job_id: str) -> requests.Response:
		"""
		Get a segment map job
		:param segment_map_job_id: required - The unique identifier for the segment map job
		:return: Gets a segment map job details based on the segment map job ID that is specified. The job definition is based on the JSON body in the request.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if segment_map_job_id is None:
			raise Exception("Segment Map Job ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/segmentMapJobs/{0}".format(segment_map_job_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_segment_map_jobs(self, payload: dict) -> requests.Response:
		"""
		Create a job to execute a segment map
		:param payload: required - The representation of a segment map job
		:return: Creates a job to execute a segment map based on the segment map ID that is specified. The job definition is based on the JSON body in the request.
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
			api_path = "/segmentMapJobs"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	SegmentMapJobs()
