# Optimizer & Scheduler 동작원리

# Terms

#### Inductive bias

Generalize a finite set of observation or make assumptions to perform any task at hand. This all is done by a learning algorithm of the machine. In Machine Learning, it aims to construct algorithms with the ability to learn to predict certain target outputs

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
