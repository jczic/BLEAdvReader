## A BLE tool library to decode some advertising data in object mode (used on ESP32 and [Pycom](http://www.pycom.io) modules)

![HC²](hc2.png "HC²")

#### Very easy to integrate and very light with one file only :
- `"bleAdvReader.py"`

#### BLEAdvReader features :
- Access to all elements data in BLE advertising packets
- Checking data format errors in lenght and structure
- Getting objects (class) to read some specialized data
- Works on data at different levels
- Reading UUIDs in the good format (16bits, 32bits, 128bits)
- Access to manufacturer data for custom ID of companies
- Decoding and reading **Apple iBeacon** format
- Decoding and reading **Google EddyStone** format :
  - EddyStone UID
  - EddyStone URL *(Beacon URI)*
  - EddyStone TML Unencrypted
  - EddyStone TML Encrypted
  - EddyStone EID
- Estimating device proximity with 3 equations :
  - LogTX (path loss exponent variable)
  - OldBconTX (on old iPhone/Android)
  - NewBconTX (on recent iPhone/Android)

### Example of using *BLEAdvReader* easily :
```python
# Getting "advertisingData" before via the BLE

from bleAdvReader import BLEAdvReader

advReader = BLEAdvReader(advertisingData)

# Gets the service data part in the advertising packet,
svcData = advReader.GetDataByDataType(BLEAdvReader.DATA_TYPE_SVC_DATA)

# List all decoded and structured objects (class),
for advElement in advReader.GetAllElements() :
    print(advElement)
    # Finds an iBeacon with classes instances comparison,
    if isinstance(advElement, BLEAdvReader.AppleIBeacon) :
    	print('This is an iBeacon with UUID %s' % advElement.StrUUID)

# Gets the same iBeacon more directly,
iBeaconElement = advReader.GetElementByClass(BLEAdvReader.AppleIBeacon)
if iBeaconElement :
	print('iBeacon found!')
```

### Using *BLEAdvReader* main class :

| Name | Function |
| - | - |
| Constructor | `advReader = BLEAdvReader(advertisingData)` |
| GetDataByDataType | `data = advReader.GetDataByDataType(dataType)` |
| GetAllElements | `advElements = advReader.GetAllElements()` |
| GetElementByClass | `advElement = advReader.GetElementByClass(elementType)` |

| Element type (class) |
| - |
| BLEAdvReader.Flags |
| BLEAdvReader.AdoptedService16bits |
| BLEAdvReader.AdoptedService32bits |
| BLEAdvReader.AdoptedService128bits |
| BLEAdvReader.ShortName |
| BLEAdvReader.CompleteName |
| BLEAdvReader.TXPowerLevel |
| BLEAdvReader.ServiceData |
| BLEAdvReader.ManufacturerData |
| BLEAdvReader.AppleService |
| BLEAdvReader.AppleIBeacon |
| BLEAdvReader.EddyStoneUID |
| BLEAdvReader.EddyStoneURL |
| BLEAdvReader.EddyStoneTLMUnencrypted |
| BLEAdvReader.EddyStoneTLMEncrypted |
| BLEAdvReader.EddyStoneEID |

