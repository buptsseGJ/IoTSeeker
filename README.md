
# IoTSeeker
## I. Introduction
It's a function semantic learning based cross-platform binary vulnerability search approach for IoT devices.

## II. File functionality
- `1_gen_idb_file.py`: it generates the idb files of binary based on IDA Pro.
- `2_gen_features.py`: it extracts original instruction features of basic blocks from idb files. 
- `3_gen_train_dataset.py`: it generates the training dataset.
- `4_gen_tfrecord_iotseeker.py`: it transforms both the instruction features, graph representations of samples into a input file in the tfrecord format, which is used to train the model. 
- `5_train_by_list_iotseeker.py`: it trains the model based on the input file in the tfrecord format.
- `6_gen_search_tfrecord_iotseeker.py`: it transforms both the instruction features, graph representations of samples containing the vulnerability into a input file in the tfrecord format.
- `7_search_by_list_iotseeker.py/7_search_model_iotseeker.py`: it conducts the known vulnerability search for binaries across compilation scenarios.


## III. Usage
1. We need modify the `config.py` file. All the dependency directories can be modified here. Simple modification is listed as following, but it need to follow the directory structure we defined:
```
IDA32_DIR = "installation directory of 32-bit IDA Pro program"
IDA64_DIR = "installation directory of 64-bit IDA Pro program"
```
2. We put the programs to be searched in the `0_Libs/search_program` directory.
3. We run the `command.py` file to generate the labeled semantic flow graphs and extract initial numerical vectors for basic blocks. The result files should be placed in the `1_Features/search_program` directory.
4. We execute the `search_by_list_iotseeker.py` file to obtain embedding vectors of the functions and get the function list in descending order of similarity scores.