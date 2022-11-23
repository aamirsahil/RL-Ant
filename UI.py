class UI:
    def __init__(self) -> None:
        self.width = 10
        self.height = 10
        self.boundary = 'periodic'

        self.agent_no = 10
        self.total_time = 10
    def readData(self):
        data = {}
        return data
    def setData(self, width=10, height=10, agent_no=10, boundary='periodic', total_time=10):
        self.width = width
        self.height = height
        self.boundary = boundary

        self.agent_no = agent_no
        self.total_time = total_time  
    def getData(self):
        world_data = {
            'width' : self.width,
            'height' : self.height,
            'boundary' : self.boundary
        }
        data = {
            'total_time' : self.total_time,
            'agent_no' : self.agent_no,
            'world_data' : world_data
        }
        return data