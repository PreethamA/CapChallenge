import os
from mock import patch
from environs import Env
from src.data_helper import iso8601_to_epoch_ms, map_to_app_insight_entry, get_dataset_name


def test_dataset_name_unix():
    # prep
    filepath = r"/mnist_experiment/testrun_1/dataset5"
    expected_response = "dataset5"

    # act
    actual_response = get_dataset_name(filepath)

    # assert
    assert expected_response == actual_response


def test_dataset_name_win():
    # prep
    filepath = r"\\mnist_experiment\\testrun_1\\dataset5"
    expected_response = "dataset5"

    # act
    actual_response = get_dataset_name(filepath)

    # assert
    assert expected_response == actual_response


def test_iso8601_to_epoch_ms():
    # prep
    time_in_iso8601_format = "2020-08-04T15:50:36.186Z"
    expected_epoch_timestamp_in_ms = 1596556236186

    # act
    actual_epoch_timestamp_in_ms = iso8601_to_epoch_ms(time_in_iso8601_format)

    # assert
    assert expected_epoch_timestamp_in_ms == actual_epoch_timestamp_in_ms


@patch("src.data_helper.iso8601_to_epoch_ms")
@patch.dict(os.environ,
            {"SUBSCRIPTION_ID": "test_subscription",
             "RESOURCE_GROUP": "test_resource",
             "WORKSPACE_NAME": "test_workspace",
             "APP_PROFILE": "test_profile"})
def test_map_to_app_insight_entry_for_aml_parent_run(mock_iso8601_to_epoch_ms):
    # prep
    env = Env()
    env.read_env()
    print(env)
    experiment_id = "5485db4e-b714-4b20-9531-6cfe79fe8ffe"
    experiment_name = "fake-experiment"

    def side_effect(value: str) -> int:
        if value == "2020-08-04T15:50:36.186Z":
            return 1596556236186
        elif value == "2020-08-04T15:55:58.349Z":
            return 1596556558349
        else:
            raise ValueError("Called with unexpected value.")

    mock_iso8601_to_epoch_ms.side_effect = side_effect

    aml_run_details = {
        "runId": "afbd49e5-0acd-4534-9368-a8bd4e163783",
        "startTimeUtc": "2020-08-04T15:50:36.186Z",
        "endTimeUtc": "2020-08-04T15:55:58.349Z",
        "status": "Completed",
        "properties": {
            "azureml.runsource": "azureml.PipelineRun"
        }
    }

    expected_run_metrics = {"resourceGroup": "test_resource",
                            "amlWorkSpace": "test_workspace",
                            "subscriptions": "test_subscription",
                            "run_id": "afbd49e5-0acd-4534-9368-a8bd4e163783",
                            "experimentName": "fake-experiment",
                            "experimentId": "5485db4e-b714-4b20-9531-6cfe79fe8ffe",
                            "execution_time_ms": 322163,
                            "start_time_utc_ms": 1596556236186,
                            "end_time_utc_ms": 1596556558349,
                            "status": "Completed",
                            "app_profile": "test_profile",
                            "run_type": "azureml.PipelineRun"
                            }

    # act
    actual_run_metrics = map_to_app_insight_entry(aml_run_details, experiment_id, experiment_name, env)

    # assert
    assert mock_iso8601_to_epoch_ms.call_count == 2
    assert expected_run_metrics == actual_run_metrics
