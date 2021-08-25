'''
This script allows to extract the description of elements (in this case SystemFunctions) with html format and as plain text

It will create a folder result in the selected Capella project with the resulting xlsx file.
'''

# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *
    
# include needed for utilities
include('workspace://Python4Capella/utilities/CapellaPlatform.py')
if False:
    from utilities.CapellaPlatform import *
    
# include needed to read/write xlsx files
from openpyxl import *
# additional import for html format description parsing
from io import StringIO
from html.parser import HTMLParser

# this code to retrieve plain text from html format was found here: https://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

# change this path to execute the script on your model
aird_path = '/In-Flight Entertainment System/In-Flight Entertainment System.aird'
model = CapellaModel()
model.open(aird_path)

# gets the SystemEngineering and print its name
se = model.get_system_engineering()
print('starting export of model ' + se.get_name())

# preparing excel file export
project_name = aird_path[0:(aird_path.index("/", 1) + 1)]
project = CapellaPlatform.getProject(project_name)
folder = CapellaPlatform.getFolder(project, 'results')
xlsx_file_name = CapellaPlatform.getAbsolutePath(folder) + '/' + 'Need8.xlsx'
# create a workbook
workbook = Workbook()


# writing excel file header
worksheet = workbook.active
worksheet.title = 'Elements Description'
worksheet["A1"] = 'Element Name'
worksheet["B1"] = 'HTML Description'
worksheet["C1"] = 'Plain text description'

i=2

# retrieving elements from the model
for elem in se.get_all_contents_by_type(SystemFunction):
    elem = SystemFunction(elem)
    worksheet["A" + str(i)] = elem.get_name()
    worksheet["B" + str(i)] = elem.get_description()
    if elem.get_description() != None:
        worksheet["C" + str(i)] = strip_tags(elem.get_description())
    i = i+1
        
# Save the xlsx file
workbook.save(xlsx_file_name)

print('saving excel file')

# refresh 
CapellaPlatform.refresh(folder)