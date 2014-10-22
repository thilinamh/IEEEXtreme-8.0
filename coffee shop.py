class Corner:

    def __init__(self):
        self.days={}
        self.benifited_Days={}
        self.num_shops=0
        self.has_3=False
        self.net_benifit=0

    def set_daily_income(self,day,income ):
        self.days[day]=income
        if(income>=5):
            self.benifited_Days[day]=True
        else:
            self.benifited_Days[day]=False

    def set_num_shops(self,num): # only once
        self.num_shops=num
        if(num==3):
            self.has_3=True

    def set_benifit_adjecent(self):
        self.has_3=True

    def has_3_shops(self):
        return self.has_3

    def get_relative_income(self):
        value=0
        for day in self.days:
            value +=self.days[day]/(self.num_shops+1)
        return value


    def set_weekly_benifit(self):

        if(self.has_3_shops()):

            for day in self.benifited_Days:

                if(self.benifited_Days[day]): #is True
                    self.net_benifit +=1


    def get_weekly_benifit(self):
        return self.net_benifit

case=list(map(int,input().split()))

def set_shops(shop_layout,row):
    for corner, num_of_shops in  enumerate(shop_layout):
        if(num_of_shops=='H'):
            row[corner].set_num_shops(3)
        elif(num_of_shops=='M'):
            row[corner].set_num_shops(2)
        elif(num_of_shops=='L'):
            row[corner].set_num_shops(1)

width=case[0]
height=case[1]
grid=[]
for x in range(height):          # initaialize cells
    row=[Corner() for y in range(width)]
    shop_layout=input().split('*')
    set_shops(shop_layout,row)
    grid.append(row)

def set_income_of_day(traffic_layout,row,day): # set income of day by traffic
        for corner, traffic in enumerate(traffic_layout):

            row[corner].set_daily_income(day,traffic)


for x in range(7):
    day = input()
    for row_index in range(height):
        traffic_layout=list(map(int,input().split('*')))
        set_income_of_day(traffic_layout,grid[row_index],day)



'''All data filled'''

'''set ad'''

for x in grid:
    for i in x:
        i.set_weekly_benifit()

def check_up(row_num,corner_num):
    if (row_num-1>=0):
        return grid[row_num-1][corner_num].get_weekly_benifit()
    else:
        return 0

def check_down(row_index,corner_num):
    if(len(grid)>row_index+1):
        return  grid[row_index+1][corner_num].get_weekly_benifit()
    else:
        return 0

def check_left(row_num,corner_num):
    if(corner_num-1>=0):
        return grid[row_num][corner_num-1].get_weekly_benifit()
    else:
        return 0

def check_right(row_num,corner_num):
    if(corner_num+1<width):
        return grid[row_num][corner_num+1].get_weekly_benifit()
    else:
        return 0
income_grid=[]
for row_index,row in enumerate(grid):
    income_row=[]
    for corner_num,corner in enumerate(row):
        if(not corner.has_3_shops()):
            up_benifit=check_up(row_index,corner_num)
            down_benifit=check_down(row_index,corner_num)
            left_benifit=check_left(row_index,corner_num)
            right_benifit=check_right(row_index,corner_num)
            traffic_benifit=corner.get_relative_income()

            income_row.append(up_benifit+down_benifit+right_benifit+left_benifit+traffic_benifit)
        else:
            income_row.append(0)
    income_grid.append(income_row)
new=[]
for position,val in enumerate(income_grid):
    new.append(max(val))
tmp=max(new)
if(tmp>=20):
    grid_idx=new.index(tmp)
    y=income_grid[grid_idx].index(tmp)
    print(grid_idx+1,y+1)
else:
    print(-1,-1)

