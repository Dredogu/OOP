# -*- coding: utf-8 -*-
"""OOP_Vize.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EFJR23QtbiWs0ZtYWWQfAbXdx-EGmwnk

Quiz 3
"""

"""
Adi: Doğukan
Soyadi: AKSOY
Numara: 20217170050
Bolum: Bilgisayar Muh.

"""

class Box:
    """Cargo box desi and price calculator class"""

    def __init__(self, depth:float, height:float, width:float, content:str) -> None:
        """Box constructor it assigns start values of a box. 
        Calls methods by order:

        calculate_desi()
        calculate_price()
        print()

        Args:
            adepth (float): depth of box
            aheight (float): height of box
            awidth (float): width of box
            acontent (str): content of box
        """
        self.depth   = depth
        self.height  = height
        self.width   = width
        self.content = content
        self.desi    = self.calculate_desi()
        self.price   = self.calculate_price()
        self.print()


    def calculate_desi(self):
        """calculates desi of box with formula:
                desi = depth*height*width / 3000 
        """
        return self.depth * self.height * self.width / 3000

    def calculate_price(self):
        """Calculate cargo price of box
            desi=0,   price = 0
            desi<10,  price = 20
            desi<20,  price = 30
            desi<30,  price = 40
            desi>=30, price = 50
        """
        price:float = 0.0

        if self.desi == 0:
          price = 0.0
        elif self.desi < 10:
          price = 20
        elif self.desi < 20:
          price = 30
        elif self.desi < 30:
          price = 40
        else:
          price = 50

        return price


    def print(self):
        """Prints the content,desi and price of a box
        ex : 
        makarna,5,20TL
        """
        print(f'{self.content},{self.desi},{self.price}TL')

box1 = Box(0,0,0,"Bos")
box2 = Box(30,40,50,"Makarna")
box3 = Box(10,5,3,"Telefon")
box4 = Box(50,60,70,"TV")

total_price = 0
for box in [box1,box2,box3,box4]:
    total_price += box.price

print("Total:{}TL".format(total_price))


"""
Beklenen Ekran Çıktısı
Bos,0.0,0.0TL
Makarna,20.0,40TL
Telefon,0.05,20TL
TV,70.0,50TL
Total:110.0TL
"""

"""Quiz 5"""

class Hesap: 
    """Hesap ve harcama bilgilerini tutan sınıf"""

    def __init__(self, ad, soyad, baslangic_bakiyesi) -> None:
        """Hesap Constructor

        Args:
            ad (str): kişi adı
            soyad (str): kişi soyadı
            baslangic_bakiyesi (str): hesap açılış bakiyesi
        """
        self.__ad                 = ad
        self.__soyad              = soyad
        self.__bakiye             = 0
        self.__hareket            = []
        self.__hareket_ekle("Başlangiç Bakiyesi", baslangic_bakiyesi)

    @property
    def ad(self):
        """ad property getter

        Returns:
            str: adın ilk üç harfi ve 3 yıldız
            örnek: Ayş***
        """
        return f'{self.__ad[:3]}***'

    @ad.setter
    def ad(self,value):
        """ad setter

        Args:
            value (str): kişi adı
        """
        self.__ad = value

    @property
    def soyad(self):
        """soyad setter

        Returns:
            str: soyadın ilk üç harfi ve 3 yıldız
            örnek: Yıl***
        """
        return f'{self.__soyad[:3]}***'

    @soyad.setter
    def soyad(self,value):
        """soyad setter

        Args:
            value (str): kişi soyadı
        """
        self.__soyad = value

    @property
    def bakiye(self):
        """bakiye property

        Returns:
            float: kişi bakiyesi
        """
        return self.__bakiye

    @bakiye.setter
    def bakiye(self,value):
        """bakiye setter

        Args:
            value (float): bakiye property si read-only dir

        Raises:
            AttributeError: Bakiye değiştirilemez!
        """
        raise AttributeError("Bakiye değiştirilemez!")

    def __hareket_ekle(self,aciklama,miktar):
        """hareket ekle methodu

        Args:
            aciklama (str): hareket açıklaması
            miktar (float): miktar 
        """
        self.__bakiye += miktar
        self.__hareket.append(f"*{aciklama},{miktar}")


    def yatir(self,value):
        """para yatirma methodu

        Args:
            value (float): yatan miktar
        miktar negatif olursa aşağıdaki hata gerçekleşmelidir.

        Raises:
            AttributeError: Yatırılan miktar 0'dan büyük olmalıdır!
        """
        if value < 0:
          raise AttributeError("Yatırılan miktar 0'dan büyük olmalıdır!")

        self.__hareket_ekle("Para Yatirma", value)

    def harca(self,aciklama,miktar):
        """harcama methodu

        Args:
            aciklama (str): harcama açıklaması
            miktar (float): miktar

            miktar negatif olursa aşağıdaki hata gerçekleşir
        Raises:
            AttributeError: Harcanan miktar 0'dan büyük olmalıdır!
        
            miktar bakiyeden büyük olursa aşağıdaki hata gerçekleşir
        Raises:
            AttributeError: Bakiye yetersiz!
        """
        if miktar < 0:
          raise AttributeError("Harcanan miktar 0'dan büyük olmalıdır!")
        elif miktar > self.bakiye:
          raise AttributeError("Bakiye yetersiz!")

        self.__hareket_ekle(aciklama, -miktar)

    def dokum(self):
        """hesap dokumu methodu 
        önce ------ yazar 20 çizgi
        sonra kişinin adı ve soyadı yazar
        sonra tüm hareketler alt alta yazılır
        sonra hesap bakiyesi yazılır
        sonra ------ yazar 20 çizgi
        
        """
        print("-"*20)
        print(self.ad, self.soyad)
        for i in self.__hareket:
          print(i);
        print(f"Hesap Bakiyesi:{self.bakiye}")
        print('-'*20)

