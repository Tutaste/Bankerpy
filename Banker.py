from datetime import datetime

class Bank():
	
	hesaplar = []
	islemGecmisi = []
	ID = 0
	cash = 0

	def getAccount(self):
		return self.hesaplar

	def Deposit(self,ID,cash):
		self.hesaplar[ID-1].deposit(cash)
		IslemKaydet(ID,"+",cash)

	def Withdraw(self,ID,cash):
		self.hesaplar[ID-1].withdraw(cash)
		IslemKaydet(ID,"-",cash)

	def IslemKaydet(self,ID,tip,ash):
		self.islemGecmisi.append("" + ID + " hesabı " + tip + cash)
		if self.islemGecmisi.length() > 5
			self.islemGecmisi.remove(0) # remove olup olmadığı kontrol edilecek

	def SonIslemler(self):
		return self.islemGecmisi

class Banker():
	"""
	Banker sınıfı oluşturulacak.
	"""

class Account():

	tarih = datetime(01,01,2019)## tekrar kontrol edilecek
	Balance=0
	Id=0

	def deposit(self,miktar):
		self.Balance += miktar
		print("Hesabınızda " + self.Balance + " TL bulunmaktadır.")

	def withdraw(self,miktar):
		if miktar <= self.Balance :
			self.Balance -= miktar
			print("Hesabınızdan "+miktar+" TL çekildi. Hesabınızda " +Balance+" TL bulunmaktadır.")
		else:
			print("Hesabınızda yeterli miktarda para bulunmamaktadır!")

	def getBalance(self):
		return self.Balance

	def getId(self):
		return self.Id

	def Benefit(self):
		pass

class LongTerm(Account):

	faiz=0.24

	def Benefit(self):
		islemTarihi = datetime.now()
		fark = ""## iki gün arası fark bulunacak tarif - islemTarihi
		return (int)(self.fark*(self.faiz/365)*self.Balance)

class ShortTerm(Account):

	faiz=0.17

	def Benefit(self):
		islemTarihi = datetime.now()
		fark = ""## iki gün arası fark bulunacak
		return (int)(self.fark*(self.faiz/365)*self.Balance)

class Current(Account):

	faiz=1

	def Benefit(self):
		islemTarihi = datetime.now()
		fark = ""## iki gün arası fark bulunacak
		return (int)(self.faiz*self.Balance)
		


		