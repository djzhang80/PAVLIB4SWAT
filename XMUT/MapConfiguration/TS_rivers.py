config = {
    "version": "v1",
    "config": {
        "visState": {
            "filters": [
              {
                  "dataId": [
                      "ts_rivers"
                  ],
                  "id": "e2v0aocqj",
                  "name": [
                      "date"
                  ],
                  "type": "timeRange",
                  "value": [
                      1199312907000,
                      1199349968000
                  ],
                  "enlarged": True,
                  "plotType": "lineChart",
                  "animationWindow": "free",
                  "yAxis": {
                      "name": "discharge",
                      "type": "real"
                  }
              }
            ],
            "layers": [
                {
                    "id": "3372ygbf",
                    "type": "geojson",
                    "config": {
                        "dataId": "ts_rivers",
                        "label": "ts_rivers",
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
                            "thickness": 4.1,
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
                                "name": "Custom Palette",
                                "type": "custom",
                                "category": "Custom",
                                "colors": [
                                    "#6dbdc3",
                                    "#4BA7AF",
                                    "#00939C",
                                    "#018a92",
                                    "#005d62"
                                ]
                            },
                            "radius": 10,
                            "sizeRange": [
                                0,
                                2
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
                        "sizeField": {
                            "name": "discharge",
                            "type": "real"
                        },
                        "sizeScale": "sqrt",
                        "strokeColorField": {
                            "name": "discharge",
                            "type": "real"
                        },
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
                        "ts_rivers": [
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
            "latitude": 25.35280270561556,
            "longitude": 117.98631566175419,
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
