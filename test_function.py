import pytest  #导入pytest模块
import os
import random
from tkinter import Label
from window_for_app import RetinalVesselSegmentationApp
from operation import give_filepath_and_turn_gray, give_filepath_and_get_4_patch, give_filepath_and_equalize_patch, give_filepath_and_predict_mask, give_filepath_and_concatenate_mask, give_filepath_and_add_attention, give_image_filepath_and_seg

class Test_function:

    def test_give_filepath_and_turn_gray(self):
        filedir = './STARE/test/image'
        filelist = os.listdir(filedir)
        for filename in filelist:
            filepath = os.path.join(filedir, filename)
            assert filepath
            output_path = give_filepath_and_turn_gray(filepath)
            assert output_path

    def test_give_filepath_and_get_4_patch(self):
        filedir = './STARE/train/image'
        filelist = os.listdir(filedir)
        for filename in filelist:
            filepath = os.path.join(filedir, filename)
            assert filepath
            output_path_1, output_path_2, output_path_3, output_path_4 = give_filepath_and_get_4_patch(filepath)
            assert output_path_1
            assert output_path_2
            assert output_path_3
            assert output_path_4

    def test_give_filepath_and_equalize_patch(self):
        filedir = './DRIVE/test/image'
        filelist = os.listdir(filedir)
        for filename in filelist:
            filepath = os.path.join(filedir, filename)
            assert filepath
            output_path = give_filepath_and_equalize_patch(filepath)
            assert output_path
    
    def test_give_filepath_and_predict_mask(self):
        filepath = './DRIVE/train/image/01_training.png'
        assert filepath
        output_path = give_filepath_and_predict_mask(filepath)
        assert output_path
    
    
    def test_give_filepath_and_concatenate_mask(self):
        filedir = './DRIVE/test/image'
        filelist = os.listdir(filedir)
        for test_id in range(20):    #随机测试20次
            filename_1, filename_2, filename_3, filename_4 = random.sample(filelist, 4)    #从文件列表中随机挑选4份文件
            filepath_1 = os.path.join(filedir, filename_1)
            filepath_2 = os.path.join(filedir, filename_2)
            filepath_3 = os.path.join(filedir, filename_3)
            filepath_4 = os.path.join(filedir, filename_4)
            assert filepath_1
            assert filepath_2
            assert filepath_3
            assert filepath_4
            output_path = give_filepath_and_concatenate_mask(filepath_1, filepath_2, filepath_3, filepath_4)
            assert output_path
    
    def test_give_filepath_and_add_attention(self):
        filedir = './DRIVE/test/label'
        filelist = os.listdir(filedir)
        for test_id in range(20):    #随机测试20次
            filename = random.sample(filelist, 1)[0]    #从文件列表中随机挑选1份文件
            filepath = os.path.join(filedir, filename)
            assert filepath
            output_path = give_filepath_and_add_attention(filepath)
            assert output_path

    def test_give_image_filepath_and_seg(self):
        filedir = './STARE/test/image'
        filelist = os.listdir(filedir)
        for test_id in range(1):    #随机测试1次
            filename = random.sample(filelist, 1)[0]    #从文件列表中随机挑选1份文件
            filepath = os.path.join(filedir, filename)
            assert filepath
            output_path = give_image_filepath_and_seg(filepath)
            assert output_path
        
