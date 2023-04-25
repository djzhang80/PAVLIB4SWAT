config={
    "version": "v1",
    "config": {
      "visState": {
        "filters": [],
        "layers": [
          {
            "id": "25mimyh",
            "type": "geojson",
            "config": {
              "dataId": "subbasin",
              "label": "subbasin",
              "color": [
                117,
                222,
                227
              ],
              "columns": {
                "geojson": "_geojson"
              },
              "isVisible": True,
              "visConfig": {
                "opacity": 0.01,
                "strokeOpacity": 0.8,
                "thickness": 1,
                "strokeColor": [
                  18,
                  147,
                  154
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
                "filled": True,
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
              "discharge_pb": [
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
              ],
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
              ],
              "subbasin": [
                {
                  "name": "OBJECTID",
                  "format": None
                },
                {
                  "name": "GRIDCODE",
                  "format": None
                },
                {
                  "name": "Subbasin",
                  "format": None
                },
                {
                  "name": "Area",
                  "format": None
                },
                {
                  "name": "Lat",
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
        "latitude": 25.425301338223125,
        "longitude": 118.0069876558284,
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