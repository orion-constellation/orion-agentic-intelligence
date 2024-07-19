ALERT_LEVEL = {0: "Low",
          1: "Medium",
          2: "High"}

# Weights can be updated based on a model that we will refine with time but at first perhaps 
# we are manually
SOURCE_TYPES = {{"name": "RULE"
                 "weight": 1.0},
                 {"name": "SIEM",
                 "weight": 0.7}, 
                 {"name": "THREAT_FEED", 
                "weight": 0.5}, 
                {"name":"INTEL_SVC",
                 "weight":"0.9"
                 #Heuristics may become rules...
                 ["name:":"HEURISTIC", 
                  "weight":0.4]
          }}