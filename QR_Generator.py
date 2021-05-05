import qrcode
import os
import image
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

class qrGen:

    def __init__(self):
        self.qrs_folder_path = os.path.join(os.getcwd(), "QRs")
        try:
            os.mkdir(self.qrs_folder_path)
        except FileExistsError:
            pass
        

    def genQR(self, id, sim):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data('Device ID: ' + str(id) + '\n' + "Sim number: " + str(sim)+ "\nPowered by: Datasoft Manufacturing & Asssembly")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.convert("RGBA")
        img = img.resize((450,450))
        
        icon = Image.open(os.path.join(os.getcwd(),'DMA_LOGO.png'))
        img_w, img_h = img.size
        icon_w, icon_h = 180, 75
        icon = icon.resize((icon_w, icon_h))
        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        
        frame = Image.new('RGBA', (500, 500), 'white')
        frame.paste(img,(25,10))
        frame.paste(icon,(w+25,h+5))
        draw = ImageDraw.Draw(frame)
        font = ImageFont.truetype("Roboto-medium.ttf", 36)
        draw.text((70, 457), 'Sim: '+str(sim) ,fill = (0, 0 , 0),font=font)
        draw.rectangle([(30 ,15), (470, 455)], outline ="red", width=8)
        draw.rectangle([(0 ,-2), (505, 505)], outline ="black", width=8)
        self.qr_path = os.path.join(self.qrs_folder_path, (str(sim) + ".png"))
        frame.save(self.qr_path, dpi= (500,500))

    def printQRCode(self):
        print(self.qr_path)
        os.startfile(self.qr_path, 'print')

    def printImagesInGrid(self, *args):
        try:
            os.mkdir("Print Ready QRs")
        except FileExistsError:
            pass
        try:
            key2 = None
            key1 = args[0]
            key2 = args[1]
            print(key1, key2)
        except IndexError:
            pass
        d = self.qrs_folder_path   
        qrs_path = list()
        while True:
            i = 0
            for path in sorted(os.listdir(d), key=len):
                if key2 is None:
                    if (int(path[4:4+len(str(key1))]) == int(key1)):
                        qrs_path.append(os.path.join(self.qrs_folder_path,path))
                        i += 1
                else:
                    if (int(path[4:4+len(str(key1))]) >= int(key1)) & (int(path[4:4+len(str(key2))]) <= int(key2)):
                            qrs_path.append(os.path.join(self.qrs_folder_path,path))
                            i += 1
            break
        imgs = list()
        for i in qrs_path:
            img = Image.open(i)
            imgs.append(img)
        del path
        pages = (len(imgs)-1)//24+1
        i = 0
        if len(qrs_path)!= 0:
            initial = (qrs_path[i][-16:-4])

        for n in range(pages):
            gridImg = Image.new('RGB', (2000, 3000), 'white')   
            currX = 500
            currY = 500
            for row in range(6):
                for col in range(4):
                    try:
                        gridImg.paste(imgs[i], (col*currX, row*currY))
                        i += 1
                        if isinstance((i/24), int):
                            break
                    except IndexError:
                        break
            path = os.path.join(os.getcwd(), "Print Ready QRs")
            final = (qrs_path[i-1][-16:-4])
            print("From ID:{} to ID:{} added to {}.pdf and ready to print".format(initial, final, initial+' >> '+final))
            gridImg.save(path+'//'+initial+' - '+final+'.png', dpi= (500, 500))
            initial = str(int((qrs_path[i-1][-16:-4]))+1)

if __name__ == "__main__":
    # a = qrGen()
    # for i in range(1103202105070001, 1103202105070100):   
    #     i = str(i)
    #     a.genQR(i, i[5:])
    # #     # break
    # a.printImagesInGrid(202105070001, 202105070100)
    pass