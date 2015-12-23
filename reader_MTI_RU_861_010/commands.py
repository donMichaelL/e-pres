# Commands
# Inverse Logic
# 4 Bytes --> HEADER --> Command from MTI (CITM) --> 0x43, 0x49, 0x54, 0x4d
# 1 Byte --> READER ID --> Broadcast --> 0xff
# 1 Byte --> COMMANDID --> Cancel Operation --> 0x50
# 8 Bytes --> COMMAND PARAMETERS --> 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
# 2 Bytes --> CHECKSUM


#--------------------------------------------- BEFORE INVENTORY ---------------------------------------------------

# 0x50 --> Cancel Operation
cancel_operation = [0x43, 0x49, 0x54, 0x4d, 0xff, 0x50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xd2, 0x0d ]
# 0x67 --> Read Mac in 5 Messages
# read the first part 0x5f
read_mac_first   = [0x43, 0x49, 0x54, 0x4d, 0xff, 0x67, 0x5f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xdd, 0x5a ]
# read the second part 0x60
read_mac_second  = [0x43, 0x49, 0x54, 0x4d, 0xff, 0x67, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xc3, 0xc5 ]
# read the third part 0x61
read_mac_third   = [0x43, 0x49, 0x54, 0x4d, 0xff, 0x67, 0x61, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x82 ]
# read the fourth part 0x62
read_mac_fourth  = [0x43, 0x49, 0x54, 0x4d, 0xff, 0x67, 0x62, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x65, 0x4a ]
# read the fifth part 0x63
read_mac_fifth   = [0x43, 0x49, 0x54, 0x4d, 0xff, 0x67, 0x63, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xb6, 0x0d ]
read_mac = [read_mac_first, read_mac_second, read_mac_third, read_mac_fourth, read_mac_fifth ]

# 0x60 --> Retrieving the MAC Firmware Version Information
get_firmware     = [0x43, 0x49, 0x54, 0x4d, 0xff, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xd0, 0xf9 ]

# 0x6c --> Retrieving the MAC-Resident OEMCfg Version Information
get_version     = [0x43, 0x49, 0x54, 0x4d, 0xff, 0x6c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xc0, 0x4c ]

# 0x6d --> Retrieving the MAC-Resident OEMCfg Update Number Information
get_upd_num     = [0x43, 0x49, 0x54, 0x4d, 0xff, 0x6d, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xe3, 0xa7 ]

# 0x64 -->Retrieving the Boot-loader Firmware Version Information
get_upd_num     = [0x43, 0x49, 0x54, 0x4d, 0xff, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3f, 0x65 ]

# 0x07 --> Retrieving Low-Level MAC Registers
mac_registers   = [0x43, 0x49, 0x54, 0x4d, 0xff, 0x07, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x3f ]
#--------------------------------------------- BEFORE INVENTORY ---------------------------------------------------

#---------------------------------------------  INVENTORY ONCE ---------------------------------------------------

# 0x02 --> Setting the Operation Mode (0:Continious or 1:non-Continuous)
set_mode        = [0x43, 0x49, 0x54, 0x4d, 0xff, 0x02, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x41, 0x80 ]

# 0x40 --> Tag Inventory Operation
tag_inventory   = [0x43, 0x49, 0x54, 0x4d, 0xff, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2c, 0x5e ]
