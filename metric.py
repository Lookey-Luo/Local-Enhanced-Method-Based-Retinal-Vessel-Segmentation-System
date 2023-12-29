def dice_coefficient(outputs,test_label):
    smooth = 1.0
    intersection = (outputs * test_label).sum().item()
    output_num = outputs.sum().item()
    label_num = test_label.sum().item()
    coefficient = (2 * intersection + smooth) / (output_num + label_num + smooth)
    return coefficient