| Data type |
| - |
| BLEAdvReader.DATA_TYPE_FLAGS |
| BLEAdvReader.DATA_TYPE_INCOMP_16BITS_UUIDS |
| BLEAdvReader.DATA_TYPE_COMP_16BITS_UUIDS |
| BLEAdvReader.DATA_TYPE_INCOMP_32BITS_UUIDS |
| BLEAdvReader.DATA_TYPE_COMP_32BITS_UUIDS |
| BLEAdvReader.DATA_TYPE_INCOMP_128BITS_UUIDS |
| BLEAdvReader.DATA_TYPE_COMP_128BITS_UUIDS |
| BLEAdvReader.DATA_TYPE_SHORT_NAME |
| BLEAdvReader.DATA_TYPE_COMPLETE_NAME |
| BLEAdvReader.DATA_TYPE_TX_POWER_LEVEL |
| BLEAdvReader.DATA_TYPE_DEVICE_CLASS |
| BLEAdvReader.DATA_TYPE_SMP_PAIR_HASH_C |
| BLEAdvReader.DATA_TYPE_SMP_PAIR_HASH_C192 |
| BLEAdvReader.DATA_TYPE_SMP_PAIR_RAND_R |
| BLEAdvReader.DATA_TYPE_SMP_PAIR_RAND_R192 |
| BLEAdvReader.DATA_TYPE_DEVICE_ID |
| BLEAdvReader.DATA_TYPE_SECU_MNGR_TK_VAL |
| BLEAdvReader.DATA_TYPE_SECU_MNGR_OOB_FLAGS |
| BLEAdvReader.DATA_TYPE_SLAVE_CONN_INT_RNG |
| BLEAdvReader.DATA_TYPE_16BITS_SVC_SOL_UUIDS |
| BLEAdvReader.DATA_TYPE_128BITS_SVC_SOL_UUIDS |
| BLEAdvReader.DATA_TYPE_SVC_DATA |
| BLEAdvReader.DATA_TYPE_SVC_DATA_16BITS_UUID |
| BLEAdvReader.DATA_TYPE_PUB_TARGET_ADDR |
| BLEAdvReader.DATA_TYPE_RAND_TARGET_ADDR |
| BLEAdvReader.DATA_TYPE_APPEARANCE |
| BLEAdvReader.DATA_TYPE_ADV_INT |
| BLEAdvReader.DATA_TYPE_LE_BLT_DEVICE_ADDR |
| BLEAdvReader.DATA_TYPE_LE_ROLE |
| BLEAdvReader.DATA_TYPE_SMP_PAIR_HASH_C256 |
| BLEAdvReader.DATA_TYPE_SMP_PAIR_RAND_R256 |
| BLEAdvReader.DATA_TYPE_32BITS_SVC_SOL_UUIDS |
| BLEAdvReader.DATA_TYPE_SVC_DATA_32BITS_UUID |
| BLEAdvReader.DATA_TYPE_SVC_DATA_128BITS_UUID |
| BLEAdvReader.DATA_TYPE_LE_SECU_CONN_RAND_VAL |
| BLEAdvReader.DATA_TYPE_URI |
| BLEAdvReader.DATA_TYPE_INDOOR_POS |
| BLEAdvReader.DATA_TYPE_TRANS_DISCOV_DATA |
| BLEAdvReader.DATA_TYPE_LE_SUPPORT_FEAT |
| BLEAdvReader.DATA_TYPE_CHAN_MAP_UPD_INDIC |
| BLEAdvReader.DATA_TYPE_PB_ADV |
| BLEAdvReader.DATA_TYPE_MESH_MSG |
| BLEAdvReader.DATA_TYPE_MESH_BEACON |
| BLEAdvReader.DATA_TYPE_3D_INFO_DATA |
| BLEAdvReader.DATA_TYPE_MANUFACTURER_DATA |

### Using *BLEAdvReader.Flags* class :

| Name | Property | Type |
| - | - | - |
| LE_LIMITED_DISC_MODE 		| `flags.LE_LIMITED_DISC_MODE`		| bool |
| LE_GENERAL_DISC_MODE 		| `flags.LE_GENERAL_DISC_MODE`		| bool |
| BR_EDR_NOT_SUPPORTED 		| `flags.BR_EDR_NOT_SUPPORTED`		| bool |
| LE_BR_EDR_CONTROLLER 		| `flags.LE_BR_EDR_CONTROLLER`		| bool |
| LE_BR_EDR_HOST			| `flags.LE_BR_EDR_HOST`			| bool |
| LE_ONLY_LIMITED_DISC_MODE | `flags.LE_ONLY_LIMITED_DISC_MODE`	| bool |
| LE_ONLY_GENERAL_DISC_MODE | `flags.LE_ONLY_GENERAL_DISC_MODE`	| bool |

### Using *BLEAdvReader.AdoptedService16bits* class :

| Name | Property | Type |
| - | - | - |
| UUID    | `adoptedSvc.UUID`    | int |
| StrUUID | `adoptedSvc.StrUUID` | string |

### Using *BLEAdvReader.AdoptedService32bits* class :

| Name | Property | Type |
| - | - | - |
| UUID    | `adoptedSvc.UUID`    | int |
| StrUUID | `adoptedSvc.StrUUID` | string |

### Using *BLEAdvReader.AdoptedService128bits* class :

| Name | Property | Type |
| - | - | - |
| UUID    | `adoptedSvc.UUID`    | bytes |
| StrUUID | `adoptedSvc.StrUUID` | string |

### Using *BLEAdvReader.ShortName* class :
Directly usable as string

### Using *BLEAdvReader.CompleteName* class :
Directly usable as string

### Using *BLEAdvReader.TXPowerLevel* class :

| Name | Property | Type |
| - | - | - |
| DBM | `txPower.DBM` | int |

| Name | Function |
| - | - |
| GetProximityByLogTX | `meters = txPowerLvl.GetProximityByLogTX(rssi, n_PathLossExp=2)` |
| GetProximityByOldBconTX | `meters = txPowerLvl.GetProximityByOldBconTX(rssi)` |
| GetProximityByNewBconTX | `meters = txPowerLvl.GetProximityByNewBconTX(rssi)` |

### Using *BLEAdvReader.ServiceData* class :

| Name | Property | Type |
| - | - | - |
| UUID | `svcData.UUID` | int |
| StrUUID | `svcData.StrUUID` | string |
| Data | `svcData.Data` | bytes |