kisi1 =  Hesap('Yusuf', 'Kanmaz',220)
kisi2 = Hesap('Fatma', 'Demir',500)
kisi1.dokum()
try:
    kisi1.bakiye = 50 
except Exception as e:
    print(str(e)) 
kisi1.ad = 'Hasan'
kisi1.yatir(35) 
kisi1.harca('Market',58)
kisi2.harca('Kuafor',350)
kisi1.harca('Kasap',100)
try:
    kisi1.yatir(-20)
except Exception as e:
    print(str(e))
try:
    kisi2.harca('Çanta',480)
except Exception as e:
    print(str(e))
kisi1.harca('Fatura',80)
kisi1.dokum()
kisi2.dokum()


"""
örnek çıktı
--------------------
Yus***,Kan***
*Başlangıç bakiyesi,220
Hesap Bakiyesi:220
--------------------
Bakiye değiştirilemez!
Yatırılan miktar 0'dan büyük olmalıdır!
Bakiye yetersiz!
--------------------
Has***,Kan***
*Başlangıç bakiyesi,220
*Para Yatırma,35
*Market,-58
*Kasap,-100
*Fatura,-80
Hesap Bakiyesi:17
--------------------
--------------------
Fat***,Dem***
*Başlangıç bakiyesi,500
*Kuafor,-350
Hesap Bakiyesi:150
--------------------
"""

"""Quiz 6"""

"""
Name Surname = Doğukan AKSOY
Number = 20217170050

"""

