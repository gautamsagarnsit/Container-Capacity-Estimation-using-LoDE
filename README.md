# 2021 Intelligent Sensing Winter School- The CORSMOL Challenge Submissio
## Objective: To Estimate capacity of Container-like objects
### Dataset: CORSMOL Dataset: [CORSMAL Containers dataset](http://corsmal.eecs.qmul.ac.uk/containers.html)
### Method: Multi-view shape estimation of transparent containers(LoDE)  [LoDE webpage](http://corsmal.eecs.qmul.ac.uk/LoDE.html)


## Description
LoDE (Localisation and Object Dimensions Estimator) is a method for jointly 
localising container-like objects and estimating their dimensions using 
two wide-baseline, calibrated RGB cameras. Under the assumption of circular 
symmetry along the vertical axis, LoDE estimates the dimensions of an object 
with a generative 3D sampling model of sparse circumferences, iterative shape 
fitting and image re-projection to verify the sampling hypotheses in each camera 
using semantic segmentation masks (Mask R-CNN).

## Demo 
Run LoDE with a sample of the CORSMAL Containers dataset (e.g. object 15, lighting 0, and background 0; contained on ./dataset/images)
```
1. python main.py --object=15 --lighting=0 --background=0 --draw
```
```
2. python main.py --object=1 --lighting=1 --background=1
```

## Output
LoDE outputs two results:
* Dimensions estimation of the height and width of the container in milimeters in results/estimation.txt
* Visual representation of the container shape in results/*.png. The visual representation can be removed by omitting the --draw commands


## Reference
[1] A. Xompero, R. Sanchez-Matilla, A. Modas, P. Frossard, and A. Cavallaro, 
_Multi-view shape estimation of transparent containers_, Published in the IEEE 
2020 International Conference on Acoustics, Speech, and Signal Processing,
Barcelona, Spain, 4-8 May 2020.

