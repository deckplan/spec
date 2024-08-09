---
title: Substrait Python 0.13 supports textual formats
description: Support for loading text representation and json representation has been released in Substrait-Python 0.13
date: 2024-02-20
---

# Substrait Python and plan formats

Up to now the Substrait-Python library was a only able to represent in memory a Substrait plan
and emit or load it from a protobuf binary representation.

In version 0.13 it was finally introduced the support to load it from more human readable formats
like the Text Format and the JSON Format. 
The Text Format allows to more easily load plans manually built by humans and provides an effective way
to debug plans, while the JSON format acts as a bridge between the human and the machine, 
providing a format that can be easily manipulated in all major programming languages, 
shipped via text based protocols like HTTP while also being fairly readable for a human.

## Using the Text Format

``` py
import tempfile
from substrait.planloader import planloader

with tempfile.NamedTemporaryFile(mode="rw+t) as tf:
    tf.write("""

    """)
    testplan = planloader.load_substrait_plan(tf.name)
```

## Using JSON Format

``` py
# SELECT count(exercise) AS exercise FROM crossfit WHERE difficulty_level <= 5');
plan = {
  "extensions":[
    {
      "extensionFunction":{
        "functionAnchor":1,
        "name":"lte"
      }
    },
    {
      "extensionFunction":{
        "functionAnchor":2,
        "name":"is_not_null"
      }
    },
    {
      "extensionFunction":{
        "functionAnchor":3,
        "name":"and"
      }
    },
    {
      "extensionFunction":{
        "functionAnchor":4,
        "name":"count"
      }
    }
  ],
  "relations":[
    {
      "root":{
        "input":{
          "project":{
            "input":{
              "aggregate":{
                "input":{
                  "read":{
                    "baseSchema":{
                      "names":[
                        "exercise",
                        "difficulty_level"
                      ],
                      "struct":{
                        "types":[
                          {
                            "varchar":{
                              "length":13,
                              "nullability":"NULLABILITY_NULLABLE"
                            }
                          },
                          {
                            "i32":{
                              "nullability":"NULLABILITY_NULLABLE"
                            }
                          }
                        ],
                        "nullability":"NULLABILITY_REQUIRED"
                      }
                    },
                    "filter":{
                      "scalarFunction":{
                        "functionReference":3,
                        "outputType":{
                          "bool":{
                            "nullability":"NULLABILITY_NULLABLE"
                          }
                        },
                        "arguments":[
                          {
                            "value":{
                              "scalarFunction":{
                                "functionReference":1,
                                "outputType":{
                                  "i32":{
                                    "nullability":"NULLABILITY_NULLABLE"
                                  }
                                },
                                "arguments":[
                                  {
                                    "value":{
                                      "selection":{
                                        "directReference":{
                                          "structField":{
                                            "field":1
                                          }
                                        },
                                        "rootReference":{
                                          
                                        }
                                      }
                                    }
                                  },
                                  {
                                    "value":{
                                      "literal":{
                                        "i32":5
                                      }
                                    }
                                  }
                                ]
                              }
                            }
                          },
                          {
                            "value":{
                              "scalarFunction":{
                                "functionReference":2,
                                "outputType":{
                                  "i32":{
                                    "nullability":"NULLABILITY_NULLABLE"
                                  }
                                },
                                "arguments":[
                                  {
                                    "value":{
                                      "selection":{
                                        "directReference":{
                                          "structField":{
                                            "field":1
                                          }
                                        },
                                        "rootReference":{
                                          
                                        }
                                      }
                                    }
                                  }
                                ]
                              }
                            }
                          }
                        ]
                      }
                    },
                    "projection":{
                      "select":{
                        "structItems":[
                          {
                            
                          }
                        ]
                      },
                      "maintainSingularStruct":true
                    },
                    "namedTable":{
                      "names":[
                        "crossfit"
                      ]
                    }
                  }
                },
                "groupings":[
                  {
                    
                  }
                ],
                "measures":[
                  {
                    "measure":{
                      "functionReference":4,
                      "outputType":{
                        "i64":{
                          "nullability":"NULLABILITY_NULLABLE"
                        }
                      }
                    }
                  }
                ]
              }
            },
            "expressions":[
              {
                "selection":{
                  "directReference":{
                    "structField":{
                      
                    }
                  },
                  "rootReference":{
                    
                  }
                }
              }
            ]
          }
        },
        "names":[
          "exercise"
        ]
      }
    }
  ],
  "version":{
    "minorNumber":24,
  }
}
```