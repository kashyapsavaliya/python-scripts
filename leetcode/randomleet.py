from readFromUrl import getGoogleSheets
import pandas as pd
import random
import webbrowser

data = getGoogleSheets('https://docs.google.com/spreadsheets/d/1eSl3Se-XS6gH_ZT5OfQ9l3D0mFrt0pYvx_hcLQX_8sc/edit#gid=0')
sheet = pd.DataFrame(data)
chosen = random.randint(1, len(sheet.index))
webbrowser.open_new_tab(sheet[1][chosen])
print(chosen + 1)
