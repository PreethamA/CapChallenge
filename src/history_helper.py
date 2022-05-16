
from itertools import chain
import os

class history:

    def __init__(self):
        self.lis=[]
        self.dic={}
        self.attribute = " "
        self.title = " "
        self.y_label = " "
        self.x_label = " "
        self.legend_location = " "
        self.colour = " "
        self.imagename = ''
        self.currentdir = ''
        self.imagefolder = ''
    # setter method
    def set_epoch(self, list2):
       self.lis=list2

    def get_epoch(self):
        return self.lis

    def set_history(self, dic2):
        self.dic = dic2

    def get_history(self):
        return self.dic

    def set_image_detaails(self,image_name,current_dir,image_folder):
        self.imagename=image_name
        self.currentdir =current_dir
        self.imagefolder=image_folder


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

