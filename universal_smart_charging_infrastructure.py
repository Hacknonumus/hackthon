import json , os ,requests 
from colorama import Fore
#from cryptography.fernet import Fernet

red,green,blue,ylo,reset=Fore.RED,Fore.GREEN,Fore.BLUE,Fore.YELLOW,Fore.RESET

class Main():
    def __init__(self,car_sel,time_sel,pv,total,sub,overload,mode,sub_total):
        self.car_sel,self.time_sel = car_sel,time_sel
        self.pv = pv
        self.total,self.sub = total,sub
        self.overload,self.mode=overload,mode
        self.sub_total=sub_total 

    def help():
        print('''   
                        {2}Commands{1}
            {0}get clear    :-{1}{2}clear data(back to default){1}
            {0}get update   :-{1}{2}update program{1}
            {0}get help     :-{1}{2}help about program and its sub_commands{1}
            

        '''.format(red,reset,blue))

    def check_update():                  # version checking 
       
        current_version = """
        {
            "currentversion": "1.0.2",
            "latestversion":"1.0.2"
        }
        """
        data = requests.get("https://raw.githubusercontent.com/Hacknonumus/hackthon/main/universal_smart_charging_infrastructure.py")
        data_json = requests.get("https://raw.githubusercontent.com/Hacknonumus/hackthon/main/data.json")
        latest_version = requests.get("https://raw.githubusercontent.com/Hacknonumus/hackthon/main/.version")
        x,y = json.loads(latest_version.text),json.loads(current_version)

        if x['latestversion'] == y['currentversion']:
            print(red,"[*].Already Updated",reset)
        else:
            print(green,"[+].Update Available\n[+].Updating Program",reset)
            for i,j in zip(('universal_smart_charging_infrastructure.py','data.json','.version'),(data.text,data_json.text,latest_version.text)):
                with open(i, 'w') as file:file.write(j)
            print(blue,"[+].Update Complete",reset) 

    def clr():
        os.system('cls') if os.name=='nt' else os.system('clear') 
    
    def rmfiles():
        os.system('del capacity.txt time_value.txt') if os.name=='nt' else os.system('rm -rf capacity.txt time_value.txt') 
        
    def banner(load,totals,pvv,subs,modes,sub_totals):
        with open('data.json','r') as data , open('.version','r') as file:x,version=json.load(data),json.load(file)        
        for cars , times in zip(x[str(car_sel)],x['time']):
                                                                    
            print('''
            {0}    [* select your charging hub]     {1}           
            {4}                                     {1}
            {4}    [1. nexon 30.2]   [2. tigor 26]  {1}
            {4}    [3. mgzs 44.5]    [4. kona 39.2] {1}
    {0}          [* Select Time Slot AM/PM]               {1}       {4}|_Car's Name::    {1} {2}{5}{1} {4}  |_Car's Capacity::{1} {2}{6}{1}    
    {0} _________________________________________________ {1}       {4}|_Time Zone::     {1} {2}{7}{1} {4}  |_{8}'s Value::  {1} {2}{9}{1}    
    {0}|                                                 |{1}       {4}|_Demand::        {1} {2}{10}{1} {4} |_Substration::   {1} {2}{12}{1}    
    {3}| [Time-Zone]            [PV2EV]   [ESU]  [GRID]  |{1}       {4}|_Load Scenerio:: {1} {2}{11}{1} {4}{1}{2}{1} 
    {0}|_________________________________________________|{1}       {4}|_Operating Mode::{1} {2}{13}{1} {4}{1}{2}{1}    {4}|__{11}_value:{1}{2}{14}{2}
                                                                                          
    {0}[{1}{0}01. 8-10:am    ---> {1}{2}    70kw    {3}{0}  0kw     {1}{4}  13.7  {0}]{1}      
    {0}[{1}{0}02. 10-12:am   ---> {1}{2}    100kw   {3}{0}  0kw     {1}{4}  13.9  {0}]{1}       
    {0}[{1}{0}03. 12-2:pm    ---> {1}{2}    130kw   {3}{0}  54.6kw  {1}{4}    0   {0}]{1}       
    {0}[{1}{0}04. 2-4:pm     ---> {1}{2}    120kw   {3}{0}  93.9kw  {1}{4}    0   {0}]{1}       
    {0}[{1}{0}05. 4-6:pm     ---> {1}{2}    80kw    {3}{0}  110.4kw {1}{4}    0   {0}]{1}      
    {0}[{1}{0}06. 6-8:pm     ---> {1}{0}    0kw     {1}{2}  21.4kw  {1}{4}    0   {0}]{1}         
    {0}[{1}{0}07. 8-10:pm    ---> {1}{0}    0kw     {1}{2}  17.8kw  {1}{4}  17.8  {0}]{1}           
    {0}[{1}{0}08. 10-12:pm   ---> {1}{0}    0kw     {1}{2}  64.8kw  {1}{4}  160   {0}]{1}          
    {0}[{1}{0}09. 12-02:am   ---> {1}{0}    0kw     {1}{2}  119.4kw {1}{4}  150   {0}]{1}          
    {0}[{1}{0}10. 02-04:am   ---> {1}{0}    0kw     {1}{2}  49.1kw  {1}{4}    0   {0}]{1}
    {0}[{1}{0}11. 04-06:am   ---> {1}{0}    0kw     {1}{2}  11.3kw  {1}{4}  11.3  {0}]{1}
    {0}[{1}{0}12. 06-08:am   ---> {1}{0}    0kw     {1}{2}  0kw     {1}{4}  86.4  {0}]{1}
                                    {0}
                            [Press 0 to Exit 

                    {4}  Current Version:~ {1} {2}{15}{1}
    ===> '''.format(red,reset,green,ylo,blue,cars['name'],cars['capacity'],times[str(time_sel)],pvv,times[pvv],totals,load,subs,modes,sub_totals,version['currentversion']))

    def main_pv(self):          
             # data.json file
            with open('data.json','r') as data:x=json.load(data)          
            for cars , times in zip(x[str(car_sel)],x['time']):         
                # i = capacity.txt , j = car_selection_and_value ,  k = time_value.txt , l = time_value_(pv_or_esu)
                for i,j,k,l in zip(['capacity.txt'],[cars['capacity']],['time_value.txt'],[times['{}'.format(self.pv)]]):
                    with open(i,'a') as file,open(k,'a') as file1:file.write("{}\n".format(j)),file1.write("{}\n".format(l))
                Main.clr()
                # i = capacity.txt , k = time_value.txt
                with open(i,'r') as file,open(k,'r') as file1: 
                    x,x1,self.total,self.sub,self.sub_total=file.readlines(),file1.readlines(),0,0,0
                    # self.total = addition , self.sub = subtration , self.sub_total = total's_value_store_in_sub_total
                    for i,j in zip(x,x1):
                        if str('pv') in self.pv :
                            self.total += float(i)      # ex. 30.2 + 70 = 60.4
                            self.sub_total = self.total 
                        elif str('esu') in self.pv:
                            f,z=float(j),float(i)
                            z -= f;self.sub=z           # ex. 30.2 - 21.4 = 8.8
                                                                
                    if self.total >= float(j) or self.sub >= float(j):              # demand >= pv = overload
                        self.overload,self.mode='OverLoad','[*].ESU2EV [*].GRID2EV'
                        x= times['esu{}'.format(str(time_sel))] 
                        self.sub_total -= times['pv{}'.format(str(time_sel))]
                        self.sub_total -= x             
                    else:
                        self.overload,self.mode='UnderLoad','[*].PV2EV [*].PVE2ESU' # demand <= pv = underload
                        self.sub_total -= float(j)
                        
                       
                global load,totals,pvv,subs,modes,sub_totals
                load,totals,pvv,subs,modes,sub_totals = self.overload , self.total , self.pv , self.sub , self.mode , self.sub_total

