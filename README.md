# Local-Enhanced-Method-Based-Retinal-Vessel-Segmentation-System

# Download Dataset

## DRIVE Dataset  
link:  
https://pan.baidu.com/s/1nk0EmKEBVhtKAnctdo4veA  
Extract code:  
8nel  

## STARE Dataset  
link:  
https://pan.baidu.com/s/1TeXuIS21OfRLoh6DiwZuIg  
Extract code:  
o9sd  

We selected 10 images from STARE dataset as the training set and another 10 images as the test set, and converted them into grayscale images. The selected images include over-exposure and under-illumination, and low contrast in the optic disk region, which can be used to test the robustness of the model.

# Implementation
Place the dataset in the specified directory as required. For example, the DRIVE dataset needs to be placed in the following format:  
./DRIVE  
  /train  
    /image  
      /01_training.png  
      /02_training.png  
      /03_training.png  
      ...  
      /20_training.png  
    /label  
  /test  
    /image  
    /label  

## Without Patch

## With Patch
