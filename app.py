
from src.logger import logging
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
 
from src.exception import CustomException

from src.components.data_ingestion import DataIngestion, DataIngestionConfig

obj = DataIngestion()
obj.initiate_data_ingestion() 
