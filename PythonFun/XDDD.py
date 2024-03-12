import pandas as pd
import matplotlib.pyplot as plt
class Tom:
    def __init__(self):
        dane = pd.DataFrame({'Miesiąc': ["Styczeń","Luty","Marzec","Kwiecień","Maj","Czerwiec","Lipiec","Sierpień","Wrzesień","Październik","Listopad","Grudzień"Styczeń","Luty","Marzec","Kwiecień","Maj","Czerwiec","Lipiec","Sierpień","Wrzesień","Październik","Listopad","Grudzień"Styczeń","Luty","Marzec","Kwiecień","Maj","Czerwiec","Lipiec","Sierpień","Wrzesień","Październik","Listopad","Grudzień"],
                     'SmartTV': [159,187,245,151,181,160,142,217,152,143,157,175],
                     'TV': [159,187,246,151,181,150,134,149,131,105,129,142]})

abbreviated_months = ["Sty","Lut","Mar","Kwi","Maj","Cze","Lip","Sie","Wrz","Paź","Lis","Gru"]
fig, ax = plt.subplots(figsize=[9, 5])
dane.plot(ax=ax)
plt.title("Sprzedaż telewizorów w roku 2016")
plt.xlabel("Miesiące")
plt.ylabel("Liczba sprzedaży")
plt.xticks(range(len(dane)), abbreviated_months)  # Use abbreviated month names for x-axis labels
plt.ylim(0, dane.max().max())  # Set y-axis limit
plt.show()