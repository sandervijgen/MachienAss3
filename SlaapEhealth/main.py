import random
import time
class CleaningRobot:
    def __init__(self,start,cleaningList):
        self.batterij = 100
        self.capacity = 10
        self.position = start
        self.cleaningList = cleaningList

    def subtacktFromCleanList(self,trash):
        self.cleaningList.remove(trash)

    def move(self, afstand, destination):
        self.batterij -= afstand
        self.position = destination

    def checkMovePosible(self,afstand):
        if(self.batterij > afstand):
            return 1
        else:
            return 0

    def leegVuilbak(self,trash):
        self.capacity -= 1
        self.subtacktFromCleanList(trash)

    def checkCapacity(self):
        if(self.capacity > 0):
            return 1
        else:
            return 0

    def leegZelf(self):
        self.capacity = 10

    def charge(self):
        self.batterij = 100

class Trash:
    def __init__(self, name):
        self.name = name
    def Name(self):
        return self.name

class Plug:
    def __init__(self, name):
        self.name = name
    def Name(self):
        return self.name

class Door:
    def __init__(self, name):
        self.name = name
    def Name(self):
        return self.name

class Emptier:
    def __init__(self, name):
        self.name = name
    def Name(self):
        return self.name

class Knoop:
    def __init__(self, name):
        self.name = name
    def Name(self):
        return self.name

