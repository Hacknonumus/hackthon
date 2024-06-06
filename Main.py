import json
import os
import requests
from colorama import Fore
from prettytable import PrettyTable

red, green, blue, ylo, reset = Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.RESET


class Main:

    class table_maker:
        def print_data_table(self, file, time_no, car_name, car_capacity_value, pv_esu_grid):
            p1 = Main.json_viewer()
            x = PrettyTable()
            x.field_names = [
                f"{red}Selected Car{reset}",
                f"{red}Selected Car Capacity{reset}",
                f"{red}Selected TimeZone{reset}",
                f"{red}{pv_esu_grid}'s Value{reset}",
            ]
            x.add_row(
                [
                    f"{blue}{car_name}{reset}",
                    f"{blue}{car_capacity_value}{reset}",
                    f"{blue}{p1.json_time_viewer(file, time_no, time_no)}{reset}",
                    f"{blue}{p1.json_time_viewer(file, time_no, pv_esu_grid)}{reset}",
                ]
            )
            return print(x)

        def print_value_table(self, car_sel, time, demand, pv, esu, grid, load, mode):
            x = PrettyTable()
            x.field_names = [
                f"{red}SELECTED CAR{reset}",
                f"{red}TIMEZONE{reset}",
                f"{red}DEMAND{reset}",
                f"{red}PV{reset}",
                f"{red}ESU{reset}",
                f"{red}GRID{reset}",
                f"{red}LOAD{reset}",
                f"{red}MODE{reset}",
            ]
            x.add_row(
                [
                    f"{blue}{car_sel}{reset}",
                    f"{blue}{time}{reset}",
                    f"{blue}{demand}{reset}",
                    f"{blue}{pv}{reset}",
                    f"{blue}{esu}{reset}",
                    f"{blue}{grid}{reset}",
                    f"{blue}{load}{reset}",
                    f"{blue}{mode}{reset}",
                ]
            )
            return print(x)

    class json_writer:
        def json_file_writer(self, file_name, dict):
            with open(file_name, "a") as f:
                json.dump(dict, f, indent=2)

    class json_viewer:
        def json_file_viewer(self, file, key, value):
            with open(file, "r") as file:
                data = json.load(file)
            for i in data[str(key)]:
                return i[str(value)]
            # for j in i[str(key2)]:
            # return j[str(value)]

        def json_car_viewer(self, file, car_select, name_or_capacity):
            with open(file, "r") as file:
                data = json.load(file)
            for j in data[str(car_select)]:
                return j[str(name_or_capacity)]

        def json_time_viewer(self, file, time_no, time_no_pv_esu_grid):
            with open(file, "r") as file:
                data = json.load(file)
            for i in data["time"]:
                for j in i[str(time_no)]:
                    return j[str(time_no_pv_esu_grid)]

    def __init__(self, file, demand=0, sub=0, load="UnderLoad", mode="PV2EV", sub_total=0):
        self.file = file
        self.demand, self.sub = demand, sub
        self.load, self.mode = load, mode
        self.sub_total = sub_total

    def clr(self):
        os.system("cls") if os.name == "nt" else os.system("clear")

    def check_update(self):
        p1 = Main.json_viewer()
        current_version = """
        {
            "currentversion": "1.0.2",
            "latestversion":"2.0.2"
        }
        """

        data0 = requests.get(p1.json_file_viewer("config.json", "update", "version"))
        data1 = requests.get(
            p1.json_file_viewer(
                "config.json", "update", "universal_smart_charging_infrastructure"
            )
        )
        data2 = requests.get(p1.json_file_viewer("config.json", "update", "Main"))
        data3 = requests.get(p1.json_file_viewer("config.json", "update", "dafault_dataset"))
        data4 = requests.get(p1.json_file_viewer("config.json", "update", "config"))

        x, y = json.loads(current_version), json.loads(current_version)
        if x["currentversion"] == y["currentversion"]:
            print(red, "[*].Already Updated", reset)
        else:
            print(green, "[+].Update Available\n[+].Updating Program", reset)
            for i, j in zip(
                (
                    ".version",
                    "universal_smart_charging_infrastructure.py",
                    "Main.py",
                    "default_dataset.json",
                    "config,json",
                ),
                (data0.text, data1.text, data2.text, data3.text, data4.text),
            ):
                with open(i, "w") as file:
                    file.write(j)

            print(blue, "[+].Update Complete", reset)

    def help(self):
        print(
            """   
            {2}Commands{1}            {2} Decription {1}

            {0}get clear    :-{1}{2}clear data(back to default){1}
            {0}get update   :-{1}{2}update program{1}
            {0}get help     :-{1}{2}help about program and its sub_commands{1}
            
        """.format(
                red, reset, blue
            )
        )

    def banner(self, file, car_sel, time_no, car_name, car_capacity_value, pv_esu_grid):
        x, y = PrettyTable(), PrettyTable()
        try:
            for i in range(1, 5):
                names = Main.json_viewer.json_car_viewer(self, file, i, "name")
                capacitys = Main.json_viewer.json_car_viewer(self, file, i, "capacity")
                x.field_names = [
                    f"{red}Sr.No{reset}",
                    f"{red}Car's Name{reset}",
                    f"{red}Car's Capacity{reset}",
                ]
                x.add_row([f"{blue}{i}{reset}", f"{blue}{names}{reset}", f"{blue}{capacitys}{reset}"])

            for j in range(1, 13):
                times = Main.json_viewer.json_time_viewer(self, file, j, j)
                pvs = Main.json_viewer.json_time_viewer(self, file, j, "pv")
                esus = Main.json_viewer.json_time_viewer(self, file, j, "esu")
                grids = Main.json_viewer.json_time_viewer(self, file, j, "grid")
                y.field_names = [
                    f"{red}Sr.No{reset}",
                    f"{red}TimeZone{reset}",
                    f"{red}Pv{reset}",
                    f"{red}Esu{reset}",
                    f"{red}Grid{reset}",
                ]
                y.add_row(
                    [
                        f"{blue}{j}{reset}",
                        f"{blue}{times}{reset}",
                        f"{blue}{pvs}{reset}",
                        f"{blue}{esus}{reset}",
                        f"{blue}{grids}{reset}",
                    ]
                )
        except KeyError:
            pass
        else:
            print(x.get_string())
            print(y.get_string())
            m1 = Main.table_maker()
            m1.print_data_table(file, time_no, car_name, car_capacity_value, pv_esu_grid)
            # m1.print_value_table(car_sel,self.add,pv_value,esu_value,grid_value,self.load,self.mode)

    def main_al(self, file, car_no, time_no, pv_esu_grid):

        p1 = Main.json_viewer()
        # p2 = Main.json_writer()  # Unused variable
        car_name = p1.json_car_viewer(file, car_no, "name")
        car_capacity_value = float(p1.json_car_viewer(file, car_no, "capacity"))  # Convert to float
        time_value = p1.json_time_viewer(file, time_no, time_no)
        pv_value = float(p1.json_time_viewer(file, time_no, "pv"))  # Convert to float
        esu_value = float(p1.json_time_viewer(file, time_no, "esu"))  # Convert to float
        grid_value = p1.json_time_viewer(file, time_no, "grid")

        def addition(car_capacity_value):
            self.demand += car_capacity_value 
            self.sub_total = self.demand
            return self.demand

        def subtraction(time_no):
            i = float(p1.json_time_viewer(file, time_no, pv_esu_grid))
            j = float(p1.json_car_viewer(file, car_no, "capacity"))
            self.sub = i - j
            return self.sub

        addition(car_capacity_value) if pv_esu_grid == "pv" or pv_esu_grid == "esu" else None

        print("Demand is ::", self.demand)
        if self.demand >= pv_value:
            self.load, self.mode = "OverLoad", "[*].ESU2EV [*].GRID2EV"
            self.sub_total = self.sub_total - pv_value  # >> value going to esu_value
            print("Demand-pv=", self.sub_total)

        if self.sub_total >= esu_value:
            self.sub_total = self.sub_total - pv_value - esu_value
            print("demand-pv-esu=", self.sub_total, "  And going to GRID2EV")

        elif esu_value == 0:
            result = int(time_no) - int(1)
            if result != 0:
                esu_value = self.sub_total + float(
                    p1.json_time_viewer(file, result, "esu")
                )
            self.sub = esu_value
            print("Going To ESU2EV")

        else:
            self.load, self.mode = "UnderLoad", "[*].PV2EV [*].PVE2ESU"
            self.sub_total = pv_value - self.sub_total  # self.sub_total == self.demand (demand)
        # Main.clr(self)
        # Logic for writing to 'new_data.txt' goes here (if needed)
        m1 = Main.table_maker()
        m1.print_value_table(
            car_name,  # Pass car name instead of car number
            time_value,
            self.demand,
            pv_value,
            self.sub,
            grid_value,
            self.load,
            self.mode,
        )

        # Main.banner(self,file,car_no,time_no,car_name,car_capacity_value,pv_esu_grid)

    def main(self, file):
        p1 = Main(file)
        p1.banner(file, 1, 1, "nexon", "30.2", "pv")
        # t1 = p1.table_maker()  # Unused variable
        while True:
            try:
                car_sel = input(red + "Enter Car No :- " + reset).split(",")
            except KeyboardInterrupt:
                quit()
            try:
                # Check if any entered car number is within the valid range
                res = any(int(i) >= 1 and int(i) <= 4 for i in car_sel)
                if res:
                    time_sel = input(red + "Enter TimeZone :- " + reset)
                    for i in car_sel:
                        if int(i) >= 1 and int(i) <= 4:
                            if int(time_sel) >= 1 and int(time_sel) <= 5:
                                p1.main_al(file, int(i), int(time_sel), "pv")  # Pass car_no as integer
                            elif int(time_sel) >= 6 and int(time_sel) <= 12:
                                p1.main_al(file, int(i), int(time_sel), "esu")  # Pass car_no as integer
                            else:
                                print(red, "Please Select From 1 To 12", reset)
                        else:
                            print(red, "Select From 1 To 4 OR Enter Value Like This >> 1,2,3", reset)
            except ValueError:
                for i in car_sel:
                    if "get help" in str(i):
                        p1.help()
                    elif "get update" in str(i):
                        p1.check_update()
                        quit()
                    elif "get clear" in str(i):
                        p1.clr()
                        os.system("python Main.py")
                        quit()
                    else:
                        print(red, "Wrong Command", reset)


if __name__ == "__main__":
    p1 = Main("formated_data.json")
    p1.main("formated_data.json")