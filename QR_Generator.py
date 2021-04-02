import qrcode
import os

class qrGen:
    
    def __init__(self):
        pass
    
    def genQR(self,id,sim):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('Device ID: '+str(id)+'\n'+"Sim number: "+str(sim))
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.show()
        self.qr_path = os.path.join(os.getcwd(),("QRs/"+str(sim)+".png"))
        img.save(self.qr_path)
    
    def printCode(self):
        print("here")
        os.startfile(self.qr_path,'print')
    
if __name__ == "__main__":
    a = qrGen()
    # a.genQR(23,23)
