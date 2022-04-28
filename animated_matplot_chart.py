import matplotlib.animation as ani
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# settings
table_csv = 'data/zidic_liga_bod.csv'
min_vertical_line = 3
max_vertical_line = 36
vertical_lin_width = 1
vertical_lin_color = 'gray'
plot_refresh_rate_ms = 1000
colors =['red', 'green', 'darkslateblue', 'orange', 'grey', 'lightcoral', 'royalblue', 'darkred', 'y', 'c']
#

excel = pd.read_csv(table_csv, delimiter=',', header='infer')
excel_interest = excel.loc[excel['Ekipa/Kolo'].isin(['KNKP', 'Ima i gorih', 'Samo Spinut', 'UB Nozevi', 'MNK Cunoglavci', 'NK Cuture', 'Los Kostolomikos', 'Matina Kola', 'Bugarske skitnice', 'HNK Pegalj'])]
excel_interest.rename(index=lambda x: excel_interest.at[x, 'Ekipa/Kolo'], inplace=True)
excel_trans = excel_interest.transpose()
excel_trans = excel_trans.drop(['Ekipa/Kolo'])
excel_trans = excel_trans.loc[(excel_trans != 0).any(1)]
# excel_trans.index = pd.to_datetime(excel_trans.index)

fig = plt.figure()
fig.set_figwidth(15)

def build_bar_chart(i=int):
    iv = min(i, len(excel_trans.index)-1) #the loop iterates an extra one time, which causes the dataframes to go out of bounds. This was the easiest (most lazy) way to solve this :)
    objects = excel_trans.max().index
    y_pos = np.arange(len(objects))
    performance = excel_trans.iloc[[iv]].values.tolist()[0]
    plt.barh(y_pos, performance, align='center', color=colors)
    plt.yticks(y_pos, objects)
    plt.title('Kolo \n' + str(iv+1))
    plt.xlabel('Bodovi')
    plt.ylabel('Ekipa')

animator = ani.FuncAnimation(fig, build_bar_chart, interval=plot_refresh_rate_ms)

for point in range (min_vertical_line, max_vertical_line, 3):
    plt.axvline(x=point, color=vertical_lin_color, linestyle='dotted', linewidth=vertical_lin_width)
plt.show()
