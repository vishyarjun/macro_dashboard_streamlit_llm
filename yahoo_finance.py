import yfinance as yf
from datetime import datetime, date, timedelta
from tech_analysis import TA
import pandas as pd

class YahooFinanceInterface:
    def __init__(self):
        self.interval = '1d'
        self.period  = '1y'
        self.file_path = "./data/"
        

    
    def convert_to_epoch(self, given_date):
        unix_epoch_time = int(datetime.combine(given_date, datetime.now().time()).timestamp())
        return unix_epoch_time
    
    def download_data(self, symbol):
        print(symbol)
        sym = yf.Ticker(symbol)
        his = sym.history(interval=self.interval, period=self.period)
        his.columns = his.columns.str.upper()
        his = TA.calculate_technicals(his)
        
        if his is not None or not his.empty:
            print(his.head())
            full_path = f'{self.file_path}{symbol}.csv'
            his.to_csv(full_path)
        return True

    def graph_data(self, symbol):
        csv_file_path = f'{self.file_path}{symbol}.csv'
        df = pd.read_csv(csv_file_path, usecols=['Date', 'CLOSE'])
        return df
    
    def get_custom_graph_data(self, symbols, cols):
        merged_df = pd.DataFrame()
        cols = ["Date"] + cols
        for symbol in symbols:
            
            csv_file_path = f'{self.file_path}{symbol}.csv'
            df = pd.read_csv(csv_file_path, usecols=cols)
            df['Symbol'] = symbol
            
            merged_df = pd.concat([merged_df, df], ignore_index=True)
        
        merged_df = merged_df.dropna(subset=['RSI14'])
        
        return merged_df






yfi = YahooFinanceInterface()
