-- store statistics about item placements

create table if not exists extended_stats (
  -- uniq identifier for join with item_locs
  id int unsigned not null auto_increment,
  -- the current version of the randomizer algorithm
  version int unsigned not null,
  -- randomizer parameters
  preset varchar(32),
  area boolean,
  boss boolean,
  majorsSplit varchar(8),
  progSpeed varchar(8),
  morphPlacement varchar(8),
  suitsRestriction boolean,
  progDiff varchar(8),
  superFunMovement boolean,
  superFunCombat boolean,
  superFunSuit boolean,
  -- how many seeds
  count int unsigned default 0,
  primary key(version, preset, area, boss, majorsSplit, progSpeed, morphPlacement, suitsRestriction, progDiff, superFunMovement, superFunCombat, superFunSuit),
  index(id)
);

create table if not exists item_locs (
  -- to join with extend_stats
  ext_id int unsigned not null,
  -- item
  item varchar(16) not null,
  -- locations (count how time the item has been placed at each location)
  EnergyTankGauntlet  smallint unsigned default 0,
  Bomb  smallint unsigned default 0,
  EnergyTankTerminator  smallint unsigned default 0,
  ReserveTankBrinstar  smallint unsigned default 0,
  ChargeBeam  smallint unsigned default 0,
  MorphingBall  smallint unsigned default 0,
  EnergyTankBrinstarCeiling  smallint unsigned default 0,
  EnergyTankEtecoons  smallint unsigned default 0,
  EnergyTankWaterway  smallint unsigned default 0,
  EnergyTankBrinstarGate  smallint unsigned default 0,
  XRayScope  smallint unsigned default 0,
  Spazer  smallint unsigned default 0,
  EnergyTankKraid  smallint unsigned default 0,
  Kraid  smallint unsigned default 0,
  VariaSuit  smallint unsigned default 0,
  IceBeam  smallint unsigned default 0,
  EnergyTankCrocomire  smallint unsigned default 0,
  HiJumpBoots  smallint unsigned default 0,
  GrappleBeam  smallint unsigned default 0,
  ReserveTankNorfair  smallint unsigned default 0,
  SpeedBooster  smallint unsigned default 0,
  WaveBeam  smallint unsigned default 0,
  Ridley  smallint unsigned default 0,
  EnergyTankRidley  smallint unsigned default 0,
  ScrewAttack  smallint unsigned default 0,
  EnergyTankFirefleas  smallint unsigned default 0,
  ReserveTankWreckedShip  smallint unsigned default 0,
  EnergyTankWreckedShip  smallint unsigned default 0,
  Phantoon  smallint unsigned default 0,
  RightSuperWreckedShip  smallint unsigned default 0,
  GravitySuit  smallint unsigned default 0,
  EnergyTankMamaturtle  smallint unsigned default 0,
  PlasmaBeam  smallint unsigned default 0,
  ReserveTankMaridia  smallint unsigned default 0,
  SpringBall  smallint unsigned default 0,
  EnergyTankBotwoon  smallint unsigned default 0,
  Draygon  smallint unsigned default 0,
  SpaceJump  smallint unsigned default 0,
  MotherBrain  smallint unsigned default 0,
  PowerBombCrateriasurface  smallint unsigned default 0,
  MissileoutsideWreckedShipbottom  smallint unsigned default 0,
  MissileoutsideWreckedShiptop  smallint unsigned default 0,
  MissileoutsideWreckedShipmiddle  smallint unsigned default 0,
  MissileCrateriamoat  smallint unsigned default 0,
  MissileCrateriabottom  smallint unsigned default 0,
  MissileCrateriagauntletright  smallint unsigned default 0,
  MissileCrateriagauntletleft  smallint unsigned default 0,
  SuperMissileCrateria  smallint unsigned default 0,
  MissileCrateriamiddle  smallint unsigned default 0,
  PowerBombgreenBrinstarbottom  smallint unsigned default 0,
  SuperMissilepinkBrinstar  smallint unsigned default 0,
  MissilegreenBrinstarbelowsupermissile  smallint unsigned default 0,
  SuperMissilegreenBrinstartop  smallint unsigned default 0,
  MissilegreenBrinstarbehindmissile  smallint unsigned default 0,
  MissilegreenBrinstarbehindreservetank  smallint unsigned default 0,
  MissilepinkBrinstartop  smallint unsigned default 0,
  MissilepinkBrinstarbottom  smallint unsigned default 0,
  PowerBombpinkBrinstar  smallint unsigned default 0,
  MissilegreenBrinstarpipe  smallint unsigned default 0,
  PowerBombblueBrinstar  smallint unsigned default 0,
  MissileblueBrinstarmiddle  smallint unsigned default 0,
  SuperMissilegreenBrinstarbottom  smallint unsigned default 0,
  MissileblueBrinstarbottom  smallint unsigned default 0,
  MissileblueBrinstartop  smallint unsigned default 0,
  MissileblueBrinstarbehindmissile  smallint unsigned default 0,
  PowerBombredBrinstarsidehopperroom  smallint unsigned default 0,
  PowerBombredBrinstarspikeroom  smallint unsigned default 0,
  MissileredBrinstarspikeroom  smallint unsigned default 0,
  MissileKraid  smallint unsigned default 0,
  Missilelavaroom  smallint unsigned default 0,
  MissilebelowIceBeam  smallint unsigned default 0,
  MissileaboveCrocomire  smallint unsigned default 0,
  MissileHiJumpBoots  smallint unsigned default 0,
  EnergyTankHiJumpBoots  smallint unsigned default 0,
  PowerBombCrocomire  smallint unsigned default 0,
  MissilebelowCrocomire  smallint unsigned default 0,
  MissileGrappleBeam  smallint unsigned default 0,
  MissileNorfairReserveTank  smallint unsigned default 0,
  MissilebubbleNorfairgreendoor  smallint unsigned default 0,
  MissilebubbleNorfair  smallint unsigned default 0,
  MissileSpeedBooster  smallint unsigned default 0,
  MissileWaveBeam  smallint unsigned default 0,
  MissileGoldTorizo  smallint unsigned default 0,
  SuperMissileGoldTorizo  smallint unsigned default 0,
  MissileMickeyMouseroom  smallint unsigned default 0,
  MissilelowerNorfairabovefireflearoom  smallint unsigned default 0,
  PowerBomblowerNorfairabovefireflearoom  smallint unsigned default 0,
  PowerBombPowerBombsofshame  smallint unsigned default 0,
  MissilelowerNorfairnearWaveBeam  smallint unsigned default 0,
  MissileWreckedShipmiddle  smallint unsigned default 0,
  MissileGravitySuit  smallint unsigned default 0,
  MissileWreckedShiptop  smallint unsigned default 0,
  SuperMissileWreckedShipleft  smallint unsigned default 0,
  MissilegreenMaridiashinespark  smallint unsigned default 0,
  SuperMissilegreenMaridia  smallint unsigned default 0,
  MissilegreenMaridiatatori  smallint unsigned default 0,
  SuperMissileyellowMaridia  smallint unsigned default 0,
  MissileyellowMaridiasupermissile  smallint unsigned default 0,
  MissileyellowMaridiafalsewall  smallint unsigned default 0,
  MissileleftMaridiasandpitroom  smallint unsigned default 0,
  MissilerightMaridiasandpitroom  smallint unsigned default 0,
  PowerBombrightMaridiasandpitroom  smallint unsigned default 0,
  MissilepinkMaridia  smallint unsigned default 0,
  SuperMissilepinkMaridia  smallint unsigned default 0,
  MissileDraygon  smallint unsigned default 0,
  primary key(ext_id, item)
)