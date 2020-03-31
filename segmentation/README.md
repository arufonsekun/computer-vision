## Image Segmentation

![](https://ai.stanford.edu/~syyeung/cvweb/Pictures3/segmentation.png)
<p align="center">Source: Introduction to Computer Vision<sup>1</sup> </p>

## Overview
This readme purpose is to briefly define what is image segmentation and explain the segmentation based algorithms core ideia used in the
code samples
[detecting-contourns](https://github.com/arufonsekun/computer-vision/tree/master/segmentation/detecting-contourns) and
[erosion-dilation](https://github.com/arufonsekun/computer-vision/tree/master/segmentation/erosion-dilation). The
techniques used in this samples are `adaptiveThreshold`, ``

### What is Image Segmentation?
Image segmentation is a important subject from Computer Vision field, that aims to divide a image into meaningful areas based
on pixels attributes. This areas describes edges and boundaries that are useful to define regions of interest, doing so
segmentation guides further techniques in processing some specifics areas instead the whole image. The segmentation are
applied in a very broad areas, an example is the software behind green screen that crop the foreground and place into a
different background.

In general, segmentation techniques are based in two pixel intensity features: **discontinuity** and **similarity**[2]. Algorithms
build on top of the first characteristic divide a image based on notably changes in pixels, the results get by appling
this kind of technique is edges for example. Algorithms that exploit pixels similarities produces an image divided into
many regions according to some criteria, there are Thresholding algorithm, region growing, region split and merging to
name some of them.

<p>
&nbsp;
</p>

![](https://raw.githubusercontent.com/arufonsekun/computer-vision/093d7f461488831a4c14d9d5c5f7ce446024e267/convolution/output/sharpengolden_gate.jpg)
&nbsp;
![](https://raw.githubusercontent.com/arufonsekun/computer-vision/093d7f461488831a4c14d9d5c5f7ce446024e267/convolution/output/edgeDetection3golden_gate.jpg)
<p align="left">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Source: The author.</p>

### References

<sup>1</sup>Available in: <https://ai.stanford.edu/~syyeung/cvweb/tutorial3.html>. Access in: 30 mar. 2020.

[2] GONZALEZ, Rafael C.. Image Segmentation. In: GONZALEZ, Rafael C.; WOODS, Richard E.. Digital Image Processing. 2. ed. S.l.: Pearson Education, 2004. Cap. 10. p. 567-568.
