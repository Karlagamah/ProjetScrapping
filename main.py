from email.mime import image
import sys
sys.stdout.reconfigure(encoding="utf-8")  

from config import URL
from app.controllers.scraping_controller import lancer
from app.views.console_view import menu

if __name__ == "__main__":
    lancer(URL)
  
    resultat = menu()
    print("Vous avez choisi :", resultat)
