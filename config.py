#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# IDA Path

IDA32_DIR = "\\media\\IDA_Pro_v6.4_Linux\\idaq"
IDA64_DIR = "\\media\\IDA_Pro_v6.4_Linux\\idaq64"

ROOT_DIR = os.path.dirname(os.path.realpath(__file__)) #  The path of the current file


CODE_DIR = ROOT_DIR
O_DIR = ROOT_DIR+ os.sep + "0_Libs"                  #  The root path of All the binary file
IDB_DIR = ROOT_DIR+ os.sep + "0_Libs"                #  The root path of All the idb file
FEA_DIR = ROOT_DIR+ os.sep + "1_Features"            #  The root path of  the feature file
DATASET_DIR = ROOT_DIR+ os.sep + "2_Dataset"
TFRECORD_IOTSEEKER_DIR = ROOT_DIR+ os.sep + "3_TFRecord" + os.sep + "IoTSeeker"
MODEL_IOTSEEKER_DIR = ROOT_DIR+ os.sep + "4_Model" + os.sep + "IoTSeeker"
CVE_FEATURE_DIR = ROOT_DIR+ os.sep + "5_CVE_Feature"
SEARCH_IOTSEEKER_TFRECORD_DIR = ROOT_DIR+ os.sep + "6_Search_TFRecord" + os.sep + "IoTSeeker"
SEARCH_RESULT_IOTSEEKER_DIR = ROOT_DIR+ os.sep + "7_Search_Result" + os.sep + "IoTSeeker"

# if convert all binary files into disassembly files
STEP1_GEN_IDB_FILE = True
STEP1_PORGRAM_ARR=["openssl"]#"openssl","coreutils","busybox","CVE-2015-1791"

# if extract feature file
STEP2_GEN_FEA = True
STEP2_PORGRAM_ARR=["openssl"]  #  all the project name"openssl",,"busybox","coreutils","CVE-2015-1791"
STEP2_REMOVE_DUP = True
STEP2_PORGRAM_ARR=["search_program"]  #  all the project name
STEP2_CVE_OPENSSL_FUN_LIST = {'ssl3_get_new_session_ticket':'CVE-2015-1791', 'OBJ_obj2txt':'CVE-2014-3508'}

# if train train dataset
STEP3_GEN_DATASET = False
STEP3_PORGRAM_ARR = ["openssl"]#"openssl","coreutils","busybox",
TRAIN_DATASET_NUM = 50000

# if train IoTSeeker TFrecord
STEP4_GEN_TFRECORD_VUL = False

STEP5_TRAIN_IOTSEEKER_MODEL = False
SETP5_IF_RESTORE_IOTSEEKER_MODEL = False
STEP5_IOTSEEKER_MODEL_TO_RESTORE = ""

STEP6_CVE_FUN_LIST = {'CVE-2015-1791':'ssl3_get_new_session_ticket', 'CVE-2014-3508':'OBJ_obj2txt'}
STEP6_GEN_SEARCH_IOTSEEKER_TFRECORD = False
STEP6_SEARCH_PROGRAM_ARR = ["search_program"]

STEP7_IF_SEARCH_IOTSEEKER=True
STEP7_SEARCH_IOTSEEKER_MODEL="iotseeker-model_final.ckpt"
