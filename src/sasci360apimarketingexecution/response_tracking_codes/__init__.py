#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apimarketingexecution.base import Base


class ResponseTrackingCodes(Base):
	"""
	Response Tracking Codes Module
	Contains operations for response tracking codes. A Response Tracking Code (RTC) is an automatically generated code that represents the unique combination of items that an individual is shown.
		1. get_response_tracking_codes(self, **kwargs) -> requests.Response
		2. get_response_tracking_code(self, response_tracking_code_id: str) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_response_tracking_codes(self, **kwargs) -> requests.Response:
		"""
		Retrieve response tracking codes
		:keyword task_id: str, optional - Query for occurrences associated with the specified task
		:keyword occurrence_id: int, optional - Query for response tracking codes associated with the specified occurrence
		:keyword task_version_id: int, optional - Query for response tracking codes associated with the specified task version
		:keyword from_dt: int, optional - Query for occurrences that ended after the specified time. The format is {year}-{month}-{day}T{hour (24)}-{minute}{time zone}. For example 2021-01-02T13:00-04:00 or 2021-01-02T00:00%2B00:00. Note that %2B must be used instead of + in the time zone field
		:keyword to_dt: int, optional - Query for occurrences that ended before the specified time. The format is {year}-{month}-{day}T{hour (24)}-{minute}{time zone}. For example 2021-01-02T13:00-04:00 or 2021-01-02T00:00%2B00:00. Note that %2B must be used instead of + in the time zone field
		:keyword limit: int, optional - The maximum number of occurrences returned by the query (maximum 500)
		:keyword start: int, optional - The first item to return in the query
		:keyword to_file: int, optional - Flag to indicate whether results should be put in a file
		:keyword delimiter_param: int, optional - If results are put in a file, this specifies the delimiter (ctrlA or comma)
		:keyword include_header_row_param: int, optional - If results are put in a file, flag to indicate whether results should include a header row
		:return: Retrieves response tracking codes.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			query_string = "?"
			if "task_id" in kwargs:
				query_string.join("taskId={0}&".format(kwargs["task_id"]))
			if "occurrence_id" in kwargs:
				query_string.join("occurrenceId={0}&".format(kwargs["occurrence_id"]))
			if "task_version_id" in kwargs:
				query_string.join("taskVersionId={0}&".format(kwargs["task_version_id"]))
			if "from_dt" in kwargs:
				query_string.join("from={0}&".format(kwargs["from_dt"]))
			if "to_dt" in kwargs:
				query_string.join("to={0}&".format(kwargs["to_dt"]))
			if "limit" in kwargs:
				query_string.join("limit={0}&".format(kwargs["limit"]))
			if "start" in kwargs:
				query_string.join("start={0}&".format(kwargs["start"]))
			if "to_file" in kwargs:
				query_string.join("toFile={0}&".format(kwargs["to_file"]))
			if "delimiter_param" in kwargs:
				query_string.join("delimiterParam={0}&".format(kwargs["delimiter_param"]))
			if "include_header_row_param" in kwargs:
				query_string.join("includeHeaderRowParam={0}&".format(kwargs["include_header_row_param"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/responseTrackingCodes{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.conn(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_response_tracking_code(self, response_tracking_code_id: str) -> requests.Response:
		"""
		Retrieve response tracking code by ID
		:param response_tracking_code_id: required - ID of response tracking code
		:return: Retrieves response tracking code based on an RTC ID.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if response_tracking_code_id is None:
			raise Exception("Response Tracking Code ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/responseTrackingCodes/{0}".format(response_tracking_code_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	ResponseTrackingCodes()
