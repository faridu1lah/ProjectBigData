import pandas as pd
raw = pd.read_csv("BBGA_CSV.csv",sep=",")

cols_to_keep = ["niveau",
                "niveaunaam",
                "gebiedcodenaam",
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
                "WWOZ_M2"


                
]

data = raw[cols_to_keep]
data = data[data["niveau"] == 4]
data = data[(data["jaar"] < 2022) & (data["jaar"] > 2014)]
data = data.rename(columns = {"WOPP0040_P":"Woonoppervlak 0-40",
                 "WOPP4060_P":"Woonoppervlak 40-60",
                 "WOPP6080_P":"Woonoppervlak 60-80",
                 "WOPP80100_P":"Woonoppervlak 80-100",
                 "WOPP100PLUS_P":"Woonoppervlak 100+",
                 "WOPPONB_P":"Woonoppervlak onbekend",
                 "SRCULTVOORZ_R":"Culturele voorzieningen",
                 "OAANBODBAO_R":"Aanbod basisscholen",
                 "WDICHT":"Woningdichtheid",
                 "BEVEENOUDERHH_P":"Eenouder huishouden",
                 "BEVALLEENHH_P":"Eenpersoons huishouden",
                 "BEVPAARZKINDHH_P":"Stel zonder kind huishouden",
                 "BEVPAARMKINDHH_P":"Stel met kind huishouden",
                 "BEVOVERIGHH_P":"overige huishouden",
                 "WCORHUUR_P":"Corporatiewoningen ",
                 "WPARTHUUR_P":"Particuliere huur",
                 "WKOOP_P":"Koopwoninging ",
                 "WWOZ_M2":"WOZ per M2"})
    