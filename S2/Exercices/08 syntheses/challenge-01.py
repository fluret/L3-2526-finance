from random import choice, randrange

""" dict_machines = [
    {"Index": i, "Cost": randrange(4000), "InService": bool(choice([True, False]))}
    for i in range(20)
]
print(dict_machines) """

dict_machines = [
    {"Index": 0, "Cost": 790, "InService": True},
    {"Index": 1, "Cost": 3150, "InService": True},
    {"Index": 2, "Cost": 3596, "InService": True},
    {"Index": 3, "Cost": 2254, "InService": False},
    {"Index": 4, "Cost": 1256, "InService": True},
    {"Index": 5, "Cost": 3201, "InService": False},
    {"Index": 6, "Cost": 392, "InService": False},
    {"Index": 7, "Cost": 1113, "InService": False},
    {"Index": 8, "Cost": 1920, "InService": False},
    {"Index": 9, "Cost": 3973, "InService": True},
    {"Index": 10, "Cost": 353, "InService": False},
    {"Index": 11, "Cost": 2279, "InService": False},
    {"Index": 12, "Cost": 2183, "InService": True},
    {"Index": 13, "Cost": 1812, "InService": True},
    {"Index": 14, "Cost": 442, "InService": True},
    {"Index": 15, "Cost": 410, "InService": False},
    {"Index": 16, "Cost": 6, "InService": False},
    {"Index": 17, "Cost": 3421, "InService": True},
    {"Index": 18, "Cost": 3238, "InService": False},
    {"Index": 19, "Cost": 1754, "InService": True},
]

print(
    [
        {
            "Index": machine["Index"],
            "InBudget": "Yes" if machine["Cost"] < 1000 else "No",
            "ValidService": machine["InService"] and machine["Index"] % 2 == 0,
        }
        for machine in dict_machines
        if machine["Index"] in [1, 2, 7, 8, 11, 14, 19]
    ]
)
