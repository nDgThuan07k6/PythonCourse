class DatabaseConnection:
    _instance = None
    def __init__(self, connectionString):
        if DatabaseConnection._instance is not None:
            raise Exception('This class is a singleton. Use get_instance() instead')
        else:
            self.connectionString = connectionString
            print(f'Database connected with {connectionString}')
            DatabaseConnection._instance = self

    @classmethod
    def  get_instance(cls, connectionString = None):
        if cls._instance is None:
            cls._instance = DatabaseConnection(connectionString)
        return cls._instance
    
db1 = DatabaseConnection.get_instance("Server=Localhost;DB=TestDB")
db2 = DatabaseConnection.get_instance("Server=Backup;DB=OtherDB")
print(db1 is db2)