car_sel,time_sel,load,totals,pvv,subs,modes,sub_totals = str(1),str(1),str('UnderLoad'),str(00),str('pv'),str(00),str('PV2EV'),str(00)
Main.banner(load, totals, pvv, subs,modes,sub_totals)       
if __name__ == '__main__':
    while True:
        try:
            
            car_sel,time_sel = input(red+"==> Select Cars:- And Time Zone:- "+reset).split(' ')
        
            if int(car_sel) >= 1 and int(car_sel) <= 4:
                if int(time_sel) >= 1 and int(time_sel) <= 5:
                
                    p1=Main(car_sel,time_sel,'pv{}'.format(str(time_sel)),0,0,'UnderLoad','PV2EV',0)
                    p1.main_pv()
                    Main.banner(load,totals,pvv,subs,modes,sub_totals)

                elif int(time_sel) >= 6 and int(time_sel) <= 12:
                
                    p1=Main(car_sel,time_sel,'esu{}'.format(str(time_sel)),0,0,'UnderLoad','PV2EV',0)
                    p1.main_pv()
                    Main.banner(load,totals,pvv,subs,modes,sub_totals)  
                
                else:
                    print(blue,"Types Wronge Number ! Please Select Between 1 To 12  ",reset)
                                         
            elif int(car_sel) == 0 and int(time_sel) == 0 :
                    print(blue,"You press 0",reset)
                    break
            else:
                print(blue,"Types Wronge Number ! Please Select Between 1 To 4 ",reset)
                
            
        except ValueError:
            if str(car_sel) == str('get'):
                if str(time_sel) == str('clear'):
                    Main.rmfiles();Main.clr()
                    car_sel,time_sel,load,totals,pvv,subs,modes,sub_totals = str(1),str(1),str('UnderLoad'),str(00),str('pv'),str(00),str('PV2EV'),str(00)
                    Main.banner(load, totals, pvv, subs,modes,sub_totals)
                elif str(time_sel) == str('update'):
                    Main.check_update()
                elif str(time_sel) == str('help'):
                    Main.clr();Main.help()
            else:
                print(blue,"Wrong Command",reset)

        except KeyboardInterrupt:
            print(blue,"Exited::",reset)
            Main.rmfiles()
            quit()
            
Main.rmfiles()
