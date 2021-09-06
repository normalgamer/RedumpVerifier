import requests
import os
import datetime
import zipfile


links = ["http://redump.org/datfile/mac/", "http://redump.org/datfile/ajcd/",
         "http://redump.org/datfile/pippin/", "http://redump.org/datfile/qis/",
         "http://redump.org/datfile/acd/", "http://redump.org/datfile/cd32/",
         "http://redump.org/datfile/cdtv/", "http://redump.org/datfile/fmt/",
         "http://redump.org/datfile/fpp/", "http://redump.org/datfile/pc/",
         "http://redump.org/datfile/ite/", "http://redump.org/datfile/kea/",
         "http://redump.org/datfile/kfb/", "http://redump.org/datfile/ksgv/",
         "http://redump.org/datfile/ixl/", "http://redump.org/datfile/hs/",
         "http://redump.org/datfile/vis/", "http://redump.org/datfile/xbox/",
         "http://redump.org/datfile/trf/", "http://redump.org/datfile/ns246/",
         "http://redump.org/datfile/pce/", "http://redump.org/datfile/pc-88/",
         "http://redump.org/datfile/pc-98/",
         "http://redump.org/datfile/pc-fx/", "http://redump.org/datfile/ngcd/",
         "http://redump.org/datfile/gc/", "http://redump.org/datfile/palm/",
         "http://redump.org/datfile/3do/", "http://redump.org/datfile/cdi/",
         "http://redump.org/datfile/photo-cd/",
         "http://redump.org/datfile/psxgs/",
         "http://redump.org/datfile/chihiro/", "http://redump.org/datfile/dc/",
         "http://redump.org/datfile/lindbergh/",
         "http://redump.org/datfile/mcd/", "http://redump.org/datfile/naomi/",
         "http://redump.org/datfile/naomi2/",
         "http://redump.org/datfile/sp21/", "http://redump.org/datfile/sre/",
         "http://redump.org/datfile/sre2/", "http://redump.org/datfile/ss/",
         "http://redump.org/datfile/psx/", "http://redump.org/datfile/ps2/",
         "http://redump.org/datfile/psp/",
         "http://redump.org/datfile/quizard/",
         "http://redump.org/datfile/ksite/", "http://redump.org/datfile/nuon/",
         "http://redump.org/datfile/vflash/",
         "http://redump.org/datfile/gamewave/"]


print("DATs are being updated. Please wait...")

files = os.listdir("dat")
for file in files:
    if "Wii" in file:
        pass
    else:
        os.remove("dat/" + file)

i = 1

for link in links:
    filename = link.split("/")[-2]
    print("Downlading " + filename + " (" + str(i) + "/" + str(len(links)) +
          ")")
    content = requests.get(link, allow_redirects=True)
    with open("dat/" + filename + ".zip", "wb") as f:
        f.write(content.content)
    i += 1
    with zipfile.ZipFile("dat/" + filename + ".zip", "r") as zip_ref:
        zip_ref.extractall("dat/")
    os.remove("dat/" + filename + ".zip")


with open("dat/_last_update", "w+") as f:
    f.write(str(datetime.date.today()))
