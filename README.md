# Tiny ML Classifier
Tiny ML classifier - Glasses or No Glasses

## Todo (09.09.2021)

- [x] Create infrastructure for Git
- [x] Quick R&D
- [x] Free data
- [x] Transfer
- [x] Augmentation data
- [ ] Pytorch or TF (as tflite - deployment)
- [ ] free skeleton model for init weights (I think it will be EfficientNet-Lite* models, MobileNetV2 or ResNet50) 
- [ ] Training Loop (Use API for convertin to Tiny models - for example .tflite)
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

- Go to [kaggle.com](kaggle.com) and download Free dataset from -
[Here](https://www.kaggle.com/jorgebuenoperez/datacleaningglassesnoglasses)


### Transfer and Augmentation

- Tools for Augmentation data and exporting many formats[RoboFlow](roboflow.com)

- From Scratch Augmentation - use [Albumentations](https://albumentations.ai/docs/)