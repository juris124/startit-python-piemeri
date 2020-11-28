import sys
import os
from PIL import Image


def bilzu_info(mape, atvert=False): # nolasam visus bilžu failus no mapes
    datnes = os.listdir(mape)
    for infile in datnes:
        try:
            with Image.open(os.path.join(mape,infile)) as attels:
                print(infile, attels.format, f"{attels.size}x{attels.mode}")
                if atvert:
                    attels.show()
        except OSError:
            pass


def sikteli(mape, lielums):    # nolasītajiem attēlu failiem izveidojam sīktēlus, ar lietotāja norādīto izmēru
    datnes = os.listdir(mape)
    size = (lielums, lielums)
    for infile in datnes:
        if not infile.find("_m") > 0:
            try:
                with Image.open(os.path.join(mape,infile)) as attels:                    
                    infile = infile.split(sep=".") # noņemam paplašinājumu 
                    infile = infile[0]                   
                    outfile = infile + "_m."+attels.format.lower()
                    attels.thumbnail(size)
                    attels.save(os.path.join(mape,outfile), attels.format)
            except OSError:
                print("Nevar izveidot attlēla sīktēlu: ", infile)
