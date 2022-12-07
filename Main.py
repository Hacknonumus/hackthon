import json , os ,requests
from colorama import Fore
from prettytable import PrettyTable
   
red,green,blue,ylo,reset=Fore.RED,Fore.GREEN,Fore.BLUE,Fore.YELLOW,Fore.RESET


class Main():
    class json_writer():
        def json_file_writer(self,file_name,dict):
            file=open(file_name,'w')
            json.dump(dict,file,indent=6)
            file.close()

    class json_viewer():
        def json_file_viewer(self,file,key,key2):
            with open(file,'r') as file:data=json.load(file)
            for i in data[str(key)]:
                return i[str(key2)]

        def json_car_viewer(self,file,car_select,name_or_capacity):
            with open(file,'r')as file:data=json.load(file)
            for j in data[str(car_select)]:
                return j[str(name_or_capacity)]

        def json_time_viewer(self,file,time_no,time_no_pv_esu_grid):
            with open(file,'r') as file:data=json.load(file)
            for i in data['time']:
                for j in i[str(time_no)]:
                    return j[str(time_no_pv_esu_grid)]

    def __init__(self,file,add=0,sub=0,load='UnderLoad',mode='PV2EV',sub_total=0):
        self.file=file
        self.add,self.sub = add,sub
        self.load,self.mode=load,mode
        self.sub_total=sub_total 

    def clr(self):
        os.system('cls') if os.name=='nt' else os.system('clear')

    def check_update(self):                
        p1=Main.json_viewer()
        current_version = """
        {
            "currentversion": "2.0.2",
            "latestversion":"2.0.2"
        }
        """
        data0=requests.get(p1.json_file_viewer('config.json','update','version'))
        data1=requests.get(p1.json_file_viewer('config.json','update','universal_smart_charging_infrastructure'))
        data2=requests.get(p1.json_file_viewer('config.json','update','Main'))
        data3=requests.get(p1.json_file_viewer('config.json','update','dafault_dataset'))
        data4=requests.get(p1.json_file_viewer('config.json','update','config'))

        x,y = json.loads(current_version.text),json.loads(current_version)
        if x['currentversion'] == y['currentversion']:
            print(red,"[*].Already Updated",reset)
        else:
            print(green,"[+].Update Available\n[+].Updating Program",reset)
            for i,j in zip(('.version','universal_smart_charging_infrastructure.py','Main.py','default_dataset.json','config,json') \
                    ,(data0.text,data1.text,data2.text,data3.text,data4.text)):
                with open(i,'w') as file:file.write(j)
                
            print(blue,"[+].Update Complete",reset) 

    def help(self):
        print('''   
            {2}Commands{1}            {2} Decription {1}

            {0}get clear    :-{1}{2}clear data(back to default){1}
            {0}get update   :-{1}{2}update program{1}
            {0}get help     :-{1}{2}help about program and its sub_commands{1}
            
        '''.format(red,reset,blue))

    def print_data_table(self,file,time_no,car_name,car_capacity_value,pv_esu_grid):
        p1=Main.json_viewer()
        x=PrettyTable()
        x.field_names=[f"{red}Selected Car{reset}",f"{red}Selected Car Capacity{reset}",f"{red}Selected TimeZone{reset}",f"{red}{pv_esu_grid}'s Value{reset}"]
        x.add_row([f'{blue}{car_name}{reset}',f'{blue}{car_capacity_value}{reset}',f'{blue}{p1.json_time_viewer(file,time_no,time_no)}{reset}',f'{blue}{p1.json_time_viewer(file,time_no,pv_esu_grid)}{reset}'])
        print(x)

    def print_value_table(self):
        x=PrettyTable()
        x.field_names=[f"{red}Demand{reset}",f"{red}Subtraction{reset}",f"{red}Load Scenerio{reset}",f"{red}Operating Mode{reset}",f"{red}{self.load}'s Value{reset}"]
        x.add_row([f"{blue}{self.add}{reset}",f"{blue}{self.sub}{reset}",f"{blue}{self.load}{reset}",f"{blue}{self.mode}{reset}",f"{blue}{self.sub_total}{reset}"])
        print(x)
    
    def banner(self,file,time_no,car_name,car_capacity_value,pv_esu_grid):
        x,y = PrettyTable(),PrettyTable()
        k=PrettyTable()
        for i in range(1,5):
            names=Main.json_viewer.json_car_viewer(self,file,i,'name')
            capacitys=Main.json_viewer.json_car_viewer(self,file,i,'capacity')
            x.field_names=[f"{red}Sr.No{reset}",f"{red}Car's Name{reset}",f"{red}Car's Capacity{reset}"]
            x.add_row([f'{blue}{i}{reset}',f'{blue}{names}{reset}',f'{blue}{capacitys}{reset}'])

        for j in range(1,13):
        
            times=Main.json_viewer.json_time_viewer(self,file,j,j)
            pvs=Main.json_viewer.json_time_viewer(self,file,j,'pv')
            esus=Main.json_viewer.json_time_viewer(self,file,j,'esu')
            grids=Main.json_viewer.json_time_viewer(self,file,j,'grid') 
            
            y.field_names=[f"{red}Sr.No{reset}",f"{red}TimeZone{reset}",f"{red}Pv{reset}",f"{red}Esu{reset}",f"{red}Grid{reset}"]
            y.add_row([f'{blue}{j}{reset}',f'{blue}{times}{reset}',f'{blue}{pvs}{reset}',f'{blue}{esus}{reset}',f'{blue}{grids}{reset}'])

        print(x.get_string())
        print(y.get_string())
        Main.print_data_table(self,file,time_no,car_name,car_capacity_value,pv_esu_grid)
        Main.print_value_table(self)
        
    def main_al(self,file,car_no,time_no,pv_esu_grid):
        p1=Main.json_viewer()
        p2=Main.json_writer()
        car_name=p1.json_car_viewer(file,car_no,'name')
        car_capacity_value=p1.json_car_viewer(file,car_no,'capacity')
        pv_value=p1.json_time_viewer(file,time_no,'pv')
        esu_value=p1.json_time_viewer(file,time_no,'esu')
        grid_value=p1.json_time_viewer(file,time_no,'grid')

        def addition(car_capacity_value):
            self.add = float(car_capacity_value) + self.add
            self.sub_total=self.add   
            return (self.add)

        def subtraction(time_no): 
            i,j=float(p1.json_time_viewer(file,time_no,pv_esu_grid)),float(p1.json_car_viewer(file,car_no,'capacity'))
            self.sub = i-j
            return (self.sub)
            
        addition(car_capacity_value) if pv_esu_grid == 'pv' else subtraction(time_no)

        if self.add >= float(pv_value) or self.sub >= float(pv_value):
            self.load,self.mode="OverLoad","[*].ESU2EV [*].GRID2EV"   
            self.sub_total = self.sub_total - float(pv_value) - float(esu_value)  
            print(self.sub_total)         
            
        else:
            self.load,self.mode="UnderLoad","[*].PV2EV [*].PVE2ESU"
            self.sub_total = self.sub_total - float(pv_value)    #   self.sub_total == self.add (demand)
            print(self.sub_total)
            # for i in time_no:result = int(i) - 1
            # subtraction(time_no)
            # self.sub_total = float(self.sub)+p1.json_time_viewer(file,result,pv_esu_grid) 
        Main.clr(self)
        dict1={
            car_no:[{
            "name":car_name,
            "capacity":car_capacity_value
            }],
            time_no:[{
            time_no:p1.json_time_viewer(file,time_no,time_no),
            "pv":pv_value,
            "esu":self.sub_total,
            "grid":0
            }]
        }
        p2.json_file_writer('dataset3.json',dict1)
        Main.banner(self,file,time_no,car_name,car_capacity_value,pv_esu_grid)

    def main(self,file):
        p1=Main(file)
        p1.banner(file,1,'nexon','30.2','pv')
        while True:
            try:
                car_sel=input(red+"Enter Car No :- "+reset).split(',')
            except KeyboardInterrupt:
                quit()
            try:
                res=any(int(i) >= int(1) and int(i) <= int(4) for i in car_sel)
                if res == True:time_sel=input(red+"Enter TimeZone :- "+reset)
                for i in car_sel:
                
                    if int(i) >= 1 and int(i) <= 4:
                        if int(time_sel) >= 1 and int(time_sel) <= 5: print(p1.main_al(file,i,time_sel,'pv'))
    
                        elif int(time_sel) >= 6 and int(time_sel) <= 12: print(p1.main_al(file,i,time_sel,'esu'))
    
                        else: print(red,"Please Select From 1 To 12",reset)

                    else: print(red,"Select From 1 To 4 OR Enter Value Like This >> 1,2,3",reset)
            except ValueError:
                for i in car_sel:
                    if "get help" in str(i):p1.help()
                    elif "get update"  in str(i):p1.check_update();quit()
                    elif "get clear" in str(i): p1.clr();p1.banner(file,1,'nexon','30.2','pv')
                    else :
                        print(red,"Wrong Command",reset)
            
if __name__ == '__main__':

    p1=Main('formated_data.json')
    p1.main('formated_data.json')
    
   