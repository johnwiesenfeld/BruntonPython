from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("CSUN Geology Brunton Database")
root.iconbitmap("CSUNGeoSeal.ico")
root.geometry("600x600")

# Databse for Brunton Compass Inventory

# Create a databse or connect to one
conn = sqlite3.connect('bruntoninventory.db')

# Create cursos
c = conn.cursor()

# Create table (only needs to run once, then comment out)

# c.execute("""
#         CREATE TABLE bruntons (
#             compass_number integer,
#             old_tag integer,
#             new_tag integer,
#             Serial # integer, 
#             state text,
#             zipcode integer
#         )""")





# Commit Changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()