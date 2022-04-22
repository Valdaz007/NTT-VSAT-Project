from kivy.uix.screenmanager import Screen
from kivy.garden.mapview import MapView, MapMarker, MapMarkerPopup
from kivy.properties import ObjectProperty
from mimod.db import DB
from mimod.popups import *

class AppContent(Screen):
    mv_Main = ObjectProperty(None)
    markers = {}
    mv_DB = DB()
    
    def create_MapMarker(cls, lat: str, lon: str):
        return SiteMapMarker(lat=lat, lon=lon)

    def add_MapMarker(cls, marker):
        cls.mv_Main.add_marker(marker)

    def rmv_MapMarker(cls, vid):
        print(vid)
        for marker in cls.markers.keys():
            if marker == vid:
                cls.mv_Main.remove_marker(cls.markers[vid])

    def new_MapMarker(cls, vid):
        print(vid)
        cls.openDB()
        sites = cls.mv_DB.pull_Site(tbl_Name = "vsat")
        if sites != False:
            for site in sites:
                if site[0] == vid:
                    print(f"site[0] - {site[0]}")
                    cls.markers[site[0]] = cls.create_MapMarker(site[1], site[2])
                    cls.add_MapMarker(cls.markers[site[0]])
        cls.closeDB()

    def add_DBMarkers(cls):
        # Pulling Sites From db.py
        sites = cls.mv_DB.pull_Site(tbl_Name = "vsat")
        if sites == False:
            print("DB Error!")
        else:
            for site in sites:
                cls.markers[site[0]] = cls.create_MapMarker(site[1], site[2])
                cls.add_MapMarker(cls.markers[site[0]])
            print(cls.markers.keys())
        cls.closeDB()

    def on_btnPress(cls, code: str):
        cls.openDB()
        provinces = cls.mv_DB.pull_Site(tbl_Name="province")
        if provinces != False:
            for province in provinces:
                if province[0] == code:
                    cls.mv_Main.center_on(float(province[1]), float(province[2]))
        cls.closeDB()
    
    def openDB(cls):
        cls.mv_DB.open_DBConn()

    def closeDB(cls):
        cls.mv_DB.close_DBConn()


class MainMapView(MapView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.zoom = 5


class SiteMapMarker(MapMarkerPopup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source="markericon.png"