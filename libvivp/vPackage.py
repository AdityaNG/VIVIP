import json
from .utils import is_vivp_file
"""
vPackages or Verilog Packages are folders with a vpackage.json file.
The chache and dependencies are stored in the .vpackage/ and .vpackage/repos respectively. 
The .vpackage/ directory can be added to .gitignore and will be regenrated. 

vpackage.json sample 

```
{

    'packageDetails': {
        'packageName' : '',
        'packageAuthors' : [],
    },

    'packageURL': '',
    
    'testBench': [],
 
    'dependencyList': []

}

```
"""




class vPackage:
    """
    vPackage class takes filePath to vpackage.json as argument and loads it to self.data

    If it is marked as saveable, write will be allowed

    If it is marked as createNew, a new blank vpackage.json will be written
    """
    def __init__(self, data=None, filePath=False, saveable=False, createNew=False):
        if filePath and not data:       # filePath is provided
            self.filePath = filePath
            self.saveable = saveable
            
            if is_vivp_file(filePath):    # load from filePath
                with open(filePath) as f:
                    self.data = json.load(f)
            elif createNew:             # create new
                self.data = self.getBlankPackageData()
                self.save()
            else:
                raise Exception("Not a vPackage")
        
        elif data and not filePath:     # data is provided
        
            if saveable:
                raise Exception("vPackage without filePath is not saveable")
            self.data = data
            self.filePath = False
            self.saveable = False
        else:
            raise Exception("vPackage initializes with either data or filePath, not both")
        pass

    def load(self):
        """
        Loads the vpackage.json to self.data
        """
        with open(self.filePath) as f:
            self.data = json.load(f)

    def save(self):
        """
        Writes changes to the vpackage.json
        """
        if not self.saveable:
            raise Exception("Write attempt to write protected package")
        
        # Save to self.filePath
        with open(self.filePath, 'w') as json_file:
            json.dump(self.data, json_file)

    def getBlankPackageData(self):
        return {
            'packageDetails': {
                'packageName' : '',
                'packageAuthors' : [],
            },
            'packageURL': '',
            'fileList': [],
            'testBench': [],
            'dependencyList': []
        }
    
    def has_dependency(self, d):
        """
        Returns True if d in self.data['dependencyList'], False otherwise
        """
        # return d in self.data['dependencyList']
        for dep in self.data['dependencyList']:
            if d == dep:
                return True
        return False
    
    def has_file(self, d):
        """
        Returns True if d in self.data['fileList'], False otherwise
        """
        for dep in self.data['fileList']:
            if d == dep:
                return True
        return False
    
    def has_testbench(self, d):
        """
        Returns True if d in self.data['testBench'], False otherwise
        """
        for dep in self.data['testBench']:
            if d == dep:
                return True
        return False

    def __repr__(self):
        return "vPackage()"
    
    def __str__(self):
        return json.dumps(self.data, indent=4, sort_keys=True)
        