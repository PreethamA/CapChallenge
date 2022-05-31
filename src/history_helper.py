
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
    @classmethod
    def set_epoch(self, list2):
       self.lis=list2
    @classmethod
    def get_epoch(self):
        return self.lis

    @classmethod
    def set_history(self, dic2):
        self.dic = dic2

    @classmethod
    def get_history(self):
        return self.dic

    @classmethod
    def set_image_detaails(self, **kargs):
         self.imagename =kargs['image_name']
         self.imagefolder=kargs['image_folder']

    @classmethod
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
    his=get_accuracy_list(history)
    Epoch=get_epoch_list(history)
    dic_expected = dict(zip(Epoch, his))
    return dic_expected