### Using *BLEAdvReader.ManufacturerData* class :

| Name | Property | Type |
| - | - | - |
| CompanyID | `mfacturerData.CompanyID` | int |
| StrCompanyID | `mfacturerData.StrCompanyID` | string |
| Data | `mfacturerData.Data` | bytes |

### Using *BLEAdvReader.AppleService* class :

| Name | Property | Type |
| - | - | - |
| TypeName | `appleSvc.TypeName` | string |
| Data | `appleSvc.Data` | bytes |

| TypeName value |
| - |
| Empty *(unknown type)* |
| `"AirDrop"` |
| `"AirPods"` |
| `"AirPlay Destination"` |
| `"AirPlay Source"` |
| `"HandOff"` |
| `"Nearby"` |

### Using *BLEAdvReader.AppleIBeacon* class :

| Name | Property | Type |
| - | - | - |
| UUID | `iBeacon.UUID` | bytes |
| StrUUID | `iBeacon.StrUUID` | string |
| Major | `iBeacon.Major` | int |
| Minor | `iBeacon.Minor` | int |
| TxPower | `iBeacon.TxPower` | int |

| Name | Function |
| - | - |
| GetProximityByLogTX | `meters = iBeacon.GetProximityByLogTX(rssi, n_PathLossExp=2)` |
| GetProximityByOldBconTX | `meters = iBeacon.GetProximityByOldBconTX(rssi)` |
| GetProximityByNewBconTX | `meters = iBeacon.GetProximityByNewBconTX(rssi)` |

### Using *BLEAdvReader.EddyStoneUID* class :

| Name | Property | Type |
| - | - | - |
| TxPower | `beaconEddyStone.TxPower` | int |
| Namespace | `beaconEddyStone.Namespace` | bytes |
| Instance | `beaconEddyStone.Instance` | bytes |

| Name | Function |
| - | - |
| GetProximityByLogTX | `meters = beaconEddyStone.GetProximityByLogTX(rssi, n_PathLossExp=2)` |
| GetProximityByOldBconTX | `meters = beaconEddyStone.GetProximityByOldBconTX(rssi)` |
| GetProximityByNewBconTX | `meters = beaconEddyStone.GetProximityByNewBconTX(rssi)` |

### Using *BLEAdvReader.EddyStoneURL* class :

| Name | Property | Type |
| - | - | - |
| TxPower | `beaconEddyStone.TxPower` | int |
| URL | `beaconEddyStone.URL` | string |

| Name | Function |
| - | - |
| GetProximityByLogTX | `meters = beaconEddyStone.GetProximityByLogTX(rssi, n_PathLossExp=2)` |
| GetProximityByOldBconTX | `meters = beaconEddyStone.GetProximityByOldBconTX(rssi)` |
| GetProximityByNewBconTX | `meters = beaconEddyStone.GetProximityByNewBconTX(rssi)` |

### Using *BLEAdvReader.EddyStoneTLMUnencrypted* class :

| Name | Property | Type |
| - | - | - |
| VBatt | `beaconEddyStone.VBatt` | int |
| Temp | `beaconEddyStone.Temp` | int |
| AdvCnt | `beaconEddyStone.AdvCnt` | int |
| SecCnt | `beaconEddyStone.SecCnt` | int |

### Using *BLEAdvReader.EddyStoneTLMEncrypted* class :

| Name | Property | Type |
| - | - | - |
| ETLM | `beaconEddyStone.ETLM` | bytes |
| SALT | `beaconEddyStone.SALT` | int |
| MIC | `beaconEddyStone.MIC` | int |

### Using *BLEAdvReader.EddyStoneEID* class :

| Name | Property | Type |
| - | - | - |
| TxPower | `beaconEddyStone.TxPower` | int |
| EncryptedID | `beaconEddyStone.EncryptedID` | bytes |

| Name | Function |
| - | - |
| GetProximityByLogTX | `meters = beaconEddyStone.GetProximityByLogTX(rssi, n_PathLossExp=2)` |
| GetProximityByOldBconTX | `meters = beaconEddyStone.GetProximityByOldBconTX(rssi)` |
| GetProximityByNewBconTX | `meters = beaconEddyStone.GetProximityByNewBconTX(rssi)` |

### Using *BLEAdvReader.ProximityHelper* "static" class :

| Name | Function |
| - | - |
| LogTX | `meters = BLEAdvReader.ProximityHelper.LogTX(rssi, rssiTX, n_PathLossExp=2)` |
| OldBconTX | `meters = BLEAdvReader.ProximityHelper.OldBconTX(rssi, rssiTX)` |
| NewBconTX | `meters = BLEAdvReader.ProximityHelper.NewBconTX(rssi, rssiTX)` |



### By JC`zic for [HC²](https://www.hc2.fr) ;')

*Keep it simple, stupid* :+1:
