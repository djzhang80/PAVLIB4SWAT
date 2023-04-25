config={
    "version": "v1",
    "config": {
      "visState": {
        "filters": [],
        "layers": [
          {
            "id": "z7x4adw",
            "type": "geojson",
            "config": {
              "dataId": "rivers",
              "label": "rivers",
              "color": [
                221,
                178,
                124
              ],
              "columns": {
                "geojson": "_geojson"
              },
              "isVisible": True,
              "visConfig": {
                "opacity": 0.8,
                "strokeOpacity": 0.8,
                "thickness": 2,
                "strokeColor": [
                  26,
                  133,
                  171
                ],
                "colorRange": {
                  "name": "Global Warming",
                  "type": "sequential",
                  "category": "Uber",
                  "colors": [
                    "#5A1846",
                    "#900C3F",
                    "#C70039",
                    "#E3611C",
                    "#F1920E",
                    "#FFC300"
                  ]
                },
                "strokeColorRange": {
                  "name": "Global Warming",
                  "type": "sequential",
                  "category": "Uber",
                  "colors": [
                    "#5A1846",
                    "#900C3F",
                    "#C70039",
                    "#E3611C",
                    "#F1920E",
                    "#FFC300"
                  ]
                },
                "radius": 10,
                "sizeRange": [
                  0,
                  10
                ],
                "radiusRange": [
                  0,
                  50
                ],
                "heightRange": [
                  0,
                  500
                ],
                "elevationScale": 5,
                "stroked": True,
                "filled": False,
                "enable3d": False,
                "wireframe": False
              },
              "hidden": False,
              "textLabel": [
                {
                  "field": None,
                  "color": [
                    255,
                    255,
                    255
                  ],
                  "size": 18,
                  "offset": [
                    0,
                    0
                  ],
                  "anchor": "start",
                  "alignment": "center"
                }
              ]
            },
            "visualChannels": {
              "colorField": None,
              "colorScale": "quantile",
              "sizeField": None,
              "sizeScale": "linear",
              "strokeColorField": None,
              "strokeColorScale": "quantile",
              "heightField": None,
              "heightScale": "linear",
              "radiusField": None,
              "radiusScale": "linear"
            }
          }
        ],
        "interactionConfig": {
          "tooltip": {
            "fieldsToShow": {
              "rivers": [
                {
                  "name": "OBJECTID",
                  "format": None
                },
                {
                  "name": "ARCID",
                  "format": None
                },
                {
                  "name": "GRID_CODE",
                  "format": None
                },
                {
                  "name": "FROM_NODE",
                  "format": None
                },
                {
                  "name": "TO_NODE",
                  "format": None
                }
              ]
            },
            "compareMode": False,
            "compareType": "absolute",
            "enabled": True
          },
          "brush": {
            "size": 0.5,
            "enabled": False
          },
          "geocoder": {
            "enabled": False
          },
          "coordinate": {
            "enabled": False
          }
        },
        "layerBlending": "normal",
        "splitMaps": [],
        "animationConfig": {
          "currentTime": None,
          "speed": 1
        }
      },
      "mapState": {
        "bearing": 1.7306903622693106,
        "dragRotate": True,
        "latitude": 25.349762427363043,
        "longitude": 117.98345191684737,
        "pitch": 50.27522937918078,
        "zoom": 10.76383577825254,
        "isSplit": False
      },
      "mapStyle": {
        "styleType": "satellite",
        "topLayerGroups": {},
        "visibleLayerGroups": {},
        "threeDBuildingColor": [
          3.7245996603793508,
          6.518049405663864,
          13.036098811327728
        ],
        "mapStyles": {}
      }
    }
  }