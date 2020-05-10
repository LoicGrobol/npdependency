# Non projective dependency parsing


This is a repository for non projective dependency parsing stuff.


It currently hosts a graph-based dependency parser inspired by the paper of [(Dozat 2017)](https://nlp.stanford.edu/pubs/dozat2017deep.pdf). 
Contrary to Dozat, the parser performs its own tagging and can use several lexers such as FastText, Bert and others. It has been specifically designed within the [Flaubert](https://github.com/getalp/Flaubert) initiative. 

I advise to have a GPU with at least 12GB graphical memory. With smaller GPUs,
using a BERT preprocessor will become difficult. The parser comes with two pretrained models ready for parsing French.


Parsing task
-----------
The parsing task (or prediction task) assumes you have an already trained model in the directory MODEL. 
You can parse a file FILE in conll format (with empty annotations, just words) with the command:

```
python graph_parser.py  --pred_file FILE   MODEL/params.yaml
```

This results in a parsed file called `FILE.parsed`. The `MODEL/params.yaml` is the model hyperparameters file. 
An example model is stored in the `default` directory. The file `default/params.yaml` is an example of such parameter file.

We advise to use the `flaubert` model which is stored in the flaubert directory. Depending on the model, the parser will be more or less fast and more or less
accurate. We can however expect the parser to process several hundred sentences per second with a decent GPU. 
The parameter file provides an option for controlling the GPU actually used for performing computations.

Pretrained models
----------------
We provide some pretrained models :

| Model name | Language | device | LAS  | speed | Comment | Download link
| ---------- | -------- | ------ | ---- | ----- | ------- | -------------
|   default  | french   | GPU/CPU| 81.5 | fast  | French treebank only          | [download model](http://www.linguist.univ-paris-diderot.fr/~bcrabbe/depmodels/default.tar.gz)
|   flaubert | french   | GPU    | xxxx | average| FlaubertBase+French treebank | [download model](http://www.linguist.univ-paris-diderot.fr/~bcrabbe/depmodels/flaubert.tar.gz)

The reader may notice a difference with the results published in [(Hang et al 2020)](https://arxiv.org/abs/1912.05372).
The difference comes from the fact that this parser predicts part of speech tags
while the version described in [(Hang et al 2020)](https://arxiv.org/abs/1912.05372) required predicted tags as part of its input.

Training task
------------

Instead of using a pretrained model, one can train his own model.
Training a model with BERT definitely requires a GPU. Unless you have a GPU with a very large amount of onboard memory, I advise to use 
very small batch sizes (2, 4, 8, 16, 32, 64) for training. Otherwise you are likely to run out of memory.

Training can be performed with the following steps:

  1. Create a directory MODEL for storing your new model
  2. `cd` to MODEL 
  3. copy the `params.yaml` file from another model into MODEL
  4. Edit the `params.yaml` according to your needs
  5. Run the command:
```
python graph_parser.py  --train_file TRAINFILE --dev_file DEVFILE  params.yaml
```
after some time (minutes,hours,days...) you are done and the model is ready to run (go back to the parsing section)

  








