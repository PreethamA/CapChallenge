from src.history_helper import history


def get_image(**kwargs)->str:
    '''
    :param kwargs: arguments containing different paramenters
    :return: str containing file path
    '''
    de=history()
    H=de.get_image_detaails()
    return H

