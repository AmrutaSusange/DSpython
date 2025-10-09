class DatabaseSession:
    def __init__(self, name):
        self.name = name
        self.connected = False

    def __enter__(self):
        print(f"Connecting to database '{self.name}'...")
        self.connected = True
        return self  # 👈 return self so 'db' becomes usable in with-block

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to '{self.name}'...")
        self.connected = False
        if exc_type:
            print(f"Error occurred: {exc_val}")
        return False  # don’t suppress exceptions

    def query(self, sql):
        if not self.connected:
            raise Exception("Not connected to database.")
        print(f"Executing SQL: {sql}")
        # Simulate returning data
        return [{"id": 1, "name": "Amruta"}, {"id": 2, "name": "Debanjan"}]