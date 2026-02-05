# git_actions_pipeline

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

When a test fails, it is run once more in a subsequnet job
