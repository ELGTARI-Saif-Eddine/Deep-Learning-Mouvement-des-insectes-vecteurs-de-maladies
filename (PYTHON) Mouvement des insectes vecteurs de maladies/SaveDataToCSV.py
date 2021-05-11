import pandas as pd


class SaveDataToCSV(object):
    
    def __init__(self):
        super(SaveDataToCSV, self).__init__()
        #self.Teta = teta


    def save(self, path, data):
        self.df = pd.DataFrame(data)
        self.df.fillna(0, inplace=True)
        #self.df.to_csv(r'C:\Users\Saif\Desktop\Data.csv', index=False)
        self.df.to_csv( path+'Data.csv', index=False)

