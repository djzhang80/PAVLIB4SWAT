config={
  "version": "v1",
  "config": {
    "visState": {
      "filters": [
        {
          "dataId": [
            "ts_raingauges_id"
          ],
          "id": "8to4iayc",
          "name": [
            "date1"
          ],
          "type": "timeRange",
          "value": [
            1059197897000,
            1063426376000
          ],
          "enlarged": True,
          "plotType": "lineChart",
          "animationWindow": "free",
          "yAxis": {
            "name": "value",
            "type": "integer"
          }
        }
      ],
      "layers": [
        {
          "id": "dixoby",
          "type": "point",
          "config": {
            "dataId": "ts_raingauges_id",
            "label": "Point",
            "color": [
              221,
              178,
              124
            ],
            "columns": {
              "lat": "lat",
              "lng": "lon",
              "altitude": None
            },
            "isVisible": True,
            "visConfig": {
              "radius": 10,
              "fixedRadius": False,
              "opacity": 0.8,
              "outline": False,
              "thickness": 2,
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
              "radiusRange": [
                0,
                50
              ],
              "filled": True
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
            "colorField": {
              "name": "value",
              "type": "integer"
            },
            "colorScale": "quantile",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "sizeField": {
              "name": "value",
              "type": "integer"
            },
            "sizeScale": "sqrt"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "ts_raingauges_id": [
              {
                "name": "Unnamed: 0",
                "format": None
              },
              {
                "name": "ele",
                "format": None
              },
              {
                "name": "date1",
                "format": None
              },
              {
                "name": "value",
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
      "bearing": 0,
      "dragRotate": False,
      "latitude": 24.966903828895365,
      "longitude": 118.00336512196948,
      "pitch": 0,
      "zoom": 8.231154587267676,
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