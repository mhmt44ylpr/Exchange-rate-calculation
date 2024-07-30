import requests
import json

print("Kur Hesaplama Programı".center(50,"-"))

class KurHesaplama(object):
    def __init__(self,alınan,donusen,miktar):
        self.alınan = alınan
        self.donusen = donusen
        self.miktar = miktar
        self.Apı_Key = "de41f4d1196858b2a74d0781"
        self.Url = f"https://v6.exchangerate-api.com/v6/{self.Apı_Key}/latest/"
        self.reg()
    def reg(self):
        new_url = self.Url + self.alınan
        r = requests.get(new_url)
        r = json.loads(r.text)
        text = f"{self.miktar} : {self.alınan} , {(self.miktar*r["conversion_rates"][self.donusen]):.2f} : {self.donusen} eşittir."
        print(text)

def Hesap():
    try:
        miktar = int(input("Miktar: "))
        try:
            alınan = input("Alınan Para Birimi: ")
            donusen = input("Donusen Para Birimi: ")
            K = KurHesaplama(alınan=alınan,
                             donusen=donusen,
                             miktar=miktar)
        except:
            print("Alınan ya da dönüşen para birimlerini doğru giriniz...")
            Hesap()
    except:
        print("Mikatrı sayı olarak giriniz...")
        Hesap()

Hesap()





