class Sample:
    def __init__(self):
        self._config = {
            "sample":100,
            "is_created":False,
            "is_active":"Coming"
        }
    
    @property
    def config(self):
        return self._config
    
    
a = Sample()
print(a.config)
a.config["sample"] = 500
print(a.config)
