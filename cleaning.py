def getData():
    import pandas as pd

    raw = pd.read_csv("data/bbga.csv", sep=";")
    raw.head()

    cols_to_keep = [
        "niveau",
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

    data = raw[cols_to_keep]
    data = data[data["niveau"] == 4]
    data = data[(data["jaar"] < 2022) & (data["jaar"] > 2014)]
    data = data.rename(
        columns={
            "WOPP0040_P": "Woonoppervlak_0_40",
            "WOPP4060_P": "Woonoppervlak_40_60",
            "WOPP6080_P": "Woonoppervlak_60_80",
            "WOPP80100_P": "Woonoppervlak_80_100",
            "WOPP100PLUS_P": "Woonoppervlak_100_plus",
            "WOPPONB_P": "Woonoppervlak_onbekend",
            "SRCULTVOORZ_R": "Culturele_voorzieningen",
            "OAANBODBAO_R": "Aanbod_basisscholen",
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

    return data


def getGeoInfo():
    from os import sep
    import pandas as pd

    raw = pd.read_csv("data/lat_and_lon.csv", on_bad_lines="skip", sep=";")

    raw.head(5)

    cols_to_keep = ["Wijkcode", "LNG", "LAT"]

    return raw[cols_to_keep]
