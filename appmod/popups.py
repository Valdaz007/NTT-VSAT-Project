from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from mimod.db import DB

# POPUP For Adding VSAT Site to the DB
class ADDVSATPOPUP(Popup):
    add_vid = ObjectProperty(None)
    add_vlat = ObjectProperty(None)
    add_vlon = ObjectProperty(None)

    def add_VSite(cls):
        if cls.add_vid.text == "" or cls.add_vlat.text == "" or cls.add_vlon.text == "":
            return False
        else:
            mv_DB = DB()
            mv_DB.add_VSite(cls.add_vid.text, cls.add_vlat.text, cls.add_vlon.text)
            cls.dismiss()
            return cls.add_vid.text


# POPUP For Removing VSAT Site from the DB
class DELETEVSATPOPUP(Popup):
    del_vid = ObjectProperty(None)
    
    def delete_VSite(cls):
        mv_DB = DB()
        mv_DB.remove_VSite(cls.del_vid.text)
        cls.dismiss()
        return cls.del_vid.text
    
# POPUP For Error Msg
class ERRORPOPUP(Popup):

    def error_VSite(cls):
        if cls.add_vid.text == "" or cls.add_vlat.text == "" or cls.add_vlon.text == "":
            return False
        else:
            mv_DB = DB()
            mv_DB.add_VSite(cls.add_vid.text, cls.add_vlat.text, cls.add_vlon.text)
            cls.dismiss()
            return cls.add_vid.text