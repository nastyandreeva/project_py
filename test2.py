import sys
import clr
# import Revit API
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
# import Revit API UI
clr.AddReference('RevitAPIUI')
# import Revit Services
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
# import ProtoGeometry
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
# get the current Revit Document
doc = DocumentManager.Instance.CurrentDBDocument
# get the current Revit application
app = DocumentManager.Instance.CurrentUIApplication.Application
# get the current UI application
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application


list_categories = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors).WhereElementIsNotElementType().ToElements()

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []
list13 = []
list14 = []
list15 = []

for p in list_categories:
	typeId = p.GetTypeId()
	type = doc.GetElement(typeId)
	type = type..sssfhdf
	#type.Family.Name = '"' + type.Family.Name + '"'
	try:
		a = p.Id
	except:
		a = 0
	list1.append(a)
	try:
		b = p.UniqueId
	except:
		b = 0
	list2.append(b)
	try:
		c = p.LookupParameter("Navisworks").AsString()
	except:
		c = 0
	list3.append(c)
	try:
		d = p.LookupParameter("Уровень").AsValueString()
	except:
		d = 0
	list4.append(d)
	try:
		e = p.LookupParameter("Номер секции №").AsString()
	except:
		e = 0
	list5.append(e)
	try:
		f = p.LookupParameter("Категория").AsValueString()
	except:
		f = 0
	list6.append(f)
	try:
		g = p.Name
	except:
		g = 0
	list8.append(g)
	try:
		h = p.LookupParameter("Длина").AsValueString()
	except:
		h = 0
	list9.append(h)
	try:
		i = p.LookupParameter("Площадь").AsValueString()
	except:
		i = 0
	list10.append(i)
	try:
		j = p.LookupParameter("Объем").AsValueString()
	except:
		j = 0
	list11.append(j)
	try:
		k = p.LookupParameter("Смещение снизу").AsValueString()
	except:
		k = 0
	list12.append(k)
	try:
		l = p.LookupParameter("Смещение сверху").AsValueString()
	except:
		l = 0
	list13.append(l)
	try:
		o = p.Symbol.LookupParameter("Ширина").AsDouble()
	except:
		o = 0
	list14.append(str(o))
	try:
		w = p.Symbol.LookupParameter("Высота").AsDouble()
	except:
		w = 0
	list15.append(str(w))
	list7.append(type)
print(list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11, list12, list13, list14, list15)