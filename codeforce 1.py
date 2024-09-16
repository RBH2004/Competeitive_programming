class KK_tea:
  total_sale={"KK Regular Tea":0}
  def __init__(self,*args):
    self.status=False
    if len(args)==1:
      self.name="KK Regular Tea"
      self.price=args[0]
      self.number=50
    elif len(args)==2:
      self.name="KK Regular Tea"
      self.number=args[1]
      self.price=args[0]
    else:
      self.name="KK "+args[0]+" Tea"
      self.number=args[2]
      self.price=args[1]
  def product_detail(self):
    print(f"Name :{self.name},weight :{self.number*2}\nTea bags :{self.number},price :{self.price}\nStatus :{self.status}")
  def update_sold_status_regular(self,*values):
    for i in values:
      i.status=True
      if i.name in KK_tea.total_sale:
        KK_tea.total_sale[i.name]+=1
      else:
        KK_tea.total_sale[i.name]=1
  @classmethod
  def total_sales(cls):
    print(cls.total_sale)
class KK_flavoured_tea(KK_tea):
  def update_sold_status_flavoured(self,*values):
    for i in values:
      i.status=True
      if i.name in KK_tea.total_sale:
        KK_tea.total_sale[i.name]+=1
      else:
        KK_tea.total_sale[i.name]=1



t1 = KK_tea(250)
print("-----------------1-----------------")
t1.product_detail()
print("-----------------2-----------------")
KK_tea.total_sales()
print("-----------------3-----------------")
t2 = KK_tea(470, 100)
t3 = KK_tea(360, 75)
KK_tea.update_sold_status_regular(t1, t2, t3)
print("-----------------4-----------------")
t3.product_detail()
print("-----------------5-----------------")
KK_tea.total_sales()
print("-----------------6-----------------")
t4 = KK_flavoured_tea("Jasmine", 260, 50)
t5 = KK_flavoured_tea("Honey Lemon", 270, 45)
t6 = KK_flavoured_tea("Honey Lemon", 270, 45)
print("-----------------7-----------------")
t4.product_detail()
print("-----------------8-----------------")
t6.product_detail()
print("-----------------9-----------------")
KK_flavoured_tea.update_sold_status_flavoured(t4, t5, t6)
print("-----------------10-----------------")
KK_tea.total_sales()
