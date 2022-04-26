# Cat recognition

## How to train your model
python3 retrain.py --image_dir={your image folder} --how_many_training_steps=500 --output_graph=IMG_graph.pb --output_labels=IMG_labels.txt --summaries_dir=summaries

## How to test your model
/usr/bin/python3 predict.py --image {path to your image input} --labels {path to your/}abels.txt --graph {path to your model} --input_layer Placeholder

### System configuration
#### Python
/usr/bin/python3
Python 3.7.11

### Tensorflow
tensorboard                  1.15.0
tensorboard-data-server      0.6.1
tensorboard-plugin-wit       1.8.1
tensorflow                   1.15.0
tensorflow-estimator         1.15.1
tensorflow-hub               0.12.0
tensorflow-io-gcs-filesystem 0.24.0

### Common issues
In case of errors during using preduct.py
It dependes on your model input and output labels
see model.txt to see the list of labels or run seemodel.py to create the list