class CleaningRobotGraph:
    def __init__(self):
        self.graph = {}

    def AddNode(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def add_connection(self, place1, place2, distance_weight, interuping_weight):
        if place1 in self.graph:
            self.graph[place1][place2] = (distance_weight, interuping_weight)
        if place2 in self.graph:
            self.graph[place2][place1] = (distance_weight, interuping_weight)

    def display_graph(self):
        for node in self.graph:
            connections = self.graph[node]
            print(connections)


class tryModel:
    def __init__(self, robot, graph):
        self.points = 0
        self.robot = robot
        self.graph = graph
        self.actionsList = []

    def actions(self):
        randomChoise = 0;
        #can do at each location
        if isinstance(self.robot.position, Trash):
            if(self.robot.checkCapacity()):
                if(self.robot.position in self.robot.cleaningList):
                        self.robot.leegVuilbak(self.robot.position)
                        self.points += 10
                        self.actionsList.append("empty Trash at " + self.robot.position.Name()+ " points = "  + str(self.points))


        if isinstance(self.robot.position, Plug):
            randomChoise = random.randint(0, 1)
            if(randomChoise == 0):
                self.robot.charge()
                self.points -= 5
                self.actionsList.append("charge at " + self.robot.position.Name()+ " points = "  + str(self.points))



        if isinstance(self.robot.position, Emptier):
            #if(take):
                self.robot.leegZelf()
                self.points -= 1
                self.actionsList.append("Emptie self at " + self.robot.position.Name() + " points = "  + str(self.points))

        if isinstance(self.robot.position, Door):
            self.points -= 2

        #can move to different location
        connections = self.graph[self.robot.position]
        posibilities = 0
        for key in connections:
            Values = connections[key]
            distance = Values[0]
            disconfort = Values[1]
            if (self.robot.checkMovePosible(distance)):
                posibilities += 1

        if(posibilities < 1): #als niks kan bewegen omdat batterij plat dan opladen voor 100 punten en opnieuw proberen
            self.robot.charge()
            self.points -= 100
            self.actionsList.append("Emergency charge :(("+ " points = "  + str(self.points))
            for key in connections:
                posibilities += 1

        randomChoise = random.randint(0,posibilities)
        momenteel = 0;
        for key in connections:
            Values = connections[key]
            distance = Values[0]
            disconfort = Values[1]
            randomChoise = random.randint(0, 1)
            if(randomChoise == momenteel):
                self.robot.move(distance,key)
                self.points -= (distance*disconfort)
                self.actionsList.append("Now at " + self.robot.position.Name()+ " points = "  + str(self.points))
                return 1
            momenteel+=1

def makeGraphe():
    office_layout = CleaningRobotGraph()

    # Add nodes to the graph
    trash_a = Trash("Trash A")
    trash_b = Trash("Trash B")
    trash_c = Trash("Trash C")
    trash_d = Trash("Trash D")
    trash_e = Trash("Trash E")
    trash_f = Trash("Trash F")
    trash_g = Trash("Trash G")
    trash_h = Trash("Trash H")

    cleaningList = [trash_a,trash_b,trash_c,trash_d,trash_e,trash_f,trash_g,trash_h]

    office_layout.AddNode(trash_a)
    office_layout.AddNode(trash_b)
    office_layout.AddNode(trash_c)
    office_layout.AddNode(trash_d)
    office_layout.AddNode(trash_e)
    office_layout.AddNode(trash_f)
    office_layout.AddNode(trash_g)
    office_layout.AddNode(trash_h)

    plug_i = Plug("Plug I")
    plug_j = Plug("Plug J")
    plug_k = Plug("Plug K")
    plug_l = Plug("Plug L")
    plug_m = Plug("Plug M")
    plug_n = Plug("Plug N")
    plug_o = Plug("Plug O")
    plug_p = Plug("Plug P")
    plug_q = Plug("Plug Q")
    plug_r = Plug("Plug R")

    office_layout.AddNode(plug_i)
    office_layout.AddNode(plug_j)
    office_layout.AddNode(plug_k)
    office_layout.AddNode(plug_l)
    office_layout.AddNode(plug_m)
    office_layout.AddNode(plug_n)
    office_layout.AddNode(plug_o)
    office_layout.AddNode(plug_p)
    office_layout.AddNode(plug_q)
    office_layout.AddNode(plug_r)

    emptier = Emptier("emptier")
    office_layout.AddNode(emptier)

    door_t = Door("Door T")
    door_u = Door("Door U")
    door_v = Door("Door V")
    door_w = Door("Door W")
    door_x = Door("Door X")
    door_y = Door("Door Y")
    door_z = Door("Door Z")

    office_layout.AddNode(door_t)
    office_layout.AddNode(door_u)
    office_layout.AddNode(door_v)
    office_layout.AddNode(door_w)
    office_layout.AddNode(door_x)
    office_layout.AddNode(door_y)
    office_layout.AddNode(door_z)

    knoop_1 = Knoop("1")
    knoop_2 = Knoop("2")
    knoop_3 = Knoop("3")
    knoop_4 = Knoop("4")
    knoop_5 = Knoop("5")
    knoop_6 = Knoop("6")

    office_layout.AddNode(knoop_1)
    office_layout.AddNode(knoop_2)
    office_layout.AddNode(knoop_3)
    office_layout.AddNode(knoop_4)
    office_layout.AddNode(knoop_5)
    office_layout.AddNode(knoop_6)

    office_layout.add_connection(plug_p, trash_b, 1, 1)
    office_layout.add_connection(trash_a, trash_b, 1, 1)
    office_layout.add_connection(trash_a, door_t, 6, 2)
    office_layout.add_connection(trash_a, door_u, 8, 3)
    office_layout.add_connection(door_t, door_u, 10, 5)
    office_layout.add_connection(door_t, plug_o, 7, 4)
    office_layout.add_connection(door_t, door_v, 10, 2)
    office_layout.add_connection(trash_h, door_v, 7, 2)
    office_layout.add_connection(trash_h, plug_n, 1, 1)
    office_layout.add_connection(plug_n, plug_p, 9, 1)
    office_layout.add_connection(door_v, plug_q, 3, 4)
    office_layout.add_connection(door_v, trash_g, 5, 1)
    office_layout.add_connection(plug_q, door_w, 5, 2)
    office_layout.add_connection(trash_g, door_x, 2, 1)
    office_layout.add_connection(trash_g, door_w, 3, 1)
    office_layout.add_connection(door_w, door_x, 3, 1)
    office_layout.add_connection(door_u, knoop_1, 1, 3)
    office_layout.add_connection(knoop_2, knoop_1, 6, 3)
    office_layout.add_connection(knoop_2, knoop_3, 6, 3)
    office_layout.add_connection(knoop_3, knoop_4, 6, 4)
    office_layout.add_connection(knoop_4, knoop_5, 2, 4)
    office_layout.add_connection(knoop_5, knoop_6, 3, 4)
    office_layout.add_connection(knoop_1, plug_r, 5, 5)
    office_layout.add_connection(knoop_2, plug_i, 5, 1)
    office_layout.add_connection(knoop_3, plug_j, 5, 4)
    office_layout.add_connection(knoop_4, plug_k, 5, 4)
    office_layout.add_connection(knoop_3, door_w, 1, 1)
    office_layout.add_connection(plug_k, trash_e, 1, 4)
    office_layout.add_connection(knoop_5, knoop_2, 3, 1)
    office_layout.add_connection(knoop_5, trash_f, 2, 5)
    office_layout.add_connection(knoop_6, door_x, 2, 2)
    office_layout.add_connection(knoop_6, door_y, 1, 3)
    office_layout.add_connection(knoop_6, door_z, 1, 3)
    office_layout.add_connection(door_z, trash_d, 4, 2)
    office_layout.add_connection(trash_d, plug_l, 1, 1)
    office_layout.add_connection(door_y, trash_c, 5, 3)
    office_layout.add_connection(door_y, plug_m, 5, 1)
    office_layout.add_connection(trash_c, plug_m, 5, 1)
    office_layout.add_connection(knoop_5, emptier, 16, 1)

    office_layout.display_graph()

    robot = CleaningRobot(plug_k,cleaningList)
    model = tryModel(robot,office_layout.graph)
    while(len(robot.cleaningList) != 0):
        model.actions()
    print(len(robot.cleaningList))
    print(model.actionsList)


if __name__ == "__main__":
    makeGraphe()


