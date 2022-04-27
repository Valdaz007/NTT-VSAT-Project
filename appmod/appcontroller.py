from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.garden.mapview import MapView, MapMarker, MapMarkerPopup
from kivy.properties import ObjectProperty
from appmod.db import DB
from appmod.popups import ADDVSATPOPUP

class SM(ScreenManager):
    pass

class AppContent(Screen):
    mv_Main = ObjectProperty(None)
    markers = {}
    mv_DB = DB()

    def create_MapMarker(cls, lat: str, lon: str):
        return SiteMapMarker(lat=lat, lon=lon)


    def add_MapMarker(cls, marker):
        '''
        add_MapMarker Plots the SiteMapMarker on the MapView 
        '''
        cls.mv_Main.add_marker(marker)


    def rmv_MapMarker(cls, vid):
        print(vid)
        for marker in cls.markers.keys():
            if marker == vid:
                cls.mv_Main.remove_marker(cls.markers[vid])


    def new_MapMarker(cls, vid):
        '''
        new_MapMarker using the 'vid' argument pulls the VSAT data from the DB
        and Plots a SiteMapMarker on the MapView.
        '''
        sites = cls.mv_DB.pull_Site(tbl_Name = "vsat")
        if sites != False:
            for site in sites:
                if site[0] == vid:
                    print(f"site[0] - {site[0]}")
                    cls.markers[site[0]] = cls.create_MapMarker(site[1], site[2])
                    cls.add_MapMarker(cls.markers[site[0]])


    def add_DBMarkers(cls):
        '''
            This function servers to pull VSAT data from the database return it
        '''
        # Pulling Sites From db.py
        sites = cls.mv_DB.pull_Site(tbl_Name = "vsat")
        if sites == False:
            print("DB Error!")
        else:
            for site in sites:
                cls.markers[site[0]] = cls.create_MapMarker(site[1], site[2])
                cls.add_MapMarker(cls.markers[site[0]])
            print(cls.markers.keys())


    def on_btnPress(cls, code: str):
        '''
        on_btnPress depending on the 'code' argument pulls data from the province table
        and change the focus to the new coordinates in the center.
        '''
        provinces = cls.mv_DB.pull_Site(tbl_Name="province")
        if provinces != False:
            for province in provinces:
                if province[0] == code:
                    cls.mv_Main.center_on(float(province[1]), float(province[2]))


    def openDB(cls):
        cls.mv_DB.open_DBConn()

    def closeDB(cls):
        cls.mv_DB.close_DBConn()


    def showAddPopup(cls):
        cls.show = ADDVSATPOPUP()
        cls.show.open()


# Kivy's MapView Module
class MainMapView(MapView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.zoom = 5


class SiteMapMarker(MapMarkerPopup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source="markericon.png"
