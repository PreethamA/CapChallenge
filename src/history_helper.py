
from itertools import chain
import os

class history:

    def __init__(self):
        self.lis=[]
        self.dic={}
        self.attribute = None
        self.title = None
        self.y_label = None
        self.x_label = None
        self.legend_location = None
        self.colour = None
        self.imagename = None
        self.currentdir = None
        self.imagefolder = None

    # setter method
    def set_epoch(self, list2):
       self.lis=list2

    def get_epoch(self):
        return self.lis

    def set_history(self, dic2):
        self.dic = dic2

    def get_history(self):
        return self.dic

    def set_image_detaails(self, **kargs):
        self.imagename =kargs['image_name']
        self.imagefolder=kargs['image_folder']


    def get_image_detaails(self):

        return os.path.join(self.imagefolder,self.imagename)


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
