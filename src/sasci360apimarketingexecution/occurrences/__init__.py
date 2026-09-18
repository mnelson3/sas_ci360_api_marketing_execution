#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apimarketingexecution.base import Base


class Occurrences(Base):
	"""
	Occurrences Module
	Contains operations for occurrences
		1. get_occurrences(self, **kwargs) -> requests.Response
		2. get_occurrence(self, occurrence_id: str) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_occurrences(self, **kwargs) -> requests.Response:
		"""
		Retrieve execution occurrences
		:keyword task_id: str, optional - Query for occurrences associated with the specified task
		:keyword segment_map_id: int, optional - Query for occurrences associated with the specified segment map
		:keyword type: int, optional - Query for occurrences associated with the specified item type. Possible values: task, segment (The value segment is used to query for segment map occurrences)
		:keyword status: str, optional - Query for occurrences with the specified execution status. Possible values: Success, Failure, In progress
		:keyword from_dt: int, optional - Query for occurrences that ended after the specified time. The format is {year}-{month}-{day}T{hour (24)}-{minute}{time zone}. For example 2021-01-02T13:00-04:00 or 2021-01-02T00:00%2B00:00. Note that %2B must be used instead of + in the time zone field
		:keyword to_dt: int, optional - Query for occurrences that ended before the specified time. The format is {year}-{month}-{day}T{hour (24)}-{minute}{time zone}. For example 2021-01-02T13:00-04:00 or 2021-01-02T00:00%2B00:00. Note that %2B must be used instead of + in the time zone field
		:keyword start_time_from: str, optional - Query for occurrences that started after the specified time. The format is {year}-{month}-{day}T{hour (24)}-{minute}{time zone}. For example 2021-01-02T13:00-04:00 or 2021-01-02T00:00%2B00:00. Note that %2B must be used instead of + in the time zone field
		:keyword start_time_to: int, optional - Query for occurrences that started before the specified time. The format is {year}-{month}-{day}T{hour (24)}-{minute}{time zone}. For example 2021-01-02T13:00-04:00 or 2021-01-02T00:00%2B00:00. Note that %2B must be used instead of + in the time zone field
		:keyword limit: int, optional - The maximum number of occurrences returned by the query (maximum 500)
		:keyword start: int, optional - The first item to return in the query
		:keyword to_file: int, optional - Flag to indicate whether results should be put in a file
		:keyword delimiter_param: int, optional - If results are put in a file, this specifies the delimiter (ctrlA or comma)
		:keyword include_header_row_param: int, optional - If results are put in a file, flag to indicate whether results should include a header row
		:return: Retrieves occurrences of a task or segment.
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
			if "segment_map_id" in kwargs:
				query_string.join("segmentMapId={0}&".format(kwargs["segment_map_id"]))
			if "type" in kwargs:
				query_string.join("type={0}&".format(kwargs["type"]))
			if "status" in kwargs:
				query_string.join("status={0}&".format(kwargs["status"]))
			if "from_dt" in kwargs:
				query_string.join("from={0}&".format(kwargs["from_dt"]))
			if "to_dt" in kwargs:
				query_string.join("to={0}&".format(kwargs["to_dt"]))
			if "start_time_from" in kwargs:
				query_string.join("startTimeFrom={0}&".format(kwargs["start_time_from"]))
			if "start_time_to" in kwargs:
				query_string.join("startTimeTo={0}&".format(kwargs["start_time_to"]))
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
			api_path = "/occurrences{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_occurrence(self, occurrence_id: str) -> requests.Response:
		"""
		Retrieve execution occurrences by ID
		:param occurrence_id: required - ID of occurrence
		:return: Retrieves execution occurrences based on an occurrence ID.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if occurrence_id is None:
			raise Exception("Occurrence ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/occurrences/{0}".format(occurrence_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Occurrences()
