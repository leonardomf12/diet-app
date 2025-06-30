To simplify the work, instead of having a postgresDB we just place all the foods in a .xlxs file within Google Drive and then manually download it and place it in this folder.
TODO: Make this update automatic within the update_food_db.py
TODO: Migrate this completely to postgresDB, by using docker.

For now:
- **Download the nutrition.xlxs file as.csv**, available in: [Google Drive Nutrition Link](https://docs.google.com/spreadsheets/d/1SMGnkb-xJI20_nDpeZXeAP8sfdtYadh0/edit?usp=sharing&ouid=110009915235291964139&rtpof=true&sd=true)
- Move it to this dir: `/repo/src/db/nutrition.csv`
- Run the `update_food_db.py` to update the .json file

Each food is represented by the following structure: 

```json
{
    "BaseUnits": "g",
    "Brand": "Lidl",
    "Description": "Embalagem 600g - 24/25 fatias",
    "Name": "Pão integral lidl",
    "price": [
      {
        "units": 100,
        "price_per_unit": 1.5
      }
    ],
    "units": {
      "slice" : {
        "unit": 20,
        "kcals": 61,
        "protein": 2.4,
        "carbhid": 10.5,
        "fat": 0.8},
      "100g" : {
        "unit": 100,
        "kcals": 265,
        "protein": 9,
        "carbhid": 49,
        "fat": 3.2}
  }
  }
```