class Mixture:
    """Salt and water mixture manipulation class"""

    def __init__(self, total_amount, salt_amount) -> None:
        """Mixture Constructor

        Args:
            total_amount (float): water + salt amount
            salt_amount (float): salt amount
        """
        self.__total_amount = total_amount
        self.__salt_amount  = salt_amount
        self.__salt_ratio   = self.salt_ratio

    @property
    def salt_ratio(self):
        """salt_ratio property getter

        Returns:
            float: salt_amount / total_amount
        """
        return self.__salt_amount / self.__total_amount


    @salt_ratio.setter
    def salt_ratio(self, value):
        """salt_ratio property setter
        Calculates salt_amount with salt_ratio and total_amount 
        and sets salt_amount 

        Args:
            value (float): salt ratio
        """
        self.__salt_ratio = value


    @property
    def water_amount(self):
        """water_amount property getter

        Returns:
            float: total_amount - salt_amount
        """   
        return self.__total_amount - self.__salt_amount


    @water_amount.setter
    def water_amount():
        """water_amount property setter
        water_amount is a calculated property 
        it is read-only

        Args:
            value (float): water amount (but not used)

        Raises:
            AttributeError: "Cannot set water amount"
        """
        raise AttributeError("Cannot set water amount")


    @property
    def water_ratio(self):
        """water_ratio property getter

        Returns:
            float: 1 - salt_ratio
        """
        return 1 - self.__salt_ratio


    @water_ratio.setter
    def water_ratio():
        """water_ratio property setter
        water_ratio is a calculated property 
        it is read-only

        Args:
            value (float): water ratio (but not used)

        Raises:
            AttributeError: "Cannot set water ratio"
        """
        raise AttributeError("Cannot set water ratio")


    @classmethod
    def from_salt_ratio(cls, total_amount, salt_ratio):
        """from_salt_ratio is a classmethod 
        it is a alternative constructor
        it calls main constructor with total_amount and 0 salt_amount
        and creates a new instance
        it sets salt_ratio property of new instance

        Args:
            total_amount (float): water + salt amount
            salt_ratio (float): salt ratio

        Returns:
            Mixture: created new instance 
        """
        return cls(total_amount, salt_ratio*total_amount)


    @classmethod
    def from_water_ratio(cls, total_amount, water_ratio):
        """from_water_ratio is a classmethod 
        it is a alternative constructor
        it calls from_salt_ratio alternative constructor with total_amount and 1-water_ratio 

        Args:
            total_amount (float): water + salt amount
            water_ratio (float): water ratio

        Returns:
            Mixture: created new instance 
        """
        return cls(total_amount, (1-water_ratio)*total_amount)


    @classmethod
    def from_water_amount(cls, total_amount, water_amount):
        """from_water_amount is a classmethod 
        it is a alternative constructor
        it calls main constructor with total_amount and total_amount-water_amount
        and creates a new instance 

        Args:
            total_amount (float): water + salt amount
            water_amount (float): water amount

        Returns:
            Mixture: created new instance 
        """
        return cls(total_amount, total_amount-water_amount)


    @classmethod
    def from_amounts(cls, water_amount, salt_amount):
        """from_amounts is a classmethod 
        it is a alternative constructor
        it calls main constructor with water_amount+salt_amount and salt_amount
        and creates a new instance 

        Args:
            water_amount (float): water amount
            salt_amount (float): salt amount

        Returns:
            Mixture: created new instance 
        """
        return cls(water_amount+salt_amount, salt_amount)


    def __add__(self, rhs):
        """Mixture class + operator overloader
        it creates a new instance with self.total_amount + rhs.total_amount and self.salt_amount + rhs.salt_amount


        Args:
            rhs (Mixture): right hand side object

        Returns:
            Mixture: created new instance
        """
        return Mixture(self.__total_amount + rhs.__total_amount, self.__salt_amount + rhs.__salt_amount)


    def __truediv__ (self, value):
        """Mixture class / operator overloader
        it creates a new instance with self.total_amount / value and self.salt_amount / value


        Args:
            value (float): divider

        Returns:
            Mixture: created new instance
        """
        return Mixture(self.__total_amount / value, self.__salt_amount / value)



    def __mul__(self, value):
        """Mixture class * operator overloader
        it creates a new instance with self.total_amount * value and self.salt_amount * value


        Args:
            value (float): multiplier

        Returns:
            Mixture: created new instance
        """
        return Mixture(self.__total_amount * value, self.__salt_amount * value)


    def __eq__(self, rhs) -> bool:
        """Mixture class == operator overloader

        Args:
            rhs (Mixture): right hand side object

        Returns:
            bool: self.total_amount == rhs.total_amount and self.salt_amount == rhs.salt_amount
        """
        return self.__total_amount == rhs.__total_amount and self.__salt_amount == rhs.__salt_amount

        

    def __str__(self) -> str:
        """Mixture class to string method overloader

        Returns:
            str: 'SA:{:3.2f},WA:{:3.2f},SR:{:3.2f},WR:{:3.2f},TOTAL:{:3.2f}'
        """
        return f"SA:{self.__salt_amount:3.2f},WA:{self.water_amount:3.2f},SR:{self.salt_ratio:3.2f},WR:{self.water_ratio:3.2f},TOTAL:{self.__total_amount:3.2f}"

m1 = Mixture(100,20)
print(f'm1={m1}')
m2 = Mixture.from_amounts(90,10)
print(f'm2={m2}')
m3 = Mixture.from_salt_ratio(100,0.2)
print(f'm3={m3}')
m4 = Mixture.from_water_amount(100,75)
print(f'm4={m4}')
m5 = Mixture.from_water_ratio(100,0.85)
print(f'm5={m5}')
print(f'm1==m2={m1==m2}')
print(f'm1==m3={m1==m3}') 
m6 = m1 +m2
print(f'm6={m6}')
m7 = m6 * 2 + m4
print(f'm7={m7}')
m8 = m5 / 2
print(f'm8={m8}')

"""Example output
m1=SA:20.00,WA:80.00,SR:0.20,WR:0.80,TOTAL:100.00
m2=SA:10.00,WA:90.00,SR:0.10,WR:0.90,TOTAL:100.00
m3=SA:20.00,WA:80.00,SR:0.20,WR:0.80,TOTAL:100.00
m4=SA:25.00,WA:75.00,SR:0.25,WR:0.75,TOTAL:100.00
m5=SA:15.00,WA:85.00,SR:0.15,WR:0.85,TOTAL:100.00
m1==m2=False
m1==m3=True
m6=SA:30.00,WA:170.00,SR:0.15,WR:0.85,TOTAL:200.00
m7=SA:85.00,WA:415.00,SR:0.17,WR:0.83,TOTAL:500.00
m8=SA:7.50,WA:42.50,SR:0.15,WR:0.85,TOTAL:50.00
"""