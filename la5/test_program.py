if __name__ == "__main__":
    print("Contains variables test_a and test_b. Import them manually.")

test_a = ['calc', ['set', 'x', 1], ['set', 'i', 1], ['while', ['i','<',11], ['set', 'x', ['x', '*', 'i']], ['set', 'i', ['i', '+', 1]], ['print', 'x'] ] ]
#test_ a = ['calc', 
#               ['set', 'x', 3], 
#               ['set', 'i', 1], 
#               ['while', ['i','<',11], 
#                   ['set', 'x', ['x', '*', 'i'] , 
#                   ['set', 'i', ['i', '+', 1]
#               ]
#               ['if', ['ans', '=', 368800], 
#                   ['print', 'ans]
#                   ['print', 'i']
#               ]
#           ]



test_b = ['calc', ['read', 'n'], ['set', 'ans', 1], ['set', 'i', 1], ['while', ['i', '<', ['n','+', 1]], ['set', 'ans', ['ans', '*', 'i'] ], ['set', 'i', ['i', '+', 1]] ], ['if', ['ans', '=', 3628800], [['print', 'ans'],['print', 'ans']], ['print', 'i']] ]
# Fackultet av insatt heltal
# test_b = ['calc', 
#               ['read', 'n'], 
#               ['set', 'ans', 1], 
#               ['set', 'i', 1], 
#               ['while', ['i', '<', ['n','+', 1] ], 
#                   ['set', 'ans', ['ans', '*', 'i'] ], 
#                   ['set', 'i', ['i', '+', 1] ]
#               ]
#           ] 
