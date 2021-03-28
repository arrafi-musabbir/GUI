import qrcode
import os

class qrGen:
    
    def __init__(self):
        self.genQR()
    
    def genQR(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('ID: '+'1103202103170002'+'\n'+"Sim number: 01862515191")
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        print(type(img))
        img.show()
        img.save(os.path.join(os.getcwd(),"QRs/t.png"))
    
    
    
if __name__ == "__main__":
    a = qrGen()