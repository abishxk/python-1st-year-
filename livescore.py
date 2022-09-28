from tkinter import *
import requests
from bs4 import BeautifulSoup

root=TK()
root.title(IPL)

url="https://www.sportskeeda.com/"

def get_scores():
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    team_1=soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
    team_2=soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
    team_1_scores=soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
    team_2_scores=soup.find_all(class_ = "cb-ovr-flo")[10].get_text()
    teams.config(text=f"{team_1}\t\t{team_2}")
    scores.config(text=f"{team_1_score}\t{team_2_scores}")
    scores.after(1000, get_score)

    title=Label(root,text='IPL 2021',font=("Haveltica 30 bold"))
    title.grid(row=0,pady=5)
    teams=Label(root,font=("Haveltica 20 bold"))
    title.grid(row=1,padx=5)
    teams=Label(root,font=("Haveltica 20 bold"))
    title.grid(row=2,padx=5)
    get_score()
    root.mainloop()
    
