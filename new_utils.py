"""
   Use to create your own functions for reuse 
   across the assignment

   Inside part_1_template_solution.py, 
  
     import new_utils
  
    or
  
     import new_utils as nu
"""

def scale_data(X):
    
    scaled_X = (X - X.min()) / (X.max() - X.min())
    
    return scaled_X


def compute_acc_confusion_matx(confusion_matrix):
    """
    Calculate accuracy from a confusion matrix.
    """

    TruePositive = confusion_matrix[1, 1]  # True Positives
    TrueNegative = confusion_matrix[0, 0]  # True Negatives
    total_samples = confusion_matrix.sum() 

    accuracy = (TruePositive+ TrueNegative) / total_samples
    
    return accuracy





