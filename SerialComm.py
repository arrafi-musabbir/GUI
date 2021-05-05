import serial.tools.list_ports
import serial
from serial.serialutil import SerialException


class commDev:

    def __init__(self):
        self.sc_state = 0
        self.communication = 0
        self.commPort = None
        self.listPorts = list()
        self.find_com_port()

    def communicate(self, id):
        self.communication = 0
        try:
            while self.commPort is not None:
                if self.communication == 1:
                    break
                try:
                    if self.sc.readline().strip().decode() == "ready":
                        print("Port is now ready")
                        while True:
                            print("sending data")
                            self.sc.write(id.encode())
                            if self.sc.readline().strip().decode() == "successful":
                                print("Communication successful")
                                print("Device registered successfully")
                                self.sc.timeout = 3
                                self.communication = 1
                                return True
                except UnicodeDecodeError:
                    return False    
        except serial.serialutil.SerialException:
            print("Could not open port")
            return False
            

    def auto_establish_comm(self):
        self.find_com_port()
        if self.commPort is not None:
            print("Communication port found: ", self.commPort)
            try:
                self.connectedPort = self.commPort
                self.sc = serial.Serial(self.connectedPort, 9600)
                self.flush_device()
                print("Establishing communication at port: ", self.connectedPort)
                self.sc.timeout = 3
                self.sc_state = 1
                return True
            except serial.serialutil.SerialException:
                self.close_device()
                return False
        else: 
            self.connectedPort = None
            return False

    def find_com_port(self):
        self.listPorts.clear()
        portData = serial.tools.list_ports.comports()
        if len(portData) > 0:
            for i in portData:
                port = str(i).split()
                self.listPorts.append(port[0])
            try:
                self.listPorts.remove('/dev/ttyAMA0')
            except ValueError:
                pass
            print("Comm ports found:",self.listPorts)
            if len(self.listPorts) > 0:
                self.commPort = self.listPorts[0]
                return self.listPorts
            else:
                self.commPort = None
                return None
        else:
            self.commPort = None
            print("No comm port found")
            return None

    def flush_device(self):
        print("device flushed")
        self.sc.flush()
        
    def close_device(self):
        try:
            self.sc.close()
            print("device closed")
        except AttributeError:
            print("Tried closing all connected serial devices")
            print("Serial port not connected properly/ serial port not responding")

if __name__ == "__main__":
    a = commDev()
    # a.find_com_port()
    # a.auto_establish_comm()
    # a.sc.flush()
    # a.communicate('12345678901234567890')
    # p = str(11111111111111111111).encode()
    # print(len(p))
    # print(p)
    pass
