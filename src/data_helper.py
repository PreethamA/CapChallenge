import os
import datetime
import re

def get_dataset_name(filepath)->str:
    '''
    :param filepath: str->filepath
    :return:str-> folder name
    '''
    dir=os.path.basename(os.path.normpath(filepath))
    return dir
def map_to_app_insight_entry(aml_run_details, experiment_id, experiment_name, env)->dict:
    '''
    :param aml_run_details: dict containing experiment execution details
    :param experiment_id: id of the experiment
    :param experiment_name: name of th experiment
    :param env: not used
    :return: dict containing experiment details
    '''

    expe_dict = {"subscriptions": "test_subscription",
                 "resourceGroup": "test_resource",
                 "amlWorkSpace": "test_workspace",
                 "app_profile": "test_profile"}
    ar = {}
    for k, v in aml_run_details.items():
        if type(v) is dict:
            for sk,sv in v.items():
                sub2="run_type"
                ar[sub2]=sv
        else:
            sub2 = re.sub('(?<!^)(?=[A-Z])', '_', k).lower()
            ar[sub2] = v

    ar["start_time_utc"]=iso8601_to_epoch_ms(ar["start_time_utc"])
    ar["end_time_utc"] = iso8601_to_epoch_ms(ar["end_time_utc"])
    ar["start_time_utc_ms"]=ar["start_time_utc"]
    del ar["start_time_utc"]
    ar["end_time_utc_ms"] = ar["end_time_utc"]
    del ar["end_time_utc"]
    ar["execution_time_ms"]=ar["end_time_utc_ms"]-ar["start_time_utc_ms"]

    ar["experimentName"]= experiment_name
    ar["experimentId"]=experiment_id
    ar.update(expe_dict)
    return ar


def iso8601_to_epoch_ms(time_in_iso8601_format)->int:
    '''
    :param time_in_iso8601_format: string->is08601 time format
    :return: int-> in milliseconds
    '''
    date = datetime.datetime.strptime(time_in_iso8601_format , '%Y-%m-%dT%H:%M:%S.%fZ')
    millisec = (date - datetime.datetime(1970, 1, 1)).total_seconds() * 1000

    return millisec

