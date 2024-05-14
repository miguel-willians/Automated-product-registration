import pyautogui as pa
import time
import pandas as pd

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pa.PAUSE = 0.5

pa.press("win")
pa.write("Chrome")
pa.press("enter")

time.sleep(1.5)
pa.hotkey("ctrl","l")
pa.write(link)
pa.press("enter")

time.sleep(3)

pa.press("tab")
pa.write("example@example.com")
pa.press("tab")
pa.write("SuperSecretPassword")
pa.press("tab")
pa.press("enter")

time.sleep(3)

table = pd.read_csv("produtos.csv")

for linha in table.index:
    pa.click(x=621, y=332)
    pa.write(str(table.loc[linha, "codigo"]))
    pa.press("tab")
    pa.write(str(table.loc[linha, "marca"]))
    pa.press("tab")
    pa.write(str(table.loc[linha, "tipo"]))
    pa.press("tab")
    pa.write(str(table.loc[linha, "categoria"]))
    pa.press("tab")
    pa.write(str(table.loc[linha, "preco_unitario"]))
    pa.press("tab")
    pa.write(str(table.loc[linha, "custo"]))
    pa.press("tab")
    obs = str(table.loc[linha, "obs"])
    if (obs != "nan"):
        pa.write(obs)
    pa.press("tab")
    pa.press("enter")
    pa.scroll(500)
    