from tkinter import *
from tkinter import ttk
def main():
  root = Tk()
  root.title("TOD Calculator")
  frm = ttk.Frame(root, padding=10)
  frm.grid()
  ttk.Label(frm, text="TOD Calculator").grid(column=0, row=0, rowspan=1, columnspan=2)
  cruiseAltStr = StringVar()
  finalAltStr = StringVar()
  groundSpeedStr = StringVar()
  todDistance = StringVar()
  descRate = StringVar()
  def calculate_tod(startalt, endalt):
    difalt = startalt - endalt
    difalt *= 3
    difalt /= 1000
    return difalt
  def calculate_rate(groundspeed):
    return groundspeed * 5
  def maincalc():
    todDistance.set(calculate_tod(int(cruiseAltStr.get()), int(finalAltStr.get())))
    descRate.set(calculate_rate(int(groundSpeedStr.get())))
    return
  ttk.Label(frm, text="Cruising Altitude: ").grid(column=0, row=1)
  ttk.Entry(frm, width=7, textvariable=cruiseAltStr).grid(column=1, row=1)
  ttk.Label(frm, text="Final Altitude: ").grid(column=0, row=2)
  ttk.Entry(frm, width=7, textvariable=finalAltStr).grid(column=1, row=2)
  ttk.Label(frm, text="Ground Speed").grid(column=0, row=3)
  ttk.Entry(frm, width=7, textvariable=groundSpeedStr).grid(column=1, row=3)
  ttk.Button(frm, text="Calculate", command=maincalc).grid(column=0, row=4)
  ttk.Label(frm, text="TOD Distance (NM):").grid(column=0, row=5)
  ttk.Label(frm, textvariable=todDistance).grid(column=1, row=5)
  ttk.Label(frm, text="Descent Rate (FPM):").grid(column=0, row=6)
  ttk.Label(frm, textvariable=descRate).grid(column=1, row=6)
  for child in frm.winfo_children():
    child.grid_configure(padx=1, pady=1)
  root.bind("<Return>", maincalc)
  root.mainloop()
if __name__ == "__main__":
  main()