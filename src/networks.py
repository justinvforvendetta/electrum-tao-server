# Main network and testnet definitions

params = {
    'bitcoin_main': {
        'pubkey_address': 66, #Tao src/chainparams.cpp L117
        'script_address': 3, #Tao src/chainparams.cpp L118
        'genesis_hash': '0000c1c4b036f822bd91dc2006b5575b9c3617903925b8e738803e094cd23f20' #Tao src/chainparams.cpp L113 
    },
    'bitcoin_test': {
        'pubkey_address': 139, #Tao src/chainparams.cpp L137
        'script_address': 19, #Tao src/chainparams.cpp L138
        'genesis_hash': '00000bafbc94add76cb75e2ec92894837288a481e5c005f6563d91623bf8bc2c' #Tao src/chainparams.cpp L129
    }
}