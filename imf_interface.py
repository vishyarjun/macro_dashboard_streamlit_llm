import requests
import pandas as pd
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
                for key in resp:
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
        for ind in self.get_all_indicators(False):
            print(ind)
            df_temp = self.get_indicator_data(ind)
            df = pd.concat([df, df_temp], axis=1)
        
        df.sort_values(by='Year', inplace=True)
        df.to_csv(self.source_data)
            
    
    def get_graph_data(self,symbols):
        if not symbols:
            return
        df = pd.read_csv(self.source_data)
        symbols = ["Year"] + symbols
        df = df[symbols]
        #df.set_index('Year',inplace=True)
        df.sort_values(by='Year', inplace=True)
        df = df.dropna()
        return df




imf = IMFInterace()
#imf.refresh_data()