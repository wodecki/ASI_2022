import numpy as np
import pandas as pd
from datetime import date, datetime
import os.path

# Read model evaluation results
eval_results = pd.read_csv('evaluation/model_eval.csv')

last_run = eval_results['time_stamp'].max()

# Prepare data for tests
RMSE_logs = eval_results[eval_results['metric']=='RMSE']
r2_logs = eval_results[eval_results['metric']=='r2']

last_RMSE = RMSE_logs[RMSE_logs['time_stamp']==last_run]['score'].values[0]
all_other_RMSE = RMSE_logs[RMSE_logs['time_stamp']!=last_run]['score'].values

last_r2 = r2_logs[r2_logs['time_stamp']==last_run]['score'].values[0]
all_other_r2 = r2_logs[r2_logs['time_stamp']!=last_run]['score'].values


### Hard test ###

# For RMSE, we identify drift (print TRUE) if the new RMSE is larger than the mean of all the past RMSE
hard_test_RMSE = last_RMSE > np.mean(all_other_RMSE)
# it obviously may be set as a fixed value, like
# hard_test_RMSE = last_RMSE > 1.0

# For r2, we identify drift (print TRUE) if the new R2 is smaller than the mean of all the past r2
hard_test_r2 = last_r2 < np.mean(all_other_r2)
# it obviously may be set as a fixed value, like
# hard_test_r2 = last_r2 < 0.7

print('\nLegend: \nTRUE means the model has drifted. FALSE means the model has not.')

print('\n.. Hard test ..')
print('RMSE: ', hard_test_RMSE, '  R2: ', hard_test_r2)

### Parametric test ###
# For RMSE, we identify drift (print TRUE) if the new RMSE is larger than the mean of all the past RMSE + 2*std of all the past RMSE
param_test_RMSE = last_RMSE > np.mean(all_other_RMSE) + 2*np.std(all_other_RMSE)

# For r2, we identify drift (print TRUE) if the new R2 is smaller than the mean of all the past r2 - 2*std of all the past r2
param_test_r2 = last_r2 < np.mean(all_other_r2) - 2*np.std(all_other_r2)

print('\n.. Parametric test ..')
print('RMSE: ', param_test_RMSE, '  R2: ', param_test_r2)