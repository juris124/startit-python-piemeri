import sys
import os
from PIL import Image


def bilzu_info(mape, atvert=False): # nolasam visus bilžu failus no mapes
    datnes = os.listdir(mape)
    for infile in datnes:
        try:
            with Image.open(os.path.join(mape,infile)) as im:
                print(infile, im.format, f"{im.size}x{im.mode}")
                if atvert:
                    im.show()
        except OSError:
            pass


def sikteli(mape):    # nolasītajiem attēlu failiem izveidojam sīktēlus
    datnes = os.listdir(mape)
    atteela_platums = int(input("Ievadi samazināmā attēla lielāko dimensiju: "))
    attela_augstums = atteela_platums
    size = (atteela_platums, attela_augstums)
    for infile in datnes:
        if not infile.find(".thumbnail") > 0:
            try:
                with Image.open(os.path.join(mape,infile)) as im:
                    outfile = infile + ".thumbnail."+im.format
                    im.thumbnail(size)
                    im.save(os.path.join(mape,outfile), im.format)
            except OSError:
                print("cannot create thumbnail for", infile)
