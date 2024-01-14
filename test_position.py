import pytest
import tkinter as tk
from window_for_app import RetinalVesselSegmentationApp

class Test_position:

    def test_upload_button_position(self):
        root_1 = tk.Tk()
        app_1 = RetinalVesselSegmentationApp(root_1)
        
        #检测上传按钮的位置
        upload_button_position = app_1.upload_button.place_info()
        assert upload_button_position['x'] == '450'
        assert upload_button_position['y'] == '480'
        
        app_1.exit_program()
        root_1.mainloop()

    def test_principle_button_position(self):
        root_2 = tk.Tk()
        app_2 = RetinalVesselSegmentationApp(root_2)
        
        #检测原理按钮的位置
        principle_button_position = app_2.principle_button.place_info()
        assert principle_button_position['x'] == '450'
        assert principle_button_position['y'] == '550'
        
        app_2.exit_program()
        root_2.mainloop()
        
    def test_quit_button_position(self):
        root_3 = tk.Tk()
        app_3 = RetinalVesselSegmentationApp(root_3)

        #检测退出按钮的位置
        quit_button_position = app_3.quit_button.place_info()
        assert quit_button_position['x'] == '700'
        assert quit_button_position['y'] == '550'
        
        app_3.exit_program()
        root_3.mainloop()

    def test_upload_in_principle_window_button_position(self):
        root_4 = tk.Tk()
        app_4 = RetinalVesselSegmentationApp(root_4)

        #检测原理界面上传按钮的位置
        app_4.demonstrate_principle()
        upload_in_principle_window_button_position = app_4.upload_in_principle_window_button.place_info()
        assert upload_in_principle_window_button_position['x'] == '145'
        assert upload_in_principle_window_button_position['y'] == '290'
        
        app_4.exit_program()
        root_4.mainloop()

    def test_return_main_button_position(self):
        root_5 = tk.Tk()
        app_5 = RetinalVesselSegmentationApp(root_5)

        #检测返回主页按钮的位置
        app_5.demonstrate_principle()
        return_main_button_position = app_5.return_main_button.place_info()
        assert return_main_button_position['x'] == '450'
        assert return_main_button_position['y'] == '650'
        
        app_5.exit_program()
        root_5.mainloop()

    def test_quit_in_principle_window_button_position(self):
        root_6 = tk.Tk()
        app_6 = RetinalVesselSegmentationApp(root_6)

        #检测原理界面退出按钮的位置
        app_6.demonstrate_principle()
        quit_in_principle_window_button_position = app_6.quit_in_principle_window_button.place_info()
        assert quit_in_principle_window_button_position['x'] == '700'
        assert quit_in_principle_window_button_position['y'] == '650'
        
        app_6.exit_program()
        root_6.mainloop()

    def test_uploaded_image_label_position(self):
        root_7 = tk.Tk()
        app_7 = RetinalVesselSegmentationApp(root_7)
        
        #检测待上传的图像的位置
        uploaded_image_label_position = app_7.uploaded_image_label.place_info()
        assert uploaded_image_label_position['x'] == '400'
        assert uploaded_image_label_position['y'] == '200'
        
        app_7.exit_program()
        root_7.mainloop()

    def test_segmented_image_label_position(self):
        root_8 = tk.Tk()
        app_8 = RetinalVesselSegmentationApp(root_8)
        
        #检测分割后的图像的位置
        segmented_image_label_position = app_8.segmented_image_label.place_info()
        assert segmented_image_label_position['x'] == '650'
        assert segmented_image_label_position['y'] == '200'
        
        app_8.exit_program()
        root_8.mainloop()



