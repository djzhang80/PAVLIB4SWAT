config={
  "version": "v1",
  "config": {
    "visState": {
      "filters": [
        {
          "dataId": [
            "ts_subbasins_id"
          ],
          "id": "2fxkhlfrj",
          "name": [
            "date"
          ],
          "type": "timeRange",
          "value": [
            1203258240000,
            1203273065000
          ],
          "enlarged": True,
          "plotType": "lineChart",
          "animationWindow": "free",
          "yAxis": {
            "name": "PETmm",
            "type": "real"
          }
        }
      ],
      "layers": [
        {
          "id": "nvwlru4",
          "type": "geojson",
          "config": {
            "dataId": "ts_subbasins_id",
            "label": "ts_subbasins_id",
            "color": [
              18,
              147,
              154
            ],
            "columns": {
              "geojson": "_geojson"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "strokeOpacity": 0.8,
              "thickness": 0.5,
              "strokeColor": [
                221,
                178,
                124
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
            "colorField": {
              "name": "PETmm",
              "type": "real"
            },
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
            "ts_subbasins_id": [
              {
                "name": "sub_no",
                "format": None
              },
              {
                "name": "date",
                "format": None
              },
              {
                "name": "PRECIPmm",
                "format": None
              },
              {
                "name": "SNOMELTmm",
                "format": None
              },
              {
                "name": "PETmm",
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
      "latitude": 25.37329132802265,
      "longitude": 117.98204929174187,
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