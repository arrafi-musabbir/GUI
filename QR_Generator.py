import qrcode
import os
import image
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
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('Device ID: ' + str(id) + '\n' + "Sim number: " + str(sim))
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        # img.show()
        self.qr_path = os.path.join(self.qrs_folder_path, (str(sim) + ".png"))
        img.save(self.qr_path)
        # self.printQRCode()

    def printQRCode(self):
        print(self.qr_path)
        os.startfile(self.qr_path, 'print')

    def printImagesInGrid(self):

        os.startfile("self.qr_path", "print")
        pass


if __name__ == "__main__":
    a = qrGen()
    # a.genQR(123456, "test")
