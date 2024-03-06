#!/bin/bash
commit=$1
cd ~/universe
~/bin/git checkout $commit

sleep 5

result=$(python3 managed-catalog/src/test/hifi/bin/hifi_runner.py -r //spark/pipelines/execution/core:UCTablePropertiesSuite-spark_4.0_2.12 -uh -d)
echo "$result"
failure_detected=$(rg "EXTERNAL_LOCATION_DOES_NOT_EXIST" <<<"$result")
all_tests_passed=$(rg "All tests passed." <<<"$result")
if [[ -n "$all_tests_passed" ]]; then
	echo "Test case passed"
	exit 0
elif [[ -n "$failure_detected" ]]; then
	echo "Test case failed"
	exit 1
else
	echo "Unknown failure"
	exit 2
fi
