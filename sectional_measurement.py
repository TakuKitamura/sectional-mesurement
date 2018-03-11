import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from time import*
import warnings;warnings.filterwarnings('ignore')

class Sectional_measurement:
    
    def __init__(self):
        

        self.an_area = 0
        self.all_area = 0
        
        end_division = int(input("グラフ分割数 :"))
        self.choice_function_graph = int(input("1. [y = x^2] 2. [y = x^3 + 1] :"))

        
        self.repeat_show_new_graph(end_division) #完成したグラフを分割数を変えて表示

    
    def show_function_graph(self): #y =x^2　のグラフを表示
        
        
        if(self.choice_function_graph == 1):
            #y = x^2
            x = np.arange(0,1,0.0001)
            y = x**2
            plt.title("y = x^2", fontsize=18)
            
        elif(self.choice_function_graph == 2):
            #y = x^3
            x = np.arange(0,1,0.0001)
            y = x**3 + 1
            plt.title("y = x^3 + 1", fontsize=18)
            

            
        plt.xlabel("x label", fontsize=18)
        plt.ylabel("y lavel", fontsize=18)
        plt.plot(x,y,color ="black")
        

        
    def show_all_bar_graph(self,division_number): #ひとつずつ棒グラフを描き、全ての棒グラフを表示
    
        left = []
        height = []

        counter = 0
        bar_width = 1/division_number
        value = 0


        while((counter/division_number) != 1):

            x_value = counter/division_number
            
            if(self.choice_function_graph == 1):
                y_value = ((counter)/division_number)**2
                
            elif(self.choice_function_graph == 2):
                y_value = ((counter)/division_number)**3 + 1


            self.all_area += self.caluculate_an_area(y_value,bar_width) #ひとつの棒グラフの面積を求め、面積を足していく
            
            left.append(x_value)
            height.append(y_value)
            counter += 1
            
            
        plt.bar(left,height,width = bar_width) #棒グラフを表示

        print("(" + str(division_number)  + "分割のときの面積) = " + str(self.all_area))
        
        self.all_area = 0

            
    def repeat_show_new_graph(self,end_division):
        
        division_number = 1
        

        while division_number <= end_division: #指定した分割数の棒グラフを全て描くまでループ
            plt.pause(.00001)
            plt.clf()
            

            self.show_function_graph()
            self.show_all_bar_graph(division_number)
            
            division_number += 1
        

            
        sleep(100)
        
    def caluculate_an_area(self,y_value,bar_width):
        
        an_area = y_value * bar_width
        
        return an_area

        
        
program_start = Sectional_measurement()
