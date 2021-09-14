# Tiny ML Classifier
Tiny ML classifier - Glasses or No Glasses

![Image](https://github.com/rvjenya/tiny-ml-classifier/blob/main/doc/all_02.png)

![DEMO](https://github.com/rvjenya/tiny-ml-classifier/blob/main/doc/infer-test.png)

## Todo (09.09.2021)

- [x] Create infrastructure for Git
- [x] Quick R&D
- [x] Free data
- [x] Transfer
- [x] Augmentation data
- [x] Pytorch or TF (as tflite)
- [x] free skeleton model for init weights (I think it will be EfficientNet-Lite* models, MobileNetV2 or ResNet50) 
- [x] Training Loop (Use API for convertin to Tiny models - for example .tflite)
- [x] Create inference demo
- [x] Optimised
- [x] Bonus ---> 
  - [x] Deployment for example RPi (with minimal memory - like RPi 3 with 1GB memory and without threading CPU)  
  - [x] Documentation on GitHub
  - [x] Video demonstration realtime classification from Camera


## Clone Tiny ML Classifier
```
git clone https://github.com/rvjenya/tiny-ml-classifier.git
or use ssh - git@github.com:rvjenya/tiny-ml-classifier.git
cd tiny-ml-classifier
```

## Up env

Create env with Python3.7

```
python3.7 -m venv venv

source venv/bin/activate

```

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

- Done Models:
  - **mobilenet_v2** (will be faster)
  - **Inception_v3**

For all models I've made FP16 version tflite - you can use it on GPU.

#### Save TF and TFLite models

Final models .pb and .tflite [here](https://github.com/rvjenya/tiny-ml-classifier/tree/main/model)
You can test my another tflite models with **number calibration** = 45 / 100 and 200 (If you want, you can try it parameters in **TFLiteConverter** step)

### Training result

My result of training by 10 Epoch:

![Image of plt](https://github.com/rvjenya/tiny-ml-classifier/blob/main/doc/rvjenya-doc-git-00001.png)

#### Test infer

Testing classification:

![Image of plt](https://github.com/rvjenya/tiny-ml-classifier/blob/main/doc/rvjenya-doc-git-00000.png)
![Image of plt](https://github.com/rvjenya/tiny-ml-classifier/blob/main/doc/rvjenya-doc-git-00002.png)


### Realtime Inference

![DEMO](https://github.com/rvjenya/tiny-ml-classifier/blob/main/doc/infer-test.png)

If you need specific architecture you can use these models:

- FP32 (Full)
- FP16 (optimisation for GPU)

#### for Realtime Camera Demo use: 

```

(venv) python cam-demo.py

```


#### for Raspberry Pi Camera demo use
![DEMO](https://github.com/rvjenya/tiny-ml-classifier/blob/main/doc/RPi-infer.png)

```
python3 classify-cam-rpi.py \
  --model /model/tflite/optimise_to_3Mb/MobileNetV2/model.tflite \
  --labels /model/tflite/optimise_to_3Mb/MobileNetV2/labels.txt

```
