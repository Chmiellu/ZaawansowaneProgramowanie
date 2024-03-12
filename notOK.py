from controllers.draw_controller import app as controllers_app
from model.team import teams
from services.draw_service import generate_pairs
from fastapi import FastAPI
from services.draw_service import generate_pairs
from model.team import teams
from tests.test_generate_original_pairs import TestGenerateOriginalPairs

app = FastAPI()

app.include_router(controllers_app.router)


class Tom:
    def __init__(self):
        self.dane = pd.DataFrame({
            'Miesiąc': ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec",
                        "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "S", "Luty",
                        "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "S", "Sierpień",
                        "Wrzesień", "Październik", "Listopad", "Grudzień"],
            'SmartTV': [159, 187, 245, 151, 181, 160, 142, 217, 152, 143, 157, 175],
            'TV': [159, 187, 246, 151, 181, 150, 134, 149, 131, 105, 129, 142]
        })
        self.abbreviated_months = ["Sty", "Lut", "Mar", "Kwi", "Maj", "Cze", "Lip", "Sie",
                                   "Wrz", "Paź", "Lis", "Gru"]

    def plot_sales(self):
        fig, ax = plt.subplots(figsize=[9, 5])
        self.dane.plot(ax=ax)
        plt.title("Sprzedaż telewizorów w roku 2016")
        plt.xlabel("Miesiące")
        plt.ylabel("Liczba sprzedaży")
        plt.xticks(range(len(self.dane)), self.abbreviated_months)
        plt.ylim(0, self.dane.max().max())
        plt.show()
