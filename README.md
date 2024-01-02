# Local-Enhanced-Method-Based-Retinal-Vessel-Segmentation-System

# Download Dataset

## DRIVE Dataset  
link:<br>
https://pan.baidu.com/s/1nk0EmKEBVhtKAnctdo4veA<br>
Extract code:<br>
8nel<br>

## STARE Dataset  
link:<br>
https://pan.baidu.com/s/1TeXuIS21OfRLoh6DiwZuIg<br>
Extract code:<br>
o9sd<br>

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
