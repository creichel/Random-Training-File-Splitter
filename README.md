# Random-Training-File-Splitter
Wanna split your dataset scientifically into test and training sets? This is a small python script that randomly separates a set of files into train and test file set given by a predefined split strategy.

To use this, simply copy it into your dataset folder and call
```
python random_training_file_splitter.py
```

You can also set the following parameters:

- `--path`: The path to your dataset. Default the current path to the script.
- `--train_dir_name`: The name of the train directory. Default `train`.
- `--test_dir_name`: The name of the test directory. Default `test`.
- `--file_extension`: The file extension you are searching for. Default `jpg` .
- `--split_strategy`: The split strategy, so to say the weight whether a file will be chosen as test or training file.
