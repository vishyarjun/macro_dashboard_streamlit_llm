import requests
import pandas as pd
from reference_data import macroeconomic_indicators
class IMFInterace:
    def __init__(self): 
        self.url = 'https://www.imf.org/external/datamapper/api/v1/'
        self.indicators = 'indicators'
        self.new_dict = {}
        self.country = 'IND'
        self.source_data = './macro_data.csv'
    

    

    def get_all_indicators(self, display_ui):
        url = self.url + self.indicators
        resp = requests.get(url)
        if resp.status_code==200:
            resp = resp.json()['indicators']
            if not display_ui:
                return resp.keys()
            else:
                for key in macroeconomic_indicators:
                    
                    self.new_dict[resp[key]['label']] = (key,resp[key]['description'])
                


                return self.new_dict
    
    def get_symbol_desc(self,keys):
        
        soln = []
        for key in keys:
            
            soln.append(self.new_dict[key])
        return soln

    def get_indicator_data(self,symbol):
        
        data_url =  self.url + symbol+'/'+self.country
        resp = requests.get(data_url).json()
        if resp.get("values",None) is None:
            return

        json =  resp["values"][symbol][self.country]
        years = list(json.keys())
        values = list(json.values())
        df = pd.DataFrame({"Year": years, symbol: values})
        df.set_index('Year',inplace=True)
        return df
    
    def refresh_data(self):
        df = pd.DataFrame()
        all_indicators = self.get_all_indicators(True)
        
        for i, ind in enumerate(macroeconomic_indicators):
            print(i, ind)
            df_temp = self.get_indicator_data(ind)
            df = pd.concat([df, df_temp], axis=1)
            if i<100:
                yield 1
            else:
                yield 0
        
        df.sort_values(by='Year', inplace=True)
        df.to_csv(self.source_data)
        return 1

            
    
    def get_graph_data(self,symbols):
        if not symbols:
            return
        df = pd.read_csv(self.source_data)
        symbols = ["Year"] + symbols
        df = df[[symbol for symbol in symbols if symbol in df.columns]]
        #df.set_index('Year',inplace=True)
        df.sort_values(by='Year', inplace=True)
        df = df.dropna()
        return df




imf = IMFInterace()
imf.get_all_indicators(True)