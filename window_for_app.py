import tkinter as tk
from tkinter import filedialog,PhotoImage
from PIL import Image, ImageTk

class RetinalVesselSegmentationApp:
    def __init__(self, root):
        self.root = root
        root.attributes('-fullscreen', True)
        root.title("Retinal Vessel Segmentation System")

        #鼠标移动到上传按钮区域时，按钮变为绿色
        def mouse_enter_upload_button(event):
            self.upload_button.config(bg = 'lightgreen')
            
        #鼠标离开上传按钮区域时，按钮变为白色
        def mouse_leave_upload_button(event):
            self.upload_button.config(bg = 'white')
            
        #鼠标移动到分割按钮区域时，按钮变为绿色            
        def mouse_enter_seg_button(event):
            self.seg_button.config(bg = 'lightgreen')
            
        #鼠标离开分割按钮区域时，按钮变为白色
        def mouse_leave_seg_button(event):
            self.seg_button.config(bg = 'white')
            
        #鼠标移动到原理按钮区域时，按钮变为绿色            
        def mouse_enter_principle_button(event):
            self.principle_button.config(bg = 'lightgreen')
            
        #鼠标离开原理按钮区域时，按钮变为白色
        def mouse_leave_principle_button(event):
            self.principle_button.config(bg = 'white')
            
        #鼠标移动到退出按钮区域时，按钮变为绿色            
        def mouse_enter_quit_button(event):
            self.quit_button.config(bg = 'lightgreen')
            
        #鼠标离开退出按钮区域时，按钮变为白色
        def mouse_leave_quit_button(event):
            self.quit_button.config(bg = 'white')

        #鼠标移动到原理界面上传按钮区域时，按钮变为绿色            
        def mouse_enter_upload_in_principle_window_button(event):
            self.upload_in_principle_window_button.config(bg = 'lightgreen')
            
        #鼠标离开原理界面上传按钮区域时，按钮变为白色
        def mouse_leave_upload_in_principle_window_button(event):
            self.upload_in_principle_window_button.config(bg = 'white')

        #鼠标移动到原理界面转换为灰度图按钮区域时，按钮变为绿色            
        def mouse_enter_turn_gray_in_principle_window_button(event):
            self.turn_gray_in_principle_window_button.config(bg = 'lightgreen')
            
        #鼠标离开原理界面转换为灰度图按钮区域时，按钮变为白色
        def mouse_leave_turn_gray_in_principle_window_button(event):
            self.turn_gray_in_principle_window_button.config(bg = 'white')

        #鼠标移动到原理界面切片按钮区域时，按钮变为绿色            
        def mouse_enter_get_patch_in_principle_window_button(event):
            self.get_patch_in_principle_window_button.config(bg = 'lightgreen')
            
        #鼠标离开原理界面切片按钮区域时，按钮变为白色
        def mouse_leave_get_patch_in_principle_window_button(event):
            self.get_patch_in_principle_window_button.config(bg = 'white')

        #鼠标移动到原理界面直方图均衡化按钮区域时，按钮变为绿色            
        def mouse_enter_equalize_patch_in_principle_window_button(event):
            self.equalize_patch_in_principle_window_button.config(bg = 'lightgreen')
            
        #鼠标离开原理界面直方图均衡化按钮区域时，按钮变为白色
        def mouse_leave_equalize_patch_in_principle_window_button(event):
            self.equalize_patch_in_principle_window_button.config(bg = 'white')

        #鼠标移动到原理界面分割按钮区域时，按钮变为绿色            
        def mouse_enter_seg_patch_in_principle_window_button(event):
            self.seg_patch_in_principle_window_button.config(bg = 'lightgreen')
            
        #鼠标离开原理界面分割按钮区域时，按钮变为白色
        def mouse_leave_seg_patch_in_principle_window_button(event):
            self.seg_patch_in_principle_window_button.config(bg = 'white')

        #鼠标移动到原理界面拼接按钮区域时，按钮变为绿色            
        def mouse_enter_concatenate_patch_in_principle_window_button(event):
            self.concatenate_patch_in_principle_window_button.config(bg = 'lightgreen')
            
        #鼠标离开原理界面拼接按钮区域时，按钮变为白色
        def mouse_leave_concatenate_patch_in_principle_window_button(event):
            self.concatenate_patch_in_principle_window_button.config(bg = 'white')

        #鼠标移动到原理界面遮蔽按钮区域时，按钮变为绿色            
        def mouse_enter_attention_mask_in_principle_window_button(event):
            self.attention_mask_in_principle_window_button.config(bg = 'lightgreen')
            
        #鼠标离开原理界面遮蔽按钮区域时，按钮变为白色
        def mouse_leave_attention_mask_in_principle_window_button(event):
            self.attention_mask_in_principle_window_button.config(bg = 'white')
            
        #鼠标移动到返回主页按钮区域时，按钮变为绿色            
        def mouse_enter_return_main_button(event):
            self.return_main_button.config(bg = 'lightgreen')
            
        #鼠标离开返回主页按钮区域时，按钮变为白色
        def mouse_leave_return_main_button(event):
            self.return_main_button.config(bg = 'white')
            
        #鼠标移动到原理界面退出按钮区域时，按钮变为绿色            
        def mouse_enter_quit_in_principle_window_button(event):
            self.quit_in_principle_window_button.config(bg = 'lightgreen')
            
        #鼠标离开原理界面退出按钮区域时，按钮变为白色
        def mouse_leave_quit_in_principle_window_button(event):
            self.quit_in_principle_window_button.config(bg = 'white')
            
        #定义背景图片标签
        background_image = Image.open('back.jpg')
        background_image = background_image.resize((1280,720))
        background_image = ImageTk.PhotoImage(background_image)
        background_image_label = tk.Label(root, image = background_image)
        background_image_label.configure(image=background_image)
        background_image_label.image = background_image
        background_image_label.place(x = 0, y = 0)

        #定义系统标题标签
        system_title_label = tk.Label(root, 
            text = '视网膜血管分割系统',    #标签的文字
            bg = 'gray',    #标签背景颜色
            justify = 'center',    #标签的对齐方式
            font = ('Arial', 12),    #字体和字体大小
            width = 20, height = 2    #标签长宽（以字符长度计算）
            )
        system_title_label.place(x = 550, y = 50)    #固定窗口位置

        #主界面的素材
        
        #定义上传按钮
        self.upload_button = tk.Button(root, text="上传", width=10, height=1, font = ('Arial', 12), cursor = 'hand2', command=self.upload_image)
        self.upload_button.place(x = 450, y = 480)        
        self.upload_button.bind("<Enter>", mouse_enter_upload_button)
        self.upload_button.bind("<Leave>", mouse_leave_upload_button)
        
        #为待上传的图像定义容器
        self.uploaded_image_label = tk.Label(root)
        self.uploaded_image_label.place(x = 400, y = 200)

        #为分割后的图像定义容器
        self.segmented_image_label = tk.Label(root)
        self.segmented_image_label.place(x = 650, y = 200)

        #定义分割按钮
        self.seg_button = tk.Button(root, text="分割", width=10, height=1, font = ('Arial', 12), cursor = 'hand2', command=self.show_segmented_mask)
        self.seg_button.place(x = 700, y = 480)
        self.seg_button.bind("<Enter>", mouse_enter_seg_button)
        self.seg_button.bind("<Leave>", mouse_leave_seg_button)
        self.seg_button.place_forget()    #主界面暂不显示分割按钮

        #定义原理按钮
        self.principle_button = tk.Button(root, text="原理", width=10, height=1, font = ('Arial', 12), cursor = 'hand2', command=self.demonstrate_principle)
        self.principle_button.place(x = 450, y = 550)
        self.principle_button.bind("<Enter>", mouse_enter_principle_button)
        self.principle_button.bind("<Leave>", mouse_leave_principle_button)
        
        #定义退出按钮
        self.quit_button = tk.Button(root, text="退出", width=10, height=1, font = ('Arial', 12), cursor = 'hand2', command=self.exit_program)
        self.quit_button.place(x = 700, y = 550)
        self.quit_button.bind("<Enter>", mouse_enter_quit_button)
        self.quit_button.bind("<Leave>", mouse_leave_quit_button)

        #原理界面的素材
        
        #为原理界面待上传的图像定义容器
        self.uploaded_image_in_principle_window_label = tk.Label(root)
        self.uploaded_image_in_principle_window_label.place(x = 120, y = 120)
        self.uploaded_image_in_principle_window_label.place_forget()    #主界面不显示原理界面待上传的图像

        #为原理界面灰度图定义容器
        self.gray_image_in_principle_window_label = tk.Label(root)
        self.gray_image_in_principle_window_label.place(x = 120, y = 380)
        self.gray_image_in_principle_window_label.place_forget()    #主界面不显示原理界面灰度图

        #为原理界面图像切片1定义容器
        self.patch_image_1_in_principle_window_label = tk.Label(root)
        self.patch_image_1_in_principle_window_label.place(x = 350, y = 350)
        self.patch_image_1_in_principle_window_label.place_forget()    #主界面不显示原理界面图像切片1

        #为原理界面图像切片2定义容器
        self.patch_image_2_in_principle_window_label = tk.Label(root)
        self.patch_image_2_in_principle_window_label.place(x = 455, y = 350)
        self.patch_image_2_in_principle_window_label.place_forget()    #主界面不显示原理界面图像切片2

        #为原理界面图像切片3定义容器
        self.patch_image_3_in_principle_window_label = tk.Label(root)
        self.patch_image_3_in_principle_window_label.place(x = 350, y = 455)
        self.patch_image_3_in_principle_window_label.place_forget()    #主界面不显示原理界面图像切片3

        #为原理界面图像切片4定义容器
        self.patch_image_4_in_principle_window_label = tk.Label(root)
        self.patch_image_4_in_principle_window_label.place(x = 455, y = 455)
        self.patch_image_4_in_principle_window_label.place_forget()    #主界面不显示原理界面图像切片4

        #为原理界面直方图均衡化后的图像切片1定义容器
        self.equalized_patch_image_1_in_principle_window_label = tk.Label(root)
        self.equalized_patch_image_1_in_principle_window_label.place(x = 610, y = 350)
        self.equalized_patch_image_1_in_principle_window_label.place_forget()    #主界面不显示原理界面直方图均衡化后的图像切片1

        #为原理界面直方图均衡化后的图像切片2定义容器
        self.equalized_patch_image_2_in_principle_window_label = tk.Label(root)
        self.equalized_patch_image_2_in_principle_window_label.place(x = 715, y = 350)
        self.equalized_patch_image_2_in_principle_window_label.place_forget()    #主界面不显示原理界面直方图均衡化后的图像切片2

        #为原理界面直方图均衡化后的图像切片3定义容器
        self.equalized_patch_image_3_in_principle_window_label = tk.Label(root)
        self.equalized_patch_image_3_in_principle_window_label.place(x = 610, y = 455)
        self.equalized_patch_image_3_in_principle_window_label.place_forget()    #主界面不显示原理界面直方图均衡化后的图像切片3

        #为原理界面直方图均衡化后的图像切片4定义容器
        self.equalized_patch_image_4_in_principle_window_label = tk.Label(root)
        self.equalized_patch_image_4_in_principle_window_label.place(x = 715, y = 455)
        self.equalized_patch_image_4_in_principle_window_label.place_forget()    #主界面不显示原理界面直方图均衡化后的图像切片4

        #为原理界面U-net原理图定义容器
        self.Unet_in_principle_window_label = tk.Label(root)
        self.Unet_in_principle_window_label.place(x = 870, y = 370)
        self.Unet_in_principle_window_label.place_forget()    #主界面不显示原理界面U-net原理图

        #为原理界面输出的掩码切片1定义容器
        self.patch_mask_1_in_principle_window_label = tk.Label(root)
        self.patch_mask_1_in_principle_window_label.place(x = 900, y = 120)
        self.patch_mask_1_in_principle_window_label.place_forget()    #主界面不显示原理界面输出的掩码切片1

        #为原理界面输出的掩码切片2定义容器
        self.patch_mask_2_in_principle_window_label = tk.Label(root)
        self.patch_mask_2_in_principle_window_label.place(x = 1005, y = 120)
        self.patch_mask_2_in_principle_window_label.place_forget()    #主界面不显示原理界面输出的掩码切片2

        #为原理界面输出的掩码切片3定义容器
        self.patch_mask_3_in_principle_window_label = tk.Label(root)
        self.patch_mask_3_in_principle_window_label.place(x = 900, y = 225)
        self.patch_mask_3_in_principle_window_label.place_forget()    #主界面不显示原理界面输出的掩码切片3

        #为原理界面输出的掩码切片4定义容器
        self.patch_mask_4_in_principle_window_label = tk.Label(root)
        self.patch_mask_4_in_principle_window_label.place(x = 1005, y = 225)
        self.patch_mask_4_in_principle_window_label.place_forget()    #主界面不显示原理界面输出的掩码切片4

        #为原理界面拼接后的掩码定义容器
        self.concatenated_mask_in_principle_window_label = tk.Label(root)
        self.concatenated_mask_in_principle_window_label.place(x = 625, y = 120)
        self.concatenated_mask_in_principle_window_label.place_forget()    #主界面不显示原理界面拼接后的掩码

        #为原理界面遮蔽后的掩码定义容器
        self.attention_mask_in_principle_window_label = tk.Label(root)
        self.attention_mask_in_principle_window_label.place(x = 365, y = 120)
        self.attention_mask_in_principle_window_label.place_forget()    #主界面不显示原理界面遮蔽后的掩码
        
        #定义原理界面上传按钮
        self.upload_in_principle_window_button = tk.Button(root, text="上传", width=10, height=1, font = ('Arial', 12), cursor = 'hand2', command=self.upload_image_in_principle_window)
        self.upload_in_principle_window_button.place(x = 145, y = 290)
        self.upload_in_principle_window_button.bind("<Enter>", mouse_enter_upload_in_principle_window_button)
        self.upload_in_principle_window_button.bind("<Leave>", mouse_leave_upload_in_principle_window_button)        
        self.upload_in_principle_window_button.place_forget()    #主界面不显示原理界面上传按钮

        #定义原理界面转换为灰度图按钮
        self.turn_gray_in_principle_window_button = tk.Button(root, text="灰度图", width=10, height=1, font = ('Arial', 12), cursor = 'hand2', command=self.turn_gray_in_principle_window)
        self.turn_gray_in_principle_window_button.place(x = 145, y = 550)
        self.turn_gray_in_principle_window_button.bind("<Enter>", mouse_enter_turn_gray_in_principle_window_button)
        self.turn_gray_in_principle_window_button.bind("<Leave>", mouse_leave_turn_gray_in_principle_window_button)
        self.turn_gray_in_principle_window_button.place_forget()    #主界面不显示原理界面转换为灰度图按钮

        #定义原理界面切片按钮
        self.get_patch_in_principle_window_button = tk.Button(root, text="切片", width=10, height=1, font = ('Arial', 12), cursor = 'hand2', command=self.get_patch_in_principle_window)
        self.get_patch_in_principle_window_button.place(x = 390, y = 550)
        self.get_patch_in_principle_window_button.bind("<Enter>", mouse_enter_get_patch_in_principle_window_button)
        self.get_patch_in_principle_window_button.bind("<Leave>", mouse_leave_get_patch_in_principle_window_button)
        self.get_patch_in_principle_window_button.place_forget()    #主界面不显示原理界面切片按钮

        #定义原理界面直方图均衡化按钮
        self.equalize_patch_in_principle_window_button = tk.Button(root, text="直方图均衡化", width=10, height=1, font = ('Arial', 12), cursor = 'hand2', command=self.equalize_patch_in_principle_window)
        self.equalize_patch_in_principle_window_button.place(x = 650, y = 550)
        self.equalize_patch_in_principle_window_button.bind("<Enter>", mouse_enter_equalize_patch_in_principle_window_button)
        self.equalize_patch_in_principle_window_button.bind("<Leave>", mouse_leave_equalize_patch_in_principle_window_button)
        self.equalize_patch_in_principle_window_button.place_forget()    #主界面不显示原理界面直方图均衡化按钮

        #定义原理界面分割按钮
        self.seg_patch_in_principle_window_button = tk.Button(root, text="分割", width=10, height=1, font = ('Arial', 12), cursor = 'hand2', command=self.seg_patch_in_principle_window)
        self.seg_patch_in_principle_window_button.place(x = 940, y = 550)
        self.seg_patch_in_principle_window_button.bind("<Enter>", mouse_enter_seg_patch_in_principle_window_button)
        self.seg_patch_in_principle_window_button.bind("<Leave>", mouse_leave_seg_patch_in_principle_window_button)
        self.seg_patch_in_principle_window_button.place_forget()    #主界面不显示原理界面分割按钮

        #定义原理界面拼接按钮
        self.concatenate_patch_in_principle_window_button = tk.Button(root, text="拼接", width=10, height=1, font = ('Arial', 12), cursor = 'hand2', command=self.concatenate_patch_in_principle_window)
        self.concatenate_patch_in_principle_window_button.place(x = 650, y = 290)
        self.concatenate_patch_in_principle_window_button.bind("<Enter>", mouse_enter_concatenate_patch_in_principle_window_button)
        self.concatenate_patch_in_principle_window_button.bind("<Leave>", mouse_leave_concatenate_patch_in_principle_window_button)
        self.concatenate_patch_in_principle_window_button.place_forget()    #主界面不显示原理界面拼接按钮

        #定义原理界面遮蔽按钮
        self.attention_mask_in_principle_window_button = tk.Button(root, text="遮蔽", width=10, height=1, font = ('Arial', 12), cursor = 'hand2', command=self.attention_mask_in_principle_window)
        self.attention_mask_in_principle_window_button.place(x = 390, y = 290)
        self.attention_mask_in_principle_window_button.bind("<Enter>", mouse_enter_attention_mask_in_principle_window_button)
        self.attention_mask_in_principle_window_button.bind("<Leave>", mouse_leave_attention_mask_in_principle_window_button)
        self.attention_mask_in_principle_window_button.place_forget()    #主界面不显示原理界面遮蔽按钮
        
        #定义返回主页按钮
        self.return_main_button = tk.Button(root, text="返回主页", width=10, height=1, font = ('Arial', 12), cursor = 'hand2', command=self.return_main)
        self.return_main_button.place(x = 450, y = 650)
        self.return_main_button.bind("<Enter>", mouse_enter_return_main_button)
        self.return_main_button.bind("<Leave>", mouse_leave_return_main_button)
        self.return_main_button.place_forget()    #主界面不显示返回主页按钮
        
        #定义原理界面退出按钮
        self.quit_in_principle_window_button = tk.Button(root, text="退出", width=10, height=1, font = ('Arial', 12), cursor = 'hand2', command=self.exit_program)
        self.quit_in_principle_window_button.place(x = 700, y = 650)
        self.quit_in_principle_window_button.bind("<Enter>", mouse_enter_quit_in_principle_window_button)
        self.quit_in_principle_window_button.bind("<Leave>", mouse_leave_quit_in_principle_window_button)
        self.quit_in_principle_window_button.place_forget()    #主界面不显示原理界面退出按钮
        
    def upload_image(self):
        file_path = filedialog.askopenfilename(title="选择图片", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            uploaded_image = Image.open(file_path)
            uploaded_image = uploaded_image.resize((200, 200))
            uploaded_photo = ImageTk.PhotoImage(uploaded_image)
            self.uploaded_image_label.configure(image=uploaded_photo)
            self.uploaded_image_label.image = uploaded_photo

        self.uploaded_image_label.place(x = 400, y = 200)    #主界面显示上传的图像
        self.seg_button.place(x = 700, y = 480)    #主界面显示分割按钮

    def show_segmented_mask(self):
        segmented_mask = Image.open('./DRIVE/train/label/01_training.png')
        segmented_mask = segmented_mask.resize((200,200))
        segmented_mask = ImageTk.PhotoImage(segmented_mask)
        self.segmented_image_label.configure(image=segmented_mask)
        self.segmented_image_label.image = segmented_mask

        self.segmented_image_label.place(x = 650, y = 200)    #主界面显示分割后的图像

    def exit_program(self):
        self.root.destroy()

    def upload_image_in_principle_window(self):
        file_path_in_principle_window = filedialog.askopenfilename(title="选择图片", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path_in_principle_window:
            uploaded_image_in_principle_window = Image.open(file_path_in_principle_window)
            uploaded_image_in_principle_window = uploaded_image_in_principle_window.resize((150, 150))
            uploaded_photo_in_principle_window = ImageTk.PhotoImage(uploaded_image_in_principle_window)
            self.uploaded_image_in_principle_window_label.configure(image=uploaded_photo_in_principle_window)
            self.uploaded_image_in_principle_window_label.image = uploaded_photo_in_principle_window

        self.uploaded_image_in_principle_window_label.place(x = 120, y = 120)    #显示原理界面待上传的图像
        self.turn_gray_in_principle_window_button.place(x = 145, y = 550)    #显示原理界面转换为灰度图按钮

    def turn_gray_in_principle_window(self):
        gray_image = Image.open('./DRIVE/train/image/01_training.png')
        gray_image = gray_image.resize((150,150))
        gray_image = ImageTk.PhotoImage(gray_image)
        self.gray_image_in_principle_window_label.configure(image=gray_image)
        self.gray_image_in_principle_window_label.image = gray_image
        
        self.gray_image_in_principle_window_label.place(x = 120, y = 380)    #显示原理界面灰度图
        self.get_patch_in_principle_window_button.place(x = 390, y = 550)    #显示原理界面切片按钮

    def get_patch_in_principle_window(self):
        #填充输入图像切片1
        patch_image_1 = Image.open('./tmp_for_app/real_patch_image_1.png')
        patch_image_1 = patch_image_1.resize((75,75))
        patch_image_1 = ImageTk.PhotoImage(patch_image_1)
        self.patch_image_1_in_principle_window_label.configure(image=patch_image_1)
        self.patch_image_1_in_principle_window_label.image = patch_image_1

        self.patch_image_1_in_principle_window_label.place(x = 350, y = 350)    #显示原理界面图像切片1

        #填充输入图像切片2
        patch_image_2 = Image.open('./tmp_for_app/real_patch_image_2.png')
        patch_image_2 = patch_image_2.resize((75,75))
        patch_image_2 = ImageTk.PhotoImage(patch_image_2)
        self.patch_image_2_in_principle_window_label.configure(image=patch_image_2)
        self.patch_image_2_in_principle_window_label.image = patch_image_2

        self.patch_image_2_in_principle_window_label.place(x = 455, y = 350)    #显示原理界面图像切片2

        #填充输入图像切片3
        patch_image_3 = Image.open('./tmp_for_app/real_patch_image_3.png')
        patch_image_3 = patch_image_3.resize((75,75))
        patch_image_3 = ImageTk.PhotoImage(patch_image_3)
        self.patch_image_3_in_principle_window_label.configure(image=patch_image_3)
        self.patch_image_3_in_principle_window_label.image = patch_image_3

        self.patch_image_3_in_principle_window_label.place(x = 350, y = 455)    #显示原理界面图像切片3

        #填充输入图像切片4
        patch_image_4 = Image.open('./tmp_for_app/real_patch_image_4.png')
        patch_image_4 = patch_image_4.resize((75,75))
        patch_image_4 = ImageTk.PhotoImage(patch_image_4)
        self.patch_image_4_in_principle_window_label.configure(image=patch_image_4)
        self.patch_image_4_in_principle_window_label.image = patch_image_4

        self.patch_image_4_in_principle_window_label.place(x = 455, y = 455)    #显示原理界面图像切片4
        self.equalize_patch_in_principle_window_button.place(x = 650, y = 550)    #显示原理界面直方图均衡化按钮

    def equalize_patch_in_principle_window(self):
        #填充直方图均衡化后的图像切片1
        equalized_patch_image_1 = Image.open('./tmp_for_app/real_equalized_patch_image_1.png')
        equalized_patch_image_1 = equalized_patch_image_1.resize((75,75))
        equalized_patch_image_1 = ImageTk.PhotoImage(equalized_patch_image_1)
        self.equalized_patch_image_1_in_principle_window_label.configure(image=equalized_patch_image_1)
        self.equalized_patch_image_1_in_principle_window_label.image = equalized_patch_image_1

        self.equalized_patch_image_1_in_principle_window_label.place(x = 610, y = 350)    #显示原理界面直方图均衡化后的图像切片1

        #填充直方图均衡化后的图像切片2
        equalized_patch_image_2 = Image.open('./tmp_for_app/real_equalized_patch_image_2.png')
        equalized_patch_image_2 = equalized_patch_image_2.resize((75,75))
        equalized_patch_image_2 = ImageTk.PhotoImage(equalized_patch_image_2)
        self.equalized_patch_image_2_in_principle_window_label.configure(image=equalized_patch_image_2)
        self.equalized_patch_image_2_in_principle_window_label.image = equalized_patch_image_2

        self.equalized_patch_image_2_in_principle_window_label.place(x = 715, y = 350)    #显示原理界面直方图均衡化后的图像切片2

        #填充直方图均衡化后的图像切片3
        equalized_patch_image_3 = Image.open('./tmp_for_app/real_equalized_patch_image_3.png')
        equalized_patch_image_3 = equalized_patch_image_3.resize((75,75))
        equalized_patch_image_3 = ImageTk.PhotoImage(equalized_patch_image_3)
        self.equalized_patch_image_3_in_principle_window_label.configure(image=equalized_patch_image_3)
        self.equalized_patch_image_3_in_principle_window_label.image = equalized_patch_image_3

        self.equalized_patch_image_3_in_principle_window_label.place(x = 610, y = 455)    #显示原理界面直方图均衡化后的图像切片3

        #填充直方图均衡化后的图像切片4
        equalized_patch_image_4 = Image.open('./tmp_for_app/real_equalized_patch_image_4.png')
        equalized_patch_image_4 = equalized_patch_image_4.resize((75,75))
        equalized_patch_image_4 = ImageTk.PhotoImage(equalized_patch_image_4)
        self.equalized_patch_image_4_in_principle_window_label.configure(image=equalized_patch_image_4)
        self.equalized_patch_image_4_in_principle_window_label.image = equalized_patch_image_4

        self.equalized_patch_image_4_in_principle_window_label.place(x = 715, y = 455)    #显示原理界面直方图均衡化后的图像切片4

        #填充U-net原理图
        Unet_image = Image.open('./U-net.png')
        Unet_image = Unet_image.resize((240,160))
        Unet_image = ImageTk.PhotoImage(Unet_image)
        self.Unet_in_principle_window_label.configure(image=Unet_image)
        self.Unet_in_principle_window_label.image = Unet_image
        
        self.Unet_in_principle_window_label.place(x = 870, y = 370)    #显示原理界面U-net原理图
        self.seg_patch_in_principle_window_button.place(x = 940, y = 550)    #显示原理界面分割按钮

    def seg_patch_in_principle_window(self):
        #填充输出掩码切片1
        patch_mask_1 = Image.open('./tmp_for_app/real_patch_mask_1.png')
        patch_mask_1 = patch_mask_1.resize((75,75))
        patch_mask_1 = ImageTk.PhotoImage(patch_mask_1)
        self.patch_mask_1_in_principle_window_label.configure(image=patch_mask_1)
        self.patch_mask_1_in_principle_window_label.image = patch_mask_1

        self.patch_mask_1_in_principle_window_label.place(x = 900, y = 120)    #显示原理界面输出的掩码切片1

        #填充输出掩码切片2
        patch_mask_2 = Image.open('./tmp_for_app/real_patch_mask_2.png')
        patch_mask_2 = patch_mask_2.resize((75,75))
        patch_mask_2 = ImageTk.PhotoImage(patch_mask_2)
        self.patch_mask_2_in_principle_window_label.configure(image=patch_mask_2)
        self.patch_mask_2_in_principle_window_label.image = patch_mask_2

        self.patch_mask_2_in_principle_window_label.place(x = 1005, y = 120)    #显示原理界面输出的掩码切片2

        #填充输出掩码切片3
        patch_mask_3 = Image.open('./tmp_for_app/real_patch_mask_3.png')
        patch_mask_3 = patch_mask_3.resize((75,75))
        patch_mask_3 = ImageTk.PhotoImage(patch_mask_3)
        self.patch_mask_3_in_principle_window_label.configure(image=patch_mask_3)
        self.patch_mask_3_in_principle_window_label.image = patch_mask_3

        self.patch_mask_3_in_principle_window_label.place(x = 900, y = 225)    #显示原理界面输出的掩码切片3

        #填充输出掩码切片4
        patch_mask_4 = Image.open('./tmp_for_app/real_patch_mask_4.png')
        patch_mask_4 = patch_mask_4.resize((75,75))
        patch_mask_4 = ImageTk.PhotoImage(patch_mask_4)
        self.patch_mask_4_in_principle_window_label.configure(image=patch_mask_4)
        self.patch_mask_4_in_principle_window_label.image = patch_mask_4

        self.patch_mask_4_in_principle_window_label.place(x = 1005, y = 225)    #显示原理界面输出的掩码切片4
        self.concatenate_patch_in_principle_window_button.place(x = 650, y = 290)    #显示原理界面拼接按钮

    def concatenate_patch_in_principle_window(self):
        #填充拼接后的输出掩码
        concatenated_mask = Image.open('./tmp_for_app/real_mask_without_attention.png')
        concatenated_mask = concatenated_mask.resize((150,150))
        concatenated_mask = ImageTk.PhotoImage(concatenated_mask)
        self.concatenated_mask_in_principle_window_label.configure(image=concatenated_mask)
        self.concatenated_mask_in_principle_window_label.image = concatenated_mask

        self.concatenated_mask_in_principle_window_label.place(x = 625, y = 120)    #显示原理界面拼接后的输出掩码
        self.attention_mask_in_principle_window_button.place(x = 390, y = 290)    #显示原理界面遮蔽按钮

    def attention_mask_in_principle_window(self):
        #填充遮蔽后的输出掩码
        attention_mask = Image.open('./tmp_for_app/real_mask_with_attention.png')
        attention_mask = attention_mask.resize((150,150))
        attention_mask = ImageTk.PhotoImage(attention_mask)
        self.attention_mask_in_principle_window_label.configure(image=attention_mask)
        self.attention_mask_in_principle_window_label.image = attention_mask

        self.attention_mask_in_principle_window_label.place(x = 365, y = 120)    #显示原理界面遮蔽后的输出掩码

    def return_main(self):
        #隐藏原理界面的所有按钮和标签
        self.uploaded_image_in_principle_window_label.place_forget()
        self.gray_image_in_principle_window_label.place_forget()
        self.patch_image_1_in_principle_window_label.place_forget()
        self.patch_image_2_in_principle_window_label.place_forget()
        self.patch_image_3_in_principle_window_label.place_forget()
        self.patch_image_4_in_principle_window_label.place_forget()
        self.equalized_patch_image_1_in_principle_window_label.place_forget()
        self.equalized_patch_image_2_in_principle_window_label.place_forget()
        self.equalized_patch_image_3_in_principle_window_label.place_forget()
        self.equalized_patch_image_4_in_principle_window_label.place_forget()
        self.Unet_in_principle_window_label.place_forget()
        self.patch_mask_1_in_principle_window_label.place_forget()
        self.patch_mask_2_in_principle_window_label.place_forget()
        self.patch_mask_3_in_principle_window_label.place_forget()
        self.patch_mask_4_in_principle_window_label.place_forget()
        self.concatenated_mask_in_principle_window_label.place_forget()
        self.attention_mask_in_principle_window_label.place_forget()
        
        self.upload_in_principle_window_button.place_forget()
        self.turn_gray_in_principle_window_button.place_forget()
        self.get_patch_in_principle_window_button.place_forget()
        self.equalize_patch_in_principle_window_button.place_forget()
        self.seg_patch_in_principle_window_button.place_forget()
        self.concatenate_patch_in_principle_window_button.place_forget()
        self.attention_mask_in_principle_window_button.place_forget()
        self.return_main_button.place_forget()
        self.quit_in_principle_window_button.place_forget()

        #显示主界面的所有按钮和标签
        self.upload_button.place(x = 450, y = 480)   
        self.principle_button.place(x = 450, y = 550)
        self.quit_button.place(x = 700, y = 550)        

    def demonstrate_principle(self):
        #隐藏主界面的所有按钮和标签
        self.upload_button.place_forget()
        self.seg_button.place_forget()
        self.principle_button.place_forget()
        self.quit_button.place_forget()
        self.uploaded_image_label.place_forget()
        self.segmented_image_label.place_forget()

        #显示原理界面的所有按钮和标签        
        self.upload_in_principle_window_button.place(x = 145, y = 290)        
        self.return_main_button.place(x = 450, y = 650)
        self.quit_in_principle_window_button.place(x = 700, y = 650)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = RetinalVesselSegmentationApp(root)
    root.mainloop()
