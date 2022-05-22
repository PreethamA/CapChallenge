from src.history_helper import history
import os


def get_image(history,**kargs)->str:
    '''
    :param kwargs: arguments containing different paramenters
    :return: str containing file path
    '''
    history.set_image_detaails(**kargs)

    if os.path.exists(kargs['image_folder']):
        os.chdir(kargs['image_folder'])
        filename=open("test_image.png",'wb')
        filename.close()

    return history.get_image_detaails()
