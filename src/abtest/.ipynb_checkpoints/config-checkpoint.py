# src/abtest/config.py

INSTALLS_PER_DAY = 20000

purchase_ratio = {"A": 0.0305, "B": 0.0315}
ecpm = {"A": 9.80, "B": 10.80}
impressions = {"A": 2.3, "B": 1.6}
ARPPU = 5

# sale settings
SALE_START = 15
SALE_END = 24

# retention points for original source
retention_points = {
    "A": {0: 1.00, 1: 0.53, 3: 0.27, 7: 0.17, 14: 0.06},
    "B": {0: 1.00, 1: 0.48, 3: 0.25, 7: 0.19, 14: 0.09},
}
