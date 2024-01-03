# Local-Enhanced-Method-Based-Retinal-Vessel-Segmentation-System

# Download Dataset

## DRIVE Dataset  
link:<br>
https://pan.baidu.com/s/1nk0EmKEBVhtKAnctdo4veA<br>
Extract code:<br>
8nel<br>

The Digital Retinal Images for Vessel Extraction (DRIVE) dataset is used for retinal vascular segmentation. It consists of a total of 40 color fundus images in JPEG format; These include 7 cases of abnormal pathology. The images were acquired as part of a diabetic retinopathy screening program in the Netherlands. Each image has a resolution of 584*565 pixels, and each color channel has 8 bits. The 40 images were divided equally into 20 images for the training set and 20 images for the test set. In both sets, each image has a circular field of view mask (FOV) with a diameter of about 540 pixels.

## STARE Dataset  
link:<br>
https://pan.baidu.com/s/1TeXuIS21OfRLoh6DiwZuIg<br>
Extract code:<br>
o9sd<br>

The STARE (Structured Analysis of the Retina) dataset is a public retinal vascular segmentation dataset created by Dr. Michael Goldbaum of the University of Vermont, USA. The dataset includes 20 fundus images with a resolution of 700x605 pixels. These images include various lesions such as macular degeneration, hypertensive retinopathy, diabetic retinopathy, etc. Each image provides a hand-labeled vascular segmentation map that can be used to train and evaluate the vascular segmentation algorithm.

We selected 10 images from STARE dataset as the training set and another 10 images as the test set, and converted them into grayscale images. The selected images include over-exposure and under-illumination, and low contrast in the optic disk region, which can be used to test the robustness of the model.

# Implementation

## Without Patch

### Prepare the Dataset
Place the dataset in the specified directory as required. For example, the DRIVE dataset needs to be placed in the following format:<br>

./DRIVE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/train<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/image<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/01_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/02_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/03_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/20_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/label<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/01_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/02_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/03_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/20_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;/test<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/image<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/01_testing.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/02_testing.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/03_testing.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/20_testing.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/label<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/01_testing.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/02_testing.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/03_testing.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/20_testing.png<br>

The DRIVE dataset and STARE dataset are processed grayscale images. If there are RGB images in your dataset, convert the RGB images to grayscale by executing the following command.<br>
```python  
python RGB2gray.py
```

### Execute the Training Code
```python  
python train.py
```

After the training, the weight file UNet.pth is generated in the home directory.<br>
We provide our weight file pretrained using the DRIVE dataset (loss functions during training include cross-entropy loss and dice loss) .<br>

link:<br>
https://pan.baidu.com/s/1Zexs93LNct2n1lCjNIlUoQ<br>
Extract code:<br>
3c4x<br>

### Predict a Mask
Place an image in **png** format in the predict directory. The file name should be img.png.<br>
We have put a processed image in the predict folder. You can replace it with your own image (either an RGB image or a grayscale image) .<br>

./predict<br>
&nbsp;&nbsp;&nbsp;&nbsp;/img.png<br>

Run the prediction code.<br>
```python  
python predict.py
```
Then the output mask can be observed in the result directory, and the file name is res.png.<br>

./result<br>
&nbsp;&nbsp;&nbsp;&nbsp;/res.png<br>

## With Patch

### Prepare the Dataset
Place the dataset in the specified directory as required. For example, the DRIVE dataset needs to be placed in the following format:<br>

./DRIVE<br>
&nbsp;&nbsp;&nbsp;&nbsp;/train<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/image<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/01_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/02_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/03_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/20_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/label<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/01_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/02_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/03_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/20_training.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;/test<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/image<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/01_testing.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/02_testing.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/03_testing.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/20_testing.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/label<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/01_testing.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/02_testing.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/03_testing.png<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;...<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;/20_testing.png<br>

The DRIVE dataset and STARE dataset are processed grayscale images. If there are RGB images in your dataset, convert the RGB images to grayscale by executing the following command.<br>
```python  
python RGB2gray.py
```

### Run the Clipping Code
```python  
python split_training_set.py
python split_testing_set.py
```
After running the code, a folder named DRIVE_patch will be generated, and the clipped images will be numbered sequentially and saved in this folder. This code applies to clipping the training set and the testing set.<br>
You can modify Line 18 of split_training_set.py and split_testing_set.py to resize each patch, or modify Line 19 of split_training_set.py and split_testing_set.py to adjust the number of patches cropped from each image.<br>
The smaller the patch size, the more patches should be cropped, or the model is at risk of underfitting; conversely, the larger the patch size, the less patches should be cropped, or the model is at risk of overfitting.<br>
Then we can use the clipped patches for training and testing.<br>

### Execute the Training Code
```python  
python train_patch.py
```

After the training, the weight file UNet_patch.pth is generated in the home directory.<br>
We provide our weight file pretrained using the DRIVE dataset (loss functions during training include cross-entropy loss and dice loss) .<br>

link:<br>
https://pan.baidu.com/s/1-1CpGxDRvKkPiI0AztKVtA<br>
Extract code:<br>
vvlh<br>

### Predict a Mask
Place an image in **png** format in the predict directory. The file name should be img.png.<br>
We have put a processed image in the predict folder. You can replace it with your own image (either an RGB image or a grayscale image) .<br>

./predict<br>
&nbsp;&nbsp;&nbsp;&nbsp;/img.png<br>

Run the prediction code.<br>
```python  
python predict.py
```
Then the output mask can be observed in the result directory, and the file name is res.png.<br>

./result<br>
&nbsp;&nbsp;&nbsp;&nbsp;/res.png<br>

