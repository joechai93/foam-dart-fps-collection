from enum import StrEnum

class DartType(StrEnum):
    WORKER_GEN3_PLUS_HE_1_0_G_STEFAN = "Worker Gen3+ HE 1.0g (Stefan)"
    WORKER_BAMBOO_1_0_G = "Worker Bamboo 1.0g (Stefan)"
    DART_ZONE_NITROSHOT_PLUS_0_98_G = "Dart Zone Nitroshot Plus 0.98g"
    ADVENTURE_FORCE_EMBER_1_0_G = "Adventure Force Ember 1.0g"

class Platform(StrEnum):
    NERF_RETALIATOR_MODDED = "Nerf Retaliator (Modded to take Stefan darts)"
    WORKER_SEAGULL_MODDED = "Worker Seagull"
    ORION_LYNX = "Orion Lynx"
    GFZ_SBL_2_0 = "GFZ SBL 2.0"

class Spring(StrEnum):
    ELITE_9_KG = "Elite 9kg"

class BarrelLength(StrEnum):
    MM_150 = "150mm"
    MM_210 = "210mm"

class BCAR(StrEnum):
    NONE = "None"
    WORKER_SCAR_16MM_TUBE = "Worker SCAR 16mm Rifled Tube"
    WORKER_BCAR_8DEG_BASE = "Worker BCAR 8° Base"
    WORKER_BCAR_8DEG_1EXT = "Worker BCAR 8° 1 Extension"
    WORKER_BCAR_8DEG_2EXT = "Worker BCAR 8° 2 Extensions"
    GFZ_BCAR_3ROW_8DEG = "GFZ BCAR 3 Row 8°"
    GFZ_BCAR_NEO_5ROW_7DEG = "GFZ BCAR Neo 5 Row 7°"