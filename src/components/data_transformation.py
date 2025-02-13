import os, sys
from src.logger import logging
from src.exception import CustomException

from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.utils import save_object




@dataclass
class DataTransformationConfig:
    preprocesso_obj_file_path = os.path.join("artifact", "preprocessor.pkl")
    
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
        
    def get_data_transformer_object(self):
        
        """ 
        This function is responsible for data transformation
        """
        
        try:
            
            numerical_columns = ['reading_score', 'writing_score']
            categorical_columns = ['gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course']
        
            num_pipeline = Pipeline(
                
            steps=[
                ("imputer", SimpleImputer(strategy='median')),
                ("scaler", StandardScaler())
            ]
        )
            
            
            cat_pipeline = Pipeline(
                
                steps=[
                    ("Imputer",SimpleImputer(strategy="most_frequent")),
                    ("One_hot_encoder", OneHotEncoder()),
                    
                ]
                
            )
            logging.info("Numerical columns Standered scaling completed")
            logging.info("Categoricale Columns encoding completed")
            
            preprocessor = ColumnTransformer(
                transformers=[
                ('numerical_pipeline', num_pipeline, numerical_columns),
                ("categorical_pipeline", cat_pipeline, categorical_columns)
                ]
            )
            
            return preprocessor
        except Exception as e:
            
            raise CustomException(e,sys) from e 
            
            
    def initiate_data_transformation(self, train_path,test_path):
        
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info(" Reading train adn test data completed")
            
            logging.info("obtaining preprocessing object")
            
            preprocessor_obj = self.get_data_transformer_object()
            
            target_column_name = 'math_score'
            

            
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis= 1)
            target_feature_train_df = train_df[target_column_name]
            
            
            input_feature_test_df = test_df.drop(columns=[target_column_name], axis= 1)
            target_feature_test_df = test_df[target_column_name]
            
            logging.info("Applying preprocessing object on training dataframe and testing dataframe")
            
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)
            
            
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            
            """ 
            np.c_: This is a shorthand for concatenating arrays along the second axis (columns). It horizontally stacks the input features and the target variable.
            input_feature_train_arr: The transformed training input features.
            np.array(target_feature_train_df): The target variable (e.g., "math_score") for the training set, converted to a NumPy array.
            
            """
            
            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]
            
            save_object(
            file_path = self.data_transformation_config.preprocesso_obj_file_path,
            obj = preprocessor_obj
            )
            
            logging.info("Saved object")
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocesso_obj_file_path
            )
            
        except Exception as e:
            raise CustomException(e,sys) from e 
        
        
        
        