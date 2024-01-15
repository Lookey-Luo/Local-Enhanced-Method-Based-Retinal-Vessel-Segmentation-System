import pytest
import tkinter as tk
from window_for_app import RetinalVesselSegmentationApp

class Test_color:

    def test_upload_button_color(self):
        root_1 = tk.Tk()
        app_1 = RetinalVesselSegmentationApp(root_1)

        root_1.update_idletasks()
        
        #检测上传按钮的颜色
        upload_button_color = app_1.upload_button.cget('bg')
        assert upload_button_color == 'SystemButtonFace'
        
        app_1.exit_program()
        root_1.mainloop()

    def test_principle_button_color(self):
        root_2 = tk.Tk()
        app_2 = RetinalVesselSegmentationApp(root_2)
        
        #检测原理按钮的颜色
        principle_button_color = app_2.principle_button.cget('bg')
        assert principle_button_color == 'SystemButtonFace'
        
        app_2.exit_program()
        root_2.mainloop()
        
    def test_quit_button_color(self):
        root_3 = tk.Tk()
        app_3 = RetinalVesselSegmentationApp(root_3)

        #检测退出按钮的颜色
        quit_button_color = app_3.quit_button.cget('bg')
        assert quit_button_color == 'SystemButtonFace'
        
        app_3.exit_program()
        root_3.mainloop()

    def test_upload_in_principle_window_button_color(self):
        root_4 = tk.Tk()
        app_4 = RetinalVesselSegmentationApp(root_4)

        #检测原理界面上传按钮的颜色
        app_4.demonstrate_principle()
        upload_in_principle_window_button_color = app_4.upload_in_principle_window_button.cget('bg')
        assert upload_in_principle_window_button_color == 'SystemButtonFace'
        
        app_4.exit_program()
        root_4.mainloop()

    def test_return_main_button_color(self):
        root_5 = tk.Tk()
        app_5 = RetinalVesselSegmentationApp(root_5)

        #检测返回主页按钮的颜色
        app_5.demonstrate_principle()
        return_main_button_color = app_5.return_main_button.cget('bg')
        assert return_main_button_color == 'SystemButtonFace'
        
        app_5.exit_program()
        root_5.mainloop()

    def test_quit_in_principle_window_button_color(self):
        root_6 = tk.Tk()
        app_6 = RetinalVesselSegmentationApp(root_6)

        #检测原理界面退出按钮的颜色
        app_6.demonstrate_principle()
        quit_in_principle_window_button_color = app_6.quit_in_principle_window_button.cget('bg')
        assert quit_in_principle_window_button_color == 'SystemButtonFace'
        
        app_6.exit_program()
        root_6.mainloop()

    def test_clear_button_color(self):
        root_7 = tk.Tk()
        app_7 = RetinalVesselSegmentationApp(root_7)

        root_7.update_idletasks()
        
        #检测清除按钮的颜色
        clear_button_color = app_7.clear_button.cget('bg')
        assert clear_button_color == 'SystemButtonFace'
        
        app_7.exit_program()
        root_7.mainloop()


