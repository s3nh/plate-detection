# Licence Plate MobilenetV2-ssd 

First attemption to built licence-plate recognizer. 
Main task: It has to be light enough to run efficiently on Movidius Intel Compute Stick  (10 FPS will be great)


#### Architecture

First attempt:

MobilenetV2-SSD 

[Link to MobileNetV2 paper](https://arxiv.org/pdf/1801.04381.pdf)


- Depthwise Separable convolutions

![Depthwise separable conv image](https://miro.medium.com/max/863/1*VvBTMkVRus6bWOqrK1SlLQ.png)



- Inverted Residual Block 

![Inverted Residual Blocks Image](https://miro.medium.com/max/592/1*5Jdh_PDTXp0uhF8c79TEsQ.png)


- Skip Connections  and residual blocks 

![Residual block image](https://kharshit.github.io/img/resnet_block.png)




#### Assumptions

#FIXME

#### Installation

```
python setup.py install 
```

#### Technology

[Intel Neural Compute Stick 2](https://software.intel.com/en-us/neural-compute-stick)

- GTX 1060 (6gb)


and yes, I am aware that Movidius does not support Pytorch objects. It is also a  some kind of challenge for me to get into TF2.

#### Sources 

Some really helpful implementations 

- [Pytorch SSD](https://github.com/qfgaohao/pytorch-ssd)




#### To dos

- Test pretrained mobilenet_v2, as it is. (in progress)
- freeze layer, modified last one 
- write some fancy image loader
- pretrain 
- test


