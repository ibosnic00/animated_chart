import pandas as pd
import numpy as np
import bar_chart_race as bcr

# settings
table_csv = 'data/zidic_liga_bod_bar.csv'
# collumn_name = 'Primljeni Golovi'
# collumn_name = 'Postignuti Golovi'
collumn_name = 'Gol Razlika'
# collumn_name = 'Bodovi'
#

excel = pd.read_csv(table_csv, delimiter=',', header='infer')
excel.head()

df = excel.pivot_table(values = collumn_name,index = ['Kolo'], columns = 'Ekipa')
df.head()

bcr.bar_chart_race(df = df, 
                   n_bars = 10, 
                   sort='desc',
                   steps_per_period=60,
                   period_length=2000,
                   figsize=(6,3.5),
                   period_fmt='Kolo {x:2.0f}',
                   title='Zidić Liga 2021/2022 - ' + collumn_name,
                   filename = 'animations/Zidić Liga '+ collumn_name + '.mp4')