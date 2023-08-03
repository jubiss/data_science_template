import sys,os
sys.path.append(os.getcwd())
import pandas as pd
def profile_df(df, report_path):
    from ydata_profiling import ProfileReport

    profile = ProfileReport(df, title='Data Profiling')
    profile.to_file(r'docs/data/Real Estate data Profiling.html')

processed_dataframe = r'data/processed/.csv'
df = pd.read_csv(processed_dataframe)
report_path = r'docs/data/Data Profiling.html'
profile_df(df, report_path)