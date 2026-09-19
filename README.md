# SAS Customer Intelligence 360

## SAS 360 API MARKETING EXECUTION LIBRARY

> **Status: superseded.** This library has been replaced by [`sas-ci360-sol-execute`](https://github.com/mnelson3/sas-ci360-sol-execute) — the same Marketing Execution API, rebuilt with mockable unit tests, typed exceptions, and safer configuration defaults. This repo is kept for historical reference; start new work in `sas-ci360-sol-execute` instead.

### Overview

The Marketing Execution API enables you to access and manage bulk task execution for various channel types like email and mobile in SAS Customer Intelligence 360. The Marketing Execution REST API provides a way to execute bulk tasks such as bulk email tasks and bulk mobile tasks. This is the same action as clicking the Run Now or Publish and Run Now buttons in a task.

For detailed information on REST API:<br>
https://support.sas.com/documentation/onlinedoc/ci/ci360-apis/marketingExecution/v1/redoc.html
<br><br>

### Table of Contents

This topic contains the following sections:

 - <a href="#prerequisites">Prerequisites</a>
 - <a href="#installation">Installation</a>
 - <a href="#getting-started">Getting Started</a>
 - <a href="#api-marketing-execution-code">API Marketing Execution Code</a>
 - <a href="#troubleshooting">Troubleshooting</a>
 - <a href="#contributing">Contributing</a>
 - <a href="#license">License</a>
 - <a href="#additional-resources">Additional Resources</a>
<br><br>

### Prerequisites

 * Required Python: >=3.6
 * Customer Intelligence 360 Tenant with Administrative Rights
 * SAS CI360 API Core Library:<br>
   https://github.com/mnelson3/sas_ci360_api_core
<br><br>

### Installation

To install the SAS CI360 API Marketing Execution Library from a clone of this repository:
 1. `git clone https://github.com/mnelson3/sas_ci360_api_marketing_execution.git`
 1. `cd sas_ci360_api_marketing_execution`
 1. `pip install .`
<br><br>

### Getting Started

While this library is available for review, please note that it is considered a work in process and NOT considered "released for production".
<br><br>

### API Marketing Execution Code

 1. Occurrences - Contains operations for occurrences. An occurrence is a single execution of an item and is generated either on a recurring schedule or from a user manually running the item. The
   occurrences of an item are listed on the Orchestration > History > Occurrences tab of an item.
 1. Response Tracking Codes - Contains operations for response tracking codes. A Response Tracking Code (RTC) is an automatically generated code that represents the unique combination of items that an
   individual is shown.
 1. Root - Contains operations for this root resource.
 1. Segment Map Jobs - Contains operations for segment maps' execution jobs.
 1. Task Jobs - Contains operations for tasks' execution jobs.
<br><br>

### Troubleshooting

For issues specific to sasci360apicore or sasci360apimarketingexecution try updating the libraries.

To update sasci360apicore:
 1. Pull the latest changes from a clone of the [sas_ci360_api_core](https://github.com/mnelson3/sas_ci360_api_core) repository
 1. Open a terminal window (Unix/macOS) or command prompt (Windows) in that clone
 1. Copy and paste the following line at the cursor<br>
    pip install --upgrade .
 1. Press "Enter"<br>
    The SAS CI360 API Core Library should install

To update sasci360apimarketingexecution:
 1. Pull the latest changes from a clone of this repository
 1. Open a terminal window (Unix/macOS) or command prompt (Windows) in that clone
 1. Copy and paste the following line at the cursor<br>
    pip install --upgrade .
 1. Press "Enter"<br>
    The SAS CI360 API Marketing Execution Library should install
<br><br>

### Contributing

We welcome your contributions! Please read [CONTRIBUTING](CONTRIBUTING.md) for details on how to submit contributions to this project.
<br><br>

### License

This project is licensed under the [Nelson Grey LLC Community License 1.0](LICENSE).

- **Free for individuals, education, and research**: use, modify, and distribute this software for non-commercial purposes
- **Commercial evaluation**: evaluate the software for a possible commercial use, free of charge
- **Commercial production use**: requires a commercial license from Nelson Grey LLC
- **Automatic conversion**: on December 13, 2029, this automatically converts to the Apache License 2.0

For commercial licensing inquiries, contact support@nelsongrey.com.

### Additional Resources

For more information, see [REST APIs](https://go.documentation.sas.com/doc/en/cintcdc/production.a/cintapis/ch-rest-apis.htm).
<br><br>
