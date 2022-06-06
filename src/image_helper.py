import os


def get_image(history, **kargs) -> str:
    """
    :param kwargs: arguments containing different paramenters
    :return: str containing file path
    """
    history.set_image_detaails(**kargs)
    if os.path.exists(kargs["image_folder"]) is True:
        os.chdir(kargs["image_folder"])
        filename = open("test_image.png", "wb")
        filename.close()
        os.chdir("..")
    else:
        raise ValueError("Invalid image_folder")
    return history.get_image_detaails()
