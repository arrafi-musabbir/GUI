import qrcode
import os
import image
import sys
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import cv2
# from PIL import Image
# import img2pdf


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
            border=2,
        )
        qr.add_data('Device ID: ' + str(id) + '\n' + "Sim number: " + str(sim))
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.convert("RGBA")
        
        icon = Image.open(os.path.join(os.getcwd(),'DMA_LOGO.png'))
        img_w, img_h = img.size
        icon_w, icon_h = 180, 75
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        
        frame = Image.new('RGBA', (500, 500), 'white')
        frame.paste(img,(25,5))
        frame.paste(icon,(w+25,h+5))
        draw = ImageDraw.Draw(frame)
        font = ImageFont.truetype("Roboto-medium.ttf", 30)
        draw.text((100, 460), 'ID: '+str(id) ,fill = (0, 0 , 0),font=font)
        draw.rectangle([(30 ,10), (470, 450)], outline ="red", width=10)
        self.qr_path = os.path.join(self.qrs_folder_path, (str(sim) + ".png"))
        frame.save(self.qr_path, dpi= (300,300))

    def printQRCode(self):
        print(self.qr_path)
        os.startfile(self.qr_path, 'print')

    def printImagesInGrid(self):
        d = self.qrs_folder_path   
        qrs_path = list()
        for path in sorted(os.listdir(d), key=len):
            qrs_path.append(os.path.join(self.qrs_folder_path,path))
        print(qrs_path[1])
        # img0 = Image.open(qrs_path[0])
        # img1 = Image.open(qrs_path[1])
        imgs = list()
        for i in qrs_path:
            img = Image.open(i)
            imgs.append(img)
        newImg = Image.new('RGB', (3000, 2000))   
        currX = 0
        currY = 0
        for i in range(6):
            newImg.paste(imgs[i], (currX, currY))
            currX += 500
        
        # newImg = Image.new('RGB', (img0.width+img1.width, img1.height))
        # newImg.paste(img0, (0,0))
        # newImg.paste(img1, (img1.width+20,0))
        newImg.show()
        # newImg.save('newImg.png', dpi= (300,300))
        
        # os.startfile(newImg, 'print')


if __name__ == "__main__":
    a = qrGen()
    # a.genQR(1,1)
    # a.printImagesInGrid()
    for i in range(1103202105031862, 1103202105031900):   
        i = str(i)
        a.genQR(i, i[5:])