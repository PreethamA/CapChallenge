import os
import pytest
import shutil
from src.history_helper import history
from src.image_helper import get_image


def test_image_helper_function():
    # prep
    attribute = "accuracy"
    history_dictionary = {
        attribute: [5, 6, 7, 8, 9]
    }
    history_obj = history()
    history_obj.set_history(history_dictionary)

    current_dir = os.getcwd()
    image_folder = os.path.join(os.path.join(current_dir, "test"), "test_data")
    image_name = "test_image.png"
    title = "Sample Image"
    y_label = "Accuracy"
    x_label = "epochs"
    legend_location = "upper left"
    colour = "r"

    if os.path.exists(image_folder) is False:
        os.mkdir(image_folder)

    expected_response = os.path.join(image_folder, image_name)

    # act
    actual_response = get_image(history=history_obj, attribute=attribute,
                                image_folder=image_folder, image_name=image_name,
                                title=title, y_label=y_label, x_label=x_label,
                                legend_location=legend_location, colour=colour)

    # assert
    assert actual_response == expected_response
    assert os.path.isfile(actual_response)

    # clean-up
    os.remove(actual_response)
    os.removedirs(image_folder)


def test_image_helper_defaults():
    # prep
    attribute = "accuracy"
    history_dictionary = {
        attribute: [5, 6, 7, 8, 9]
    }
    history_obj = history()
    history_obj.set_history(history_dictionary)

    current_dir = os.getcwd()
    image_folder = os.path.join(os.path.join(current_dir, "test"), "test_data")
    image_name = "test_image.png"
    title = "Sample Image"
    y_label = "Accuracy"

    if os.path.exists(image_folder) is False:
        os.mkdir(image_folder)

    expected_response = os.path.join(image_folder, image_name)

    # act
    actual_response = get_image(history=history_obj, attribute=attribute,
                                image_folder=image_folder, image_name=image_name,
                                title=title, y_label=y_label)

    # assert
    assert actual_response == expected_response
    assert os.path.isfile(actual_response)

    # clean-up
    os.remove(actual_response)
    os.removedirs(image_folder)


def test_image_helper_exception():
    # prep
    attribute = "accuracy"
    history_dictionary = {
        attribute: [5, 6, 7, 8, 9]
    }
    history_obj = history()
    history_obj.set_history(history_dictionary)

    current_dir = os.getcwd()
    image_folder = os.path.join(os.path.join(current_dir, "test"), "test_data")
    image_name = "test_image.png"
    title = "Sample Image"
    y_label = "Accuracy"

    if os.path.exists(image_folder) is True:
        try:
            shutil.rmtree(image_folder)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

    # act assert
    with pytest.raises(ValueError):
        get_image(history=history_obj, attribute=attribute,
                  image_folder=image_folder, image_name=image_name,
                  title=title, y_label=y_label)
