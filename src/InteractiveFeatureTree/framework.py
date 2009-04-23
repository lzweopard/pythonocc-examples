from OCC import AppStd, TDocStd, TCollection, TDF

app = AppStd.AppStd_Application()

h_doc = TDocStd.Handle_TDocStd_Document()
schema = TCollection.TCollection_ExtendedString("MyFormat")
app.NewDocument(schema, h_doc)

doc = h_doc.GetObject()

root = doc.Main()

ts = TDF.TDF_TagSource()

shape_root = ts.NewChild(root)
