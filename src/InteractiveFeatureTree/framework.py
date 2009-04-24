from OCC import AppStd, TDocStd, TCollection, TDF

#
# Create a default Application object. You only need one of these per process
#
app = AppStd.AppStd_Application()

#
# Make a Standard document
#
h_doc = TDocStd.Handle_TDocStd_Document()

#I'm going to invent my own document structure as I go along
schema = TCollection.TCollection_ExtendedString("MyFormat")
app.NewDocument(schema, h_doc)

doc = h_doc.GetObject()

root = doc.Main()

ts = TDF.TDF_TagSource()

#
# We'll add all shapes under this node in the label tree 
#
shape_root = ts.NewChild(root)
