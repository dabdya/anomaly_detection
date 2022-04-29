from abc import ABC, abstractmethod
from ipywidgets import IntProgress
from IPython.display import display
from utils.metrics import far, mar, f1_score

import matplotlib.pyplot as plt
import pandas as pd

class Predictor(ABC):
    @abstractmethod
    def make_prediction(self, df):
        """Must return predictions by df"""
        pass
    
class Pipeline:
    
    def __init__(self, print_scores=True, show_plots=True):
        self.print_scores = print_scores
        self.show_plots = show_plots
        
        self.all_predictions = []
        
    def _show_bar(self, size):
        bar = IntProgress(
            min=0, max=len(size), 
            description="Computing", style={'bar_color': '#61dc8a'},)
        
        display(bar)
        return bar
    
    def _calc_scores(self, list_of_df, predictions):
        true_outlier = pd.concat([df.anomaly for df in list_of_df])
        pred_outlier = pd.concat(predictions)
        f1 = f1_score(true_outlier, pred_outlier)
        far_score = far(true_outlier, pred_outlier)
        mar_score = mar(true_outlier, pred_outlier)
        return f1, far_score, mar_score
    
    def _print_scores(self, **kwargs):
        for score_name, score_value in kwargs.items():
            print(f"{score_name} = {score_value}\n")

    def _show_plots(self, list_of_df, predictions):
        for i in range(len(predictions)): 
            plt.figure(figsize=(12,3))
            plt.title(f"dataframe №{i+1}")  
            list_of_df[i].anomaly.plot(label='true')
            predictions[i].plot(label='predicted')
            plt.legend()
        
    def run(self, list_of_df, predictor, anomaly_description=""):
        
        print(f"Anomaly: {anomaly_description.lower()}")
        bar = self._show_bar(size=list_of_df)
    
        predictions = []
        for df in list_of_df:
            predictions.append(predictor.make_prediction(df))   
            bar.value += 1
        
        f1, far_score, mar_score = self._calc_scores(list_of_df, predictions)
        if self.print_scores:
            self._print_scores(F1=f1, FAR=far_score, MAR=mar_score)

        if self.show_plots:
            self._show_plots(list_of_df, predictions)
            
        self.all_predictions.append(predictions)
            
        return f1, far_score, mar_score 
