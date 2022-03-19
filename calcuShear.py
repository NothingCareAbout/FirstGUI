
from ast import Return
import math




#抗剪键参数

#fc=14.3
E=206000
G=79000
'''
B=100
H=200
t=20
tw=16
B1=1000'''
#H形钢 惯性矩I,面积：A ,翼缘厚度t，腹板厚度tw ,腹板面积A1 ,宽B,高H
#钢材弹性模量E=2.06X10^5 N/m㎡ ,剪变模量G=7.9X10^4 
#几何参数
'''A=2*B*t+(H-2t)*tw
A1=(H-2t)*tw
I=1/12((B*math.pow(H,3))-(B-tw)*math.pow(H-2t,3)))'''

class Shear():
    def __init__(self,con,B,H,t,tw,B1):
        super().__init__()
        self.con=con
        self.B=B
        self.H=H
        self.t=t
        self.tw=tw
        self.B1=B1
        
    def cal_A(self):
        return 2*self.B*self.t+(self.H-2*self.t)*self.tw

    def cal_A1(self):
        return (self.H-2*self.t)*self.tw

    def cal_I(self):
        return (1/12)*((self.B*math.pow(self.H,3))-(self.B-self.tw)*math.pow(self.H-2*self.t,3))

    def cal_k(self):  
        A1=self.cal_A1()
        A=self.cal_A()
        return A1/A
        
        #k′为剪切截面形状系数,与截面形状有关，矩形截面
    #取 1 /1.2，H 型钢或工字型钢近似取 k′ = A1 /A，A1 为腹板面积)   

    
    
    #混凝土等级fc
    def concreteValue(self):
        if self.con=="C30":
            
            return float(14.3)
        
        elif self.con=="C35":
            
            return float(16.7 )  
        elif self.con=="C40":
            
            return float(19.1 )
        elif self.con=="C45":
           
            return float(21.1 )
    def cal_k1(self): 
        fc=self.concreteValue()
        K=self.cal_k()
        A=self.cal_A()
        return 2*fc*self.B/(K*A*G)

    def cal_k2(self):
        I=self.cal_I()
        fc=self.concreteValue()
        return 2*fc*self.B/(E*I)

    #计算基础混凝土沿剪力方向的计算长度l 基础尺寸B1xL1xD
    def cal_l(self):
        if 3*self.B<(self.B1/2-self.H/2):
            return 3*self.B
        else:
            return (self.B1/2-self.H/2)
        

    def cal_h(self):  # 计算抗剪键埋深h
        k1=self.cal_k1()
        k2=self.cal_k2()
        l=self.cal_l()
        #情况一：对应抗剪屈服承载力
        q=0.021 #初始化
        if q==0.021:
            return round((1/math.sqrt(k2))*math.sqrt(math.sqrt(1.52*pow(k1,2)+q*k2*l)-1.23*k1))
            
        else: #对应抗剪极限承载力的埋深
            return round((1/math.sqrt(k2))*math.sqrt(math.sqrt(1.52*pow(k1,2)+q*k2*l)-1.23*k1))


    #计算抗剪承载力
    def cal_V(self):
        h=self.cal_h()
        q=0.021
        fc=self.concreteValue()
        if q==0.021:
            return round((0.77*fc*self.B*h)/1000,2)#屈服承载力
        else:
            return round((0.87*fc*self.B*h)/1000,2)#极限承载力
        
    #计算由抗剪键产生的柱脚附加弯矩M

    def cal_M(self):
        h=self.cal_h()
        q=0.021
        fc=self.concreteValue()
        if q==0.021:
            return round((0.314*fc*self.B*math.pow(h,2))/1000000,2)#M1
        else:
            return round((0.381*fc*self.B*math.pow(h,2))/1000000,2) #M2
'''   
def main():
    sk1=Shear("C30",100,200,20,16,1000) #抗剪键参数
    埋深=sk1.cal_h()
    剪力=sk1.cal_V()
    附加弯矩=sk1.cal_M()  
    print("埋深：{}".format(埋深)+" mm","剪力：{}".format(剪力)+" Kn","附加弯矩：{}".format(附加弯矩)+" Kn.m") 
    
if __name__ == '__main__':
    main()
    '''