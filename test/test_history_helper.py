from src.history_helper import get_accuracy_per_epoch, get_accuracy_list, get_epoch_list, history
from mock import patch


def test_get_epoch_list():
    # prep
    history_epoch = [1, 2, 3, 4, 5]
    history_obj = history()
    history_obj.set_epoch(history_epoch)

    expected_response = [1, 2, 3, 4, 5]

    # act
    actual_response = get_epoch_list(history=history_obj)

    # assert
    assert expected_response == actual_response


def test_get_accuracy_list():
    # prep
    history_dictionary = {
        "accuracy": [5, 6, 7, 8, 9]
    }
    history_obj = history()
    history_obj.set_history(history_dictionary)
    expected_response = [5, 6, 7, 8, 9]

    # act
    actual_response = get_accuracy_list(history=history_obj)

    # assert
    assert expected_response == actual_response


def test_get_accuracy_per_epoch():
    # prep
    history_epoch = [1, 2, 3, 4, 5]
    history_dictionary = {
        "accuracy": [5, 6, 7, 8, 9]
    }
    history_obj = history()
    history_obj.set_epoch(history_epoch)
    history_obj.set_history(history_dictionary)

    expected_response = {1: 5, 2: 6, 3: 7, 4: 8, 5: 9}

    # act
    actual_response = get_accuracy_per_epoch(history=history_obj)

    # assert
    assert expected_response == actual_response


@patch("src.history_helper.get_epoch_list")
@patch("src.history_helper.get_accuracy_list")
def test_get_accuracy_per_epoch_method_calls(mock_get_epoch_list, mock_get_accuracy_list):
    # prep
    history_epoch = [1, 2, 3, 4, 5]
    history_dictionary = {
        "accuracy": [5, 6, 7, 8, 9]
    }
    history_obj = history()
    history_obj.set_epoch(history_epoch)
    history_obj.set_history(history_dictionary)

    # act
    _ = get_accuracy_per_epoch(history=history_obj)

    # assert
    assert mock_get_epoch_list.call_count == 1
    assert mock_get_accuracy_list.call_count == 1
