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
        self.add_IP()

    def __del__(self):
        self.clearPlate()

    def add_IP(self):
        url="https://free-proxy-list.net/"
        response=requests.get(url)
        soup=BeautifulSoup(response.text, 'html.parser')
        for row in soup.find("table",attrs={"id":"proxylisttable"}).find_all("tr")[1:]:
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
    
    def setProxy(self):
        return self.currentIP.IPaddress

    def rotate(self):
        if self.currentIP.nextval==None:
            self.currentIP=self.headval
        else:
            self.currentIP=self.currentIP.nextval

    def PrintCIP(self):
        print("This is current IP address:")
        print(self.currentIP.IPaddress)

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
        