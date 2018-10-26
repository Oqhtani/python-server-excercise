Class Udacian:

    def __init__(self,name,city,enrollment,nanodegree,status):
        self.name=name
        self.city=city
        self.enrollment=enrollment
        self.nanodegree=nanodegree
        self.status=status

    def print_udacian(self):
        print(self.name+" are from "+self.city+". they are "+self.enrollment
        +" in the "+self.nanodegree+" and are "+self.status)
