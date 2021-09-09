# Tiny ML Classifier
Tiny ML classifier - Glasses or No Glasses

## Todo (09.09.2021)

- [x] Create infrastructure for Git
- [x] Quick R&D
- [x] Free data
- [x] Transfer
- [x] Augmentation data
- [x] Pytorch or TF (as tflite)
- [x] free skeleton model for init weights (I think it will be EfficientNet-Lite* models, MobileNetV2 or ResNet50) 
- [x] Training Loop (Use API for convertin to Tiny models - for example .tflite)
- [ ] Create inference demo
- [ ] Optimised
- [ ] Bonus ---> 
  - [ ] Deployment for example RPi (with minimal memory - like RPi 3 with 1GB memory and without threading CPU)  
  - [ ] Documentation on GitHub
  - [ ] Video demonstration realtime classification


## Clone Tily ML Classifier
```
git clone https://github.com/rvjenya/tiny-ml-classifier.git
or use ssh - git@github.com:rvjenya/tiny-ml-classifier.git
cd tiny-ml-classifier
```

## Up env
```
./install.sh

```


### Dataset

- Go to (kaggle.com) and download Free dataset from -
[Here](https://www.kaggle.com/jorgebuenoperez/datacleaningglassesnoglasses)


### Transfer and Augmentation

- Tools for Augmentation data and exporting many formats (roboflow.com)

- From Scratch Augmentation - use [Albumentations](https://albumentations.ai/docs/)

### Use TF classification notebook

- Open on your PC with GPU or Colab (I've attached colab version but you can export it to your GPU env)
[![Open All Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1hThmbqVvYiMUD5AOORX_TXjLq2XiH-DO?usp=sharing)

```
https://colab.research.google.com/drive/1hThmbqVvYiMUD5AOORX_TXjLq2XiH-DO?usp=sharing

```
#### GPU Setting
Edit > Notebook settings or Runtime > Change runtime type and select GPU as Hardware accelerator

### Training

- I use **mobilenet_v2_100_224** with **Bach size = 32**
- You can change these parameters and ReTrain your model. Just try many experiments while you will be satisfied. 

#### Save TF and TFLite models

Final models .pb and .tflite [here](https://github.com/rvjenya/tiny-ml-classifier/tree/main/model)
You can test my another tflite models with **number calibration** = 45 / 100 and 200 (If you want, you can try it parameters in **TFLiteConverter** step)

My result of training by 10 Epoch:

![Image of plt](https://github.com/rvjenya/tiny-ml-classifier/blob/main/doc/rvjenya-doc-git-00001.png)
