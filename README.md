# Optimizer & Scheduler 

optimzer, scheduler state 저장

<img src="https://github.com/sandokim/Optimizer_Scheduler/blob/main/images/save_model.PNG" width="100%">

optimizer 지정, scheduler 지정, 저장된 optimizer state load, 저장된 scheduler state load

<img src="https://github.com/sandokim/Optimizer_Scheduler/blob/main/images/optimize&scheduler.PNG" width="100%">

<img src="https://github.com/sandokim/Optimizer_Scheduler/blob/main/images/build optim.PNG" width="100%">

# The augmentation and regularization strategies

We include most of the augmentation and regularization strategies of [63] in training, including RandAugment [17], Mixup [77], Cutmix [75], random erasing [82] and stochastic depth [35], but not repeated augmentation [31] and Exponential Moving Average (EMA) [45] which do not enhance performance. Note that this is contrary to [63] where repeated augmentation is crucial to stabilize the training of ViT. An increasing degree of stochastic depth augmentation is employed for larger models, i.e. 0.2, 0.3, 0.5 for Swin-T, Swin-S, and Swin-B, respectively

#### Stochastic depth code & how to quote it

<img src="https://github.com/sandokim/Optimizer_Scheduler/blob/main/images/stochastic depth code.PNG" width="100%">

[Deep Networks with Stochastic Depth](https://arxiv.org/abs/1603.09382)

Stochastic depth --> Skip connection에서 Identity function만 남기고 Conv Block Drop, 이 경우 code상에서는 ReLU만 남기 때문에 ReLU가 identity function으로 사용된다 볼 수 있다.

<img src="https://github.com/sandokim/Optimizer_Scheduler/blob/main/images/stochastic depth.jpg" width="100%">

Skip connection --> Dimension matching in ResNet

<img src="https://github.com/sandokim/Optimizer_Scheduler/blob/main/images/dimension match resnet.jpg" width="100%">

# Terms

#### Inductive bias

Generalize a finite set of observation or make assumptions to perform any task at hand. This all is done by a learning algorithm of the machine. In Machine Learning, it aims to construct algorithms with the ability to learn to predict certain target outputs.

While the recent ViT/DeiT models abandon translation invariance in image classification even though it has long been shown to be crucial for visual modeling, we find that inductive bias that encourages certain translation invariance is still preferable for general-purpose visual modeling, particularly for the dense prediction tasks of object detection and semantic segmentation.

# Data Conversion

# Eqaulity and Ineqaulity conditions

# KKT Conditions

# Scheduler

#### What is linear warmup?

Linear Warmup is a learning rate schedule where we linearly increase the learning rate from a low rate to a constant rate thereafter. This reduces volatility in the early stages of training.

<img src="https://github.com/sandokim/Optimizer_Scheduler/blob/main/images/linear warmup.PNG" width="50%">

We employ an AdamW optimizer for 90 epochs using a linear decay learning rate scheduler with a 5-epoch linear warm-up.

# Computing resources

##### FLOPS

플롭스(FLOPS, FLoating point Operations Per Second)는 컴퓨터의 성능을 수치로 나타낼 때 주로 사용되는 단위이다. 초당 부동소수점 연산이라는 의미로 컴퓨터가 1초동안 수행할 수 있는 부동소수점 연산의 횟수를 기준으로 삼는다.

##### Gradient checkpointing

Gradient Checkpointing is a method used for reducing the memory footprint when training deep neural networks, at the cost of having a small increase in computation time.
