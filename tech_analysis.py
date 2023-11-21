import pandas as pd
import numpy as np
from talib import RSI, EMA, stream
from ta.volatility import KeltnerChannel
class TechAnalysis:
    def __init__(self):
        self.ema_period = 13
        self.rsi_period = 7
        self.stochastic_period = 7
        self.rsi_divergence_period = 14

    def calculate_technicals(self, df):
        try:
            if len(df) >= 50:
                df['RSI14'] = RSI(df['CLOSE'], timeperiod=self.rsi_divergence_period)
                indicator_kc = KeltnerChannel(high=df["HIGH"],low=df["LOW"],close=df["CLOSE"], window=50, window_atr=50,fillna=False,multiplier=5, original_version=False)
                df["KC_UPPER"] = indicator_kc.keltner_channel_hband()
                df["KC_MIDDLE"] = indicator_kc.keltner_channel_mband()
                df["KC_LOWER"] = indicator_kc.keltner_channel_lband()
            else:
                print('else')
                df['RSI14'] = np.nan
                print('else1')
                df["KC_UPPER"] = np.nan
                print('else2')
                df["KC_MIDDLE"] = np.nan
                print('else3')
                df["KC_LOWER"] = np.nan
                print('else4')
            return df
        except Exception as e:
            print('error while calculating technicals')
            print(f'exception occured {e}')


    def get_current_rsi_and_stoch(self,tick,ltp,df):
        new_data = {
            "CLOSE": [ltp],
            "OPEN": [ltp], 
            "HIGH": [ltp],
            "LOW": [ltp]
        }
        #new_data = pd.DataFrame(new_data)
        #df = pd.concat([df, new_data], ignore_index=True)
        last_row = df.iloc[-1]
        return last_row["RSI"]
        
        ema = EMA(df['CLOSE'],timeperiod=self.ema_period)
        rsi = stream.RSI(ema, timeperiod=self.rsi_period)
        return rsi
    
    def get_current_keltner(self,open, high, low, close,df):
        last_row = df.iloc[-1]
        return last_row["KC_UPPER"],last_row["KC_MIDDLE"],last_row["KC_LOWER"]


TA = TechAnalysis()