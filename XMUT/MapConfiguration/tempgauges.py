config={
    "version": "v1",
    "config": {
      "visState": {
        "filters": [],
        "layers": [
          {
            "id": "0sjxaip",
            "type": "geojson",
            "config": {
              "dataId": "tempgauge",
              "label": "tempgauge",
              "color": [
                71,
                211,
                217
              ],
              "columns": {
                "geojson": "_geojson"
              },
              "isVisible": True,
              "visConfig": {
                "opacity": 0.8,
                "strokeOpacity": 0.8,
                "thickness": 0.5,
                "strokeColor": None,
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
                "radius": 30,
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
                "stroked": False,
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
              "tempgauge": [
                {
                  "name": "OBJECTID",
                  "format": None
                },
                {
                  "name": "POINTID",
                  "format": None
                },
                {
                  "name": "GRID_CODE",
                  "format": None
                },
                {
                  "name": "Xpr",
                  "format": None
                },
                {
                  "name": "Ypr",
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
        "latitude": 25.43801219586105,
        "longitude": 118.07592504530639,
        "pitch": 50.27522937918078,
        "zoom": 9.994990365520216,
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