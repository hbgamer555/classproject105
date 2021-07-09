import pandas as pd
import statistics
def totalpeople():
 df=pd.read_csv(r"C:\Users\ADMIN\Dropbox\My PC (DESKTOP-QH1TBQA)\Downloads\New folder (5)\Data-visualization-master\csv files\SOCR-HeightWeight.csv")
 height=df["Height(Inches)"]
 x=statistics.stdev(height)
 print(x)





 

totalpeople()
