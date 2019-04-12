# Training documentation of FastRCNN_circle


## 1. Sort you picture
Save the pictures with annotations in C://caffe/annos/

## 2. Convert ImageJ-Annotations (ROI) to BB-Circle-XMLs

1. Open convert_imageJ_annos_to_BB_cirle_defs.m
2. Change following variables:
    * Input dir
    * output dir
    * Image type = 'bmp' # should set 'bmp' for SOPAT pictures
    * class names: 'B, T' # 'Blasen' and 'Tropfen'
3. Also check Fiji/ImageJ version - path name

## 3. Check if all annotations are correct

1. Open gui_check_circle_annos.m

## 4. Create VOC training data struct from annos BB

1. Open Visual Studio
2. Open project --> create VOC training data struct from annos BB
3. Right click on Python Environment -> Add/Remove Python Environment
4. Choose Miniconda2
5. Click on Py.Data
6. Change following variables:
    * annoDir
    * resultDir
    * scales
    * fractionOfTrainingData
    * if necessary other variables under user options (From trainval.txt to test.txt, sort representative and all kind of images)
7. Click run

## 5. Create Symlink / Softlink

### Manually
Do this if you only have one or a few folders

1. Create DNNs/dev/.../data
2. Create VOCdevkit0020_folder name "imdbSubSetNames"
3. Create Subfolder "results\VOC0020\Main"
4. Open cmd as administrator --> `cd` to target folder
5. Run `mklink /d VOC0020 source_path_name`

### Batch mode
1. Open python_tools
2. Run `conda environment list` - check if `py36` is available
3. Run `activate py36`
4. Open C:\DNNs\dev\DNNs_python_tools\inputDataFromVocFolders.py
5. change `rootVOCFolder` and `fasterRCNNDataFolder`
6. Run `python inputDataFromVocFolders.py` in cmd

## 6. Start the training

1. Open Visual Studio --> perform_net_training.sln
2. Open project --> create VOC training data struct from annos BB
3. Right click on Python Environment -> Add/Remove Python Environment
4. Choose Miniconda2
5. Click on Py.Data --> perform_net_training.py
7. Important things to configure:
    * showScores = False / # True
    * In the solver.prototxt -- to change:
        * base_lr
        * gamma
        * stepsize
    * Initial Weight using orig.caffemodel
    * Move or delete Old Voc data from output folder
    * YML-Data for configuration
    * PerformTesting on test (also possible with trainval)
    * Change `imdbSubSetNames` to folder name after "VOC0020_"
8. Edit YML Data, you can find it by copying path from python file. Configure following important variables:
    * Scales: Aufloesung
    * Region Proposal Net
    * RPN_PRE_ hochschrauben
    * PIXEL_MEAN: [55, 55, 55]
    * CONF_THRESH: 0.8
9. Configure Config.py
10. Click run

# More Tipps

## To detect 'big' Particles
1. Set down the `CONF_THRESH` in YML data
2. Do more annotations with 'big' droplets/bubbles
3. Scale down the picture

## Delete VOC-Folder
Always delete VOC-Folders or move them to output.

## Perform Net-Training
* Set up YML RPN_PRE_NMS_TOP_N & RPN_POST_NMS_TOP_N as high as possible (only change it in Test)
* in Testblock: CONF_THRESH: 0.5
* Scale the picture (zusammen mit PRE & POST)

## FineTuning
* Change `stepsize` to 10.000
* Do not change base_lr: 0.00005
* nur mit den Gasblasenbildern
