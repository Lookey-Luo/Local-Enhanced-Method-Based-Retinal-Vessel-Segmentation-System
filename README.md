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
Place the dataset in the specified directory as required. For example, the DRIVE dataset needs to be placed in the following format:<br>
./DRIVE<br>
/train<br>
    /image<br>
      /01_training.png<br>
      /02_training.png<br>
      /03_training.png<br>
      ...<br>
      /20_training.png<br>
    /label<br>
  /test<br>
    /image<br>
    /label<br>

## Without Patch

## With Patch
