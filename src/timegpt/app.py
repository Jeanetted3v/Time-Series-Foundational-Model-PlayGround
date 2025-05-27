import pandas as pd
from nixtla import NixtlaClient
from src.utils.settings import SETTINGS


# 1. Instantiate the NixtlaClient
nixtla_client = NixtlaClient(api_key=SETTINGS.TIMEGPT_API_KEY,)

# 2. Read historic electricity demand data
df = pd.read_csv('https://raw.githubusercontent.com/Nixtla/transfer-learning-time-series/main/datasets/electricity-short.csv')

# 3. Forecast the next 24 hours
fcst_df = nixtla_client.forecast(df, h=24, level=[80, 90])

# 4. Plot your results (optional)
nixtla_client.plot(df, fcst_df, level=[80, 90])
