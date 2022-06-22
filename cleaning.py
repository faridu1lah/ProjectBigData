from sklearn.metrics import jaccard_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import json
from shapely.validation import make_valid
from shapely.geometry import Polygon

def getData():
    raw = pd.read_csv("data/bbga.csv",sep=";")

    raw = raw.replace(",", ".", regex=True)

    cols_to_keep = ["niveau",
                "niveaunaam",
                "gebiedcodenaam",
                "gebiedcode22",
                "jaar",
                "WOPP0040_P",
                "WOPP4060_P",
                "WOPP6080_P",
                "WOPP80100_P",
                "WOPP100PLUS_P",
                "WOPPONB_P",
                "VCRIMIN_I",
                "SRCULTVOORZ_R",
                "OAANBODBAO_R",
                "WDICHT",
                "BEVEENOUDERHH_P",
                "BEVALLEENHH_P",
                "BEVPAARZKINDHH_P",
                "BEVPAARMKINDHH_P",
                "BEVOVERIGHH_P",
                "WCORHUUR_P",
                "WPARTHUUR_P",
                "WKOOP_P",
                "WWOZ_M2",
                
    ]
    colsint = [     "jaar",
                "WOPP0040_P",
                "WOPP4060_P",
                "WOPP6080_P",
                "WOPP80100_P",
                "WOPP100PLUS_P",
                "WOPPONB_P",
                "WDICHT",
                "BEVEENOUDERHH_P",
                "BEVALLEENHH_P",
                "BEVPAARZKINDHH_P",
                "BEVPAARMKINDHH_P",
                "BEVOVERIGHH_P",
                "WCORHUUR_P",
                "WPARTHUUR_P",
                "WKOOP_P",
                "WWOZ_M2",
                
    ]
    data = raw[cols_to_keep]

    data[cols_to_keep]=data[cols_to_keep].fillna(data.mean().iloc[0])
    data[colsint] = data[colsint].apply(pd.to_numeric)



    data = data[data["niveau"] == 4]


    data = data[(data["jaar"] < 2021) & (data["jaar"] > 2015)]

    #crime rates aren't available for 2021
    data = data.drop(["VCRIMIN_I"],axis=1)
    data = data.drop(["OAANBODBAO_R"],axis=1)
    data = data.drop(["SRCULTVOORZ_R"],axis=1)







    data = data.rename(
        columns={
            "WOPP0040_P": "Woonoppervlak_0_40",
            "WOPP4060_P": "Woonoppervlak_40_60",
            "WOPP6080_P": "Woonoppervlak_60_80",
            "WOPP80100_P": "Woonoppervlak_80_100",
            "WOPP100PLUS_P": "Woonoppervlak_100_plus",
            "WOPPONB_P": "Woonoppervlak_onbekend",
            "WDICHT": "Woningdichtheid",
            "BEVEENOUDERHH_P": "Eenouder_huishouden",
            "BEVALLEENHH_P": "Eenpersoons_huishouden",
            "BEVPAARZKINDHH_P": "Stel_zonder_kind_huishouden",
            "BEVPAARMKINDHH_P": "Stel_met_kind_huishouden",
            "BEVOVERIGHH_P": "overige_huishouden",
            "WCORHUUR_P": "Corporatiewoningen",
            "WPARTHUUR_P": "Particuliere_huur",
            "WKOOP_P": "Koopwoninging",
            "WWOZ_M2": "WOZ_per_M2",
            "gebiedcode22": "wijkcode",
        }
    )

    

    le = LabelEncoder()

    data["gebiedscode"] = le.fit_transform(data["gebiedcodenaam"])
    data = get_woz_features(data)
    
    return data
def get_woz_features(data):

    data = data.sort_values(by=["gebiedcodenaam", "jaar"])
    data["WWOZ_PREV1"] = data.groupby("gebiedcodenaam")["WOZ_per_M2"].transform(
        lambda x: x.shift(1)
    )


    # fill first dataset entry(s) with first known WOZ value, if missing
    
    data["WWOZ_PREV1"] = data.groupby("gebiedcodenaam")["WWOZ_PREV1"].transform(lambda x: x.fillna(x.min()))
    return data

def getGeoInfo():
    # from os import sep


    raw = pd.read_csv("data/lat_and_lon.csv", sep=";")
    jsonData = pd.read_json("https://maps.amsterdam.nl/open_geodata/geojson_lnglat.php?KAARTLAAG=INDELING_WIJK&THEMA=gebiedsindeling")

    # pol = Polygon(
    #     [
    #         [
    #             [4.8674055, 52.3717966],
    #             [4.8695858, 52.368605],
    #             [4.8708093, 52.3668503],
    #             [4.8737991, 52.3677141],
    #             [4.8768091, 52.3685032],
    #             [4.8766794, 52.368677],
    #             [4.8763027, 52.3689665],
    #             [4.8759929, 52.3692536],
    #             [4.8758061, 52.3694618],
    #             [4.8756743, 52.3696392],
    #             [4.8750449, 52.3706832],
    #             [4.8745033, 52.3718889],
    #             [4.8744518, 52.37206],
    #             [4.8744399, 52.372201],
    #             [4.8744832, 52.3723237],
    #             [4.8745554, 52.3724494],
    #             [4.8746452, 52.372562],
    #             [4.874783, 52.3726898],
    #             [4.8748307, 52.3727266],
    #             [4.8751684, 52.3729238],
    #             [4.8752354, 52.3729742],
    #             [4.8752958, 52.3730353],
    #             [4.8753841, 52.3731502],
    #             [4.8754317, 52.3732351],
    #             [4.8754871, 52.37341],
    #             [4.8674055, 52.3717966],
    #         ]
    #     ]
    # )

    # pol.is_valid

    # valid = make_valid()

    # print(valid)

    polygon = pd.DataFrame()
    polygon["coordinates"] = jsonData["features"].apply(lambda row: json.dumps(row["geometry"]["coordinates"]))
    polygon["wijkcode"] = jsonData["features"].apply(lambda row: row["properties"]["Wijkcode"])

    cols_to_keep = ["Wijkcode", "LNG", "LAT"]
    data = raw[cols_to_keep].rename(columns={"LAT": "lat", "LNG": "lon", "Wijkcode": "wijkcode"})

    final = pd.merge(data, polygon, on="wijkcode")

    final.head()
    return final
