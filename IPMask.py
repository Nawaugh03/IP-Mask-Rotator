import requests
from requests.exceptions import ProxyError
from bs4 import BeautifulSoup

class IP:
    def __init__(self, address=None, port=None):
        self.address=address
        self.port=port
        self.IPaddress=str(self.address)+":"+str(self.port)
        self.nextval = None
    def __del__(self):
        self.address=None
        self.port=None
        self.IPaddress=None
        self.nextval=None

class IPRotator:
    def __init__(self):
        #print("IP Proxy Rotator online.")
        self.headval=None
        self.currentIP=None
        if self.__webtest__() is not None:
            self.add_IP()
            print("Rotator ready")
        else:
            print("Rotator need to be updated")

    def __del__(self):
        self.clearPlate()
    def __webtest__(self):
        A=None
        url="https://free-proxy-list.net/"
        response=requests.get(url)
        soup=BeautifulSoup(response.text, 'html.parser')
        try:
            A=soup.find("table").find_all("tr")[1:]
        except:
            A=None
        return A
    def add_IP(self):
        
        for row in self.__webtest__():
            tds=row.find_all("td")
            try:
               address=tds[0].text.strip()
               port=tds[1].text.strip()
               valid=tds[6].text.strip()
               if valid =="yes": 
                   newproxy=IP(address,port)
                   if self.headval==None:
                       self.headval = newproxy
                       self.currentIP= newproxy
                   else:
                       previousIP.nextval=newproxy
                   previousIP=newproxy
               else:
                  continue
            except:
                continue

    def getCurrentIP_Proxy(self):
        return self.currentIP.IPaddress

    def rotate(self):
        if self.currentIP.nextval==None:
            self.currentIP=self.headval
        else:
            self.currentIP=self.currentIP.nextval

    def PrintCurrentIP(self):
        print("This is current IP address:")
        print(self.currentIP.IPaddress)

    def setproxyrequest(self):
        return {"http":getCurrentIP_Proxy(),"https":getCurrentIP_Proxy()}
    def printlist(self):
        currentvalue=self.headval
        while currentvalue.nextval != None:
            if currentvalue==self.currentIP:
                print("~~~","| Current IP address |","~~~")
                print("-->",currentvalue.IPaddress,'<--')
            else:
                print(currentvalue.IPaddress)
            currentvalue=currentvalue.nextval

    def clearPlate(self):  
        current=self.headval
        next=None
        while (current!=None):
            next=current.nextval
            del current
            current=next
        self.headval=None
    
    def refresh(self):
        self.clearPlate()
        self.add_IP()
   
if __name__ =='__main__':
    Test=IPRotator()
    Test.PrintCIP()
