import math

class Punto():
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def strg(self):
    print( "Punto:" "({} , {})".format(self.x,self.y) )
  

  def cuadrante(self):
    if self.x==0 and self.y == 0:
        print("Esta el origen de coordenadas")
    elif self.x== 0 and self.y!=0:
        print("Esta sobre el eje X")
    elif self.x!= 0 and self.y==0:
        print("Esta sobre el eje Y")
    elif self.x > 0 and self.y > 0:
        print("Esta en el primer cuadrante")
    elif self.x < 0 and self.y > 0:
        print("Esta en el segundo cuadrante")
    elif self.x < 0 and self.y < 0:
        print("Esta en el tercer cuadrante")
    else:
        print("Esta en el cuarto cuadrante")
  def vector(self,p):
    vector = (p.x-self.x,p.y-self.y)
    return vector
  def distancia(self,p2):
    return math.sqrt((p2.x-self.x)**2 + (p2.y-self.y)**2)
class Rectangulo():
  def __init__(self):
    self.pinicialx = 0
    self.pfinalx = 0
    self.pinicialy = 0
    self.pfinaly = 0
  def set_pinicialx(self,pinicialx):
    self.pinicialx = pinicialx
  def set_pfinalx(self,pfinalx):
    self.pfinalx = pfinalx
  def set_pinicialy(self,pinicialy):
    self.pinicialy = pinicialy
  def set_pfinaly(self,pfinaly):
    self.pfinaly = pfinaly
  def get_pinicialx(self):
    return self.pinicialx 
  def get_pfinalx(self):
    return self.pfinalx 
  def get_pinicialy(self):
    return self.pinicialy 
  def get_pfinaly(self):
    return self.pfinaly 
  
  def base(self):
    pipf= math.sqrt((self.get_pinicialx()-self.get_pfinalx())**2 + (self.get_pinicialy()-self.get_pfinaly())**2)
    base= math.cos(45)*pipf
    print(base)
    return base
  def altura(self):
    pipf= math.sqrt((self.get_pinicialx()-self.get_pfinalx())**2 + (self.get_pinicialy()-self.get_pfinaly())**2)
    altura =  math.sin(45)*pipf
    print(altura)
    return altura
  def area(self):
    pipf= math.sqrt((self.get_pinicialx()-self.get_pfinalx())**2 + (self.get_pinicialy()-self.get_pfinaly())**2)
    base= math.cos(45)*pipf
    altura =  math.sin(45)*pipf
    area = base*altura
    return area


 

  
      























    

         
        


    

    



  
