import pprint
# Get the database using the method we defined in pymongo_test_insert file
from pymongo_test_insert import get_database
dbname = get_database()
invasives=["Acer pseudoplatanus",
"Achyranthes japonica",
"Alliaria petiolata",
"Ampelopsis brevipedunculata",
"Anthriscus sylvestris",
"Aralia elata",
"Artemisia vulgaris",
"Arthraxon hispidus",
"Berberis thunbergii",
"Brachypodium sylvaticum",
"Cabomba caroliniana",
"Cardamine impatiens",
"Celastrus orbiculatus",
"Centaurea stoebe",
"Cirsium arvense",
"Cynanchum louiseae",
"Cynanchum rossicum",
"Dioscorea polystachya",
"Dipsacus laciniatus",
"Egeria densa",
"Elaeagnus umbellata",
"Euphorbia cyparissias",
"Euphorbia esula",
"Ficaria verna",
"Frangula alnus",
"Glyceria maxima",
"Heracleum mantegazzianum",
"Humulus japonicus",
"Hydrilla verticillata",
"Hydrocharis morus-ranae",
"Imperata cylindrica",
"Iris pseudacorus",
"Lepidium latifolium",
"Lespedeza cuneata",
"Ligustrum obtusifolium",
"Lonicera japonica",
"Lonicera maackii",
"Lonicera morrowii",
"Lonicera tatarica",
"Lonicera x bella",
"Ludwigia hexapetala",
"Ludwigia peploides",
"Lysimachia vulgaris",
"Lythrum salicaria",
"Microstegium vimineum",
"Murdannia keisak",
"Myriophyllum heterophyllum",
"Myriophyllum heterophyllum x",
"Myriophyllum spicatum",
"Nymphoides peltata",
"Oplismenus hirtellus",
"Persicaria perfoliata",
"(Polygonum perfoliatum)",
"Phellodendron amurense",
"Phragmites australis",
"Phyllostachys aurea",
"Phyllostachys aureosulcata",
"Potamogeton crispus",
"Pueraria montana Kudzu"
"Reynoutria japonica (Fallopia)",
"japonica Polygonum (cuspidatum)",
"Reynoutria sachalinensis",
"Reynoutria x bohemica",
"Fallopia x bohemica",
"Polygonum x",
"bohemica",
"Rhamnus cathartica",
"Rosa multiflora",
"Rubus phoenicolasius ",
"Salix atrocinerea",
"Silphium perfoliatum",
"Trapa natans",
"Vitex rotundifolia"
]
# Create a new collection
collection_name = dbname["'allplants'"]
#item = collection_name.find_one({"Scientific Name with Author":"Abutilon abutiloides (Jacq.) Garcke ex Hochr."})
#pprint.pprint(item)


for sname in invasives:
    items = collection_name.find({"Scientific Name with Author":{'$regex':sname}})
    for item in items:
        if item:
            print(sname," -------- ",item["Scientific Name with Author"])
            collection_name.update_one({"Scientific Name with Author":item["Scientific Name with Author"]},{'$set':{'Inv':['NY']}})
        else:
            print(sname, "------------------ no match")




#item_details = collection_name.find({"Symbol":"ABAB"})
#from pandas import DataFrame
#print(item_details)
# convert the dictionary objects to dataframe
#items_df = DataFrame(item_details)

# see the magic
#print(items_df)

#for item in collection_name.find({"Symbol":"ABAB"}):
#    pprint.pprint(item)
