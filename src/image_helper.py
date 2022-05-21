from src.history_helper import history
import os



def get_image(history,**kargs)->str:
    '''
    :param kwargs: arguments containing different paramenters
    :return: str containing file path
    '''


    history.set_image_detaails(**kargs)

    return history.get_image_detaails()


