
from itertools import chain
import os

class history:

    def __init__(self):
        self.lis=[]
        self.dic={}
        self.attribute = "accuracy"
        self.current_dir = os.getcwd()
        self.image_folder = os.path.join(os.path.join(self.current_dir, "test"), "test_data")
        self.image_name = "test_image.png"
        self.title = "Sample Image"
        self.y_label = "Accuracy"
        self.x_label = "epochs"
        self.legend_location = "upper left"
        self.colour = "r"
    # setter method
    def set_epoch(self, list2):
       self.lis=list2


    def get_epoch(self):
        return self.lis

    def set_history(self, dic2):
        self.dic = dic2

    def get_history(self):
        return self.dic
    def set_image_detaails(self,imagfolder,imagname):
        self.image_name=imagname
        self.image_folder=imagfolder

    def get_image_detaails(self):
        return self.image_folder+self.image_name


def get_epoch_list(history)->list:
    '''
    :param history: instance
    :return: list of values
    '''
    return history.get_epoch()

def get_accuracy_list(history)->list:
    '''

    :param history: instance
    :return: list of values
    '''
    get_list=[]
    x=history.get_history()
    for k,v in x.items():
       get_list.append(v)
    return list(chain(*get_list))

def get_accuracy_per_epoch(history)->dict:
    '''
    :param history:Instance
    :return: dict of keys and values
    '''
    History = history.get_history()
    Epoch = history.get_epoch()
    get_list=[]
    for k,v in History.items():
       get_list.append(v)
    his=list(chain(*get_list))
    dic_expected=dict(zip(Epoch, his))
    return dic_expected

