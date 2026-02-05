# git_actions_pipeline

LINK TO THE REPO = https://github.com/sgrapai/git_actions_pipeline

TEST REPORT SCREENSHOT:
![Alt text](TEST_REPORT_SCREENSHOT.png?raw=true "Optional Title")

Test suites are divided by scope:
 - smoke: minimal set of tests
 - regression: all tests
Also tests are divided by type
 - api: API related tests
 - web: Web related tests

The pipeline will trigger a different suite based on the event
 - When a PR targeting main is created, smoke suite is run
 - When a push to main is commited, regression suite is run
 - Every day at 12:00 (cron) hrs regression will be run
 - Runs can also be trigger manually for all the test suites mentioned before (smoke, regression, api and web)

A CI variable is used and required for API test cases
 - BASE_API_URL
 This variable is configured in the repo

When a test fails, it is run once more in a subsequnet job
