from math import ceil

from logic.smbool import SMBool
from logic.helpers import Helpers, Bosses
from logic.cache import Cache
from logic.logic import Logic
from rom.rom_patches import RomPatches
from graph.graph_utils import getAccessPoint

class HelpersGraph(Helpers):
    def __init__(self, smbm):
        self.smbm = smbm

#    def canEnterAndLeaveGauntletQty(self, nPB, nTanksSpark):
#        sm = self.smbm
#        # EXPLAINED: to access Gauntlet Entrance from Landing site we can either:
#        #             -fly to it (infinite bomb jumps or space jump)
#        #             -shinespark to it
#        #             -wall jump with high jump boots
#        #             -wall jump without high jump boots
#        #            then inside it to break the bomb wals:
#        #             -use screw attack (easy way)
#        #             -use power bombs
#        #             -use bombs
#        #             -perform a simple short charge on the way in
#        #              and use power bombs on the way out
#        return sm.wand(sm.wor(sm.canFly(),
#                              sm.haveItem('SpeedBooster'),
#                              sm.wand(sm.knowsHiJumpGauntletAccess(),
#                                      sm.haveItem('HiJump')),
#                              sm.knowsHiJumpLessGauntletAccess()),
#                       sm.wor(sm.haveItem('ScrewAttack'),
#                              sm.wor(sm.wand(sm.energyReserveCountOkHardRoom('Gauntlet'),
#                                             sm.wand(sm.canUsePowerBombs(),
#                                                     sm.wor(sm.itemCountOk('PowerBomb', nPB),
#                                                            sm.wand(sm.haveItem('SpeedBooster'),
#                                                                    sm.energyReserveCountOk(nTanksSpark))))),
#                                     sm.wand(sm.energyReserveCountOkHardRoom('Gauntlet', 0.51),
#                                             sm.canUseBombs()))))
#
#    @Cache.decorator
#    def canEnterAndLeaveGauntlet(self):
#        sm = self.smbm
#        return sm.wor(sm.wand(sm.canShortCharge(),
#                              sm.canEnterAndLeaveGauntletQty(2, 2)),
#                      sm.canEnterAndLeaveGauntletQty(2, 3))

    @Cache.decorator
    def canPassCrateriaGreenPirates(self):
        sm = self.smbm
        return sm.wor(sm.canPassBombPassages(), # pirates can be killed with bombs or power bombs
                      sm.haveMissileOrSuper(),
                      sm.energyReserveCountOk(1),
                      sm.wor(sm.haveItem('Charge'),
                             sm.haveItem('Ice'),
                             sm.haveItem('Wave'),
                             sm.haveItem('Spazer'),
                             sm.haveItem('Plasma'),
                             sm.haveItem('ScrewAttack')))

    # from blue brin elevator
    @Cache.decorator
    def canAccessBillyMays(self):
        sm = self.smbm
        return sm.wand(sm.wor(RomPatches.has(RomPatches.BlueBrinstarBlueDoor),
                              sm.traverse('ConstructionZoneRight')),
                       sm.canUsePowerBombs(),
                       sm.canGravLessLevel1())

    @Cache.decorator
    def canPassMoatReverse(self):
        sm = self.smbm
        return sm.wand(sm.haveItem('Gravity'),
                       # TODO::try with a spring ball jump
                       sm.wor(sm.canFly(),
                              sm.haveItem('HiJump'),
                              sm.canShortCharge()))

    @Cache.decorator
    def canAccessEtecoons(self):
        sm = self.smbm
        return sm.wand(sm.canUsePowerBombs(),
                       # beetoms
                       sm.wor(sm.haveMissileOrSuper(),
                              sm.canUsePowerBombs(),
                              sm.haveItem('ScrewAttack')))

    # the water zone east of WS
    @Cache.decorator
    def canPassForgottenHighway(self):
        sm = self.smbm
        return wm.wand(sm.canMorphJump(),
                       sm.wor(sm.haveItem('Gravity'),
                              sm.wand(sm.knowsGravLessLevel1(),
                                      sm.haveItem('HiJump'))))
    @Cache.decorator
    def canTraverseSandPitsBottom(self):
        sm = self.smbm
        # quite horrible to do... even with gravity...
        return sm.wand(sm.haveItem('Gravity'),
                       # eigher freeze top evir to jump on it, or use speedbooster to jump higher
                       # or use spacejump
                       sm.wor(sm.wand(sm.wor(sm.haveItem('Ice'), sm.haveItem('SpeedBooster')),
                                      sm.haveItem('HiJump')),
                              sm.haveItem('SpaceJump')))

    @Cache.decorator
    def canTraverseSandPitsTop(self):
        sm = self.smbm
        # quite horrible to do...
        return sm.wand(sm.haveItem('Gravity'),
                       sm.wor(sm.haveItem('HiJump'), sm.haveItem('SpaceJump')))

    @Cache.decorator
    def canBusinessToCathedral(self):
        sm = self.smbm
        return sm.wand(sm.traverse('CathedralEntranceRight'),
                       sm.haveItem('Morph'),
                       sm.canLavaBath(**Logic.Settings.bathsTable['Lava']['Cathedral'],
                                      **Logic.Settings.hellRunsTable['MainUpperNorfair']['Norfair Entrance -> Cathedral Missiles']))

    @Cache.decorator
    def canCathedralToBubble(self):
        sm = self.smbm
        return sm.wand(sm.traverse('CathedralRight'),
                       sm.canLavaBath(**Logic.Settings.bathsTable['Lava']['Cathedral'],
                                      **Logic.Settings.hellRunsTable['MainUpperNorfair']['Norfair Entrance -> Cathedral Missiles']))

    @Cache.decorator
    def canBubbleToCathedral(self):
        sm = self.smbm
        return sm.canLavaBath(**Logic.Settings.bathsTable['Lava']['Cathedral'],
                              **Logic.Settings.hellRunsTable['MainUpperNorfair']['Norfair Entrance -> Cathedral Missiles']))

    @Cache.decorator
    def canCathedralToBusiness(self):
        sm = self.smbm
        return sm.wand(sm.haveItem('Morph'),
                       sm.canLavaBath(**Logic.Settings.bathsTable['Lava']['Cathedral'],
                                      **Logic.Settings.hellRunsTable['MainUpperNorfair']['Norfair Entrance -> Cathedral Missiles']))

    @Cache.decorator
    def canTraverseFrogSpeedway(self):
        sm = self.smbm
        # kill/freeze beetoms, or enough energy.
        return sm.wor(sm.canPassBeetoms(),
                      sm.energyReserveCountOk(2))

    @Cache.decorator
    def canFallToSpeedBooster(self):
        sm = self.smbm
        # 3 etanks
        return sm.canHellRun(**Logic.Settings.hellRunsTable['MainUpperNorfair']['Bubble -> Speed Booster'])

    @Cache.decorator
    def canGetBackFromSpeedBooster(self):
        sm = self.smbm
        # 8 etanks
        return sm.wand(sm.canHellRun(**Logic.Settings.hellRunsTable['MainUpperNorfair']['Speed Booster -> Bubble']),
                       # in bat cave (and also to exit the small tunnel for speed missile)
                       sm.canMorphJump())

    @Cache.decorator
    def canAccessDoubleChamberItems(self):
        sm = self.smbm
        hellRun = Logic.Settings.hellRunsTable['MainUpperNorfair']['Bubble -> Wave']
        return sm.wand(sm.haveItem('Morph'), sm.canHellRun(**hellRun))

    @Cache.decorator
    def canClimbAttic(self):
        # requires hijump or space jump
        sm = self.smbm
        # TODO::check if it's possible with IBJ
        return sm.wor(sm.haveItem('Hijump'), sm.haveItem('SpaceJump'))

    @Cache.decorator
    def canClimbCrocSpeedway(self):
        sm = self.smbm
        # croc speedway, only morph required.
        # the hellrun is way to complicated to do it suitless,
        # with speed it's a easier but still complicated...
        # the speed start is only possible when vanilla croc though
        return sm.wand(sm.haveItem('Morph'),
                       sm.wor(sm.heatProof(),
                              sm.wand(sm.haveItem('SpeedBooster'),
                                      sm.canHellRun(**Logic.Settings.hellRunsTable['Ice']['Croc -> Norfair Entrance']),
                                      sm.isVanillaCroc())))


    @Cache.decorator
    def canClimbGrappleEscape(self):
        sm = self.smbm
                        # something to kill the enemies
        return  sm.wand(sm.wor(sm.haveItem('Missile'), sm.haveItem('Super'), sm.haveItem('PowerBomb'),
                               sm.haveItem('Charge'), sm.haveItem('Ice'), sm.haveItem('Plasma')),
                        sm.canLavaBath(**Logic.Settings.bathsTable['Lava']['Crocomire Escape'],
                                       **Logic.Settings.hellRunsTable['MainUpperNorfair']['Croc -> Norfair Entrance']))

    @Cache.decorator
    def canEnterNorfairReserveAreaFromBubbleMoutain(self):
        sm = self.smbm
        return sm.wand(sm.traverse('BubbleMountainTopLeft'),
                       # it's possible with a delayed wall jump off the grapple blocks but it's hard
                       # TODO::add it as a wall jump technique ?
                       sm.wor(sm.canFly(),
                              sm.haveItem('Ice'),
                              sm.haveItem('HiJump'),
                              # spring ball jump from the right (at the grapple blocks)
                              sm.canSpringBallJump()))

    @Cache.decorator
    def canPassLavaPit(self):
        sm = self.smbm
        # in rotation it's possible to pass it with no items if you're fast enough and you can wall jump
        # on the right fune before it spits a flame, starting your jump from the left fune,
        # we use the knowsLavaDive for it
        return sm.wand(sm.canUsePowerBombs(), # power bomb blocks left and right of LN entrance without any items before
                       sm.wor(sm.knowsLavaDive(),
                              sm.wand(sm.haveItem('Gravity'), sm.haveItem('SpaceJump')),
                              sm.wand(sm.haveItem('Gravity'), sm.knowsGravityJump()),
                              sm.haveItem('HiJump')),
                       sm.canLavaBath(**Logic.Settings.bathsTable['Lava']['Lava Dive Room'],
                                      **Logic.Settings.hellRunsTable['LowerNorfair']['Main']))

    @Cache.decorator
    def canPassLavaPitReverse(self):
        sm = self.smbm
        nTanks = 2
        if sm.heatProof().bool == False:
            nTanks = 6
        return sm.energyReserveCountOk(nTanks)

#    @Cache.decorator
#    def canPassLowerNorfairChozo(self):
#        sm = self.smbm
#        # to require one more CF if no heat protection because of distance to cover, wait times, acid...
#        return sm.wand(sm.canHellRun(**Logic.Settings.hellRunsTable['LowerNorfair']['Entrance -> GT via Chozo']),
#                       sm.canUsePowerBombs(),
#                       sm.wor(RomPatches.has(RomPatches.LNChozoSJCheckDisabled), sm.haveItem('SpaceJump')))
#
#    @Cache.decorator
#    def canExitScrewAttackArea(self):
#        sm = self.smbm
#
#        return sm.wand(sm.canDestroyBombWalls(),
#                       sm.wor(sm.canFly(),
#                              sm.wand(sm.haveItem('HiJump'),
#                                      sm.haveItem('SpeedBooster'),
#                                      sm.wor(sm.wand(sm.haveItem('ScrewAttack'), sm.knowsScrewAttackExit()),
#                                             sm.knowsScrewAttackExitWithoutScrew())),
#                              sm.wand(sm.canUseSpringBall(),
#                                      sm.knowsSpringBallJumpFromWall()),
#                              sm.wand(sm.canSimpleShortCharge(), # fight GT and spark out
#                                      sm.enoughStuffGT())))
#
#    @Cache.decorator
#    def canPassWorstRoom(self):
#        sm = self.smbm
#        return sm.wand(sm.canDestroyBombWalls(),
#                       sm.canPassWorstRoomPirates(),
#                       sm.wor(sm.canFly(),
#                              sm.wand(sm.knowsWorstRoomIceCharge(), sm.haveItem('Ice'), sm.canFireChargedShots()),
#                              sm.wor(sm.wand(sm.knowsGetAroundWallJump(), sm.haveItem('HiJump')),
#                                     sm.knowsWorstRoomWallJump()),
#                              sm.wand(sm.knowsSpringBallJumpFromWall(), sm.canUseSpringBall())))
#
#    # checks mix of super missiles/health
#    def canGoThroughLowerNorfairEnemy(self, nmyHealth, nbNmy, nmyHitDmg, supDmg=300.0):
#        sm = self.smbm
#        # supers only
#        if sm.itemCount('Super')*5*supDmg >= nbNmy*nmyHealth:
#            return SMBool(True, 0, items=['Super'])
#
#        # - or with taking damage as well?
#        (dmgRed, redItems) = sm.getDmgReduction(envDmg=False)
#        dmg = nmyHitDmg / dmgRed
#        if sm.heatProof() and (sm.itemCount('Super')*5*supDmg)/nmyHealth + (sm.energyReserveCount()*100 - 2)/dmg >= nbNmy:
#            # require heat proof as long as taking damage is necessary.
#            # display all the available energy in the solver.
#            return sm.wand(sm.heatProof(), SMBool(True, 0, items=redItems+['Super', '{}-ETank - {}-Reserve'.format(self.smbm.itemCount('ETank'), self.smbm.itemCount('Reserve'))]))
#
#        return sm.knowsDodgeLowerNorfairEnemies()
#
#    def canKillRedKiHunters(self, n):
#        sm = self.smbm
#        destroy = sm.wor(sm.haveItem('Plasma'),
#                         sm.haveItem('ScrewAttack'),
#                         sm.wand(sm.heatProof(), # this takes a loooong time ...
#                                 sm.wor(sm.haveItem('Spazer'),
#                                        sm.haveItem('Ice'),
#                                        sm.wand(sm.haveItem('Charge'),
#                                                sm.haveItem('Wave')))))
#        if destroy.bool == True:
#            return destroy
#        return sm.canGoThroughLowerNorfairEnemy(1800.0, float(n), 200.0)
#
#    @Cache.decorator
#    def canPassThreeMuskateers(self):
#        sm = self.smbm
#        return sm.canKillRedKiHunters(6)
#
#    @Cache.decorator
#    def canPassRedKiHunters(self):
#        sm = self.smbm
#        return sm.canKillRedKiHunters(3)
#
#    @Cache.decorator
#    def canPassWastelandDessgeegas(self):
#        sm = self.smbm
#        destroy = sm.wor(sm.haveItem('Plasma'),
#                         sm.haveItem('ScrewAttack'),
#                         sm.wand(sm.heatProof(), # this takes a loooong time ...
#                                 sm.wor(sm.haveItem('Spazer'),
#                                        sm.wand(sm.haveItem('Charge'),
#                                                sm.haveItem('Wave')))),
#                                        sm.itemCountOk('PowerBomb', 4))
#        if destroy.bool == True:
#            return destroy
#
#        return sm.canGoThroughLowerNorfairEnemy(800.0, 3.0, 160.0)
#
#    @Cache.decorator
#    def canPassNinjaPirates(self):
#        sm = self.smbm
#        return sm.wor(sm.itemCountOk('Missile', 10),
#                      sm.itemCountOk('Super', 2),
#                      sm.haveItem('Plasma'),
#                      sm.wor(sm.haveItem('Spazer'),
#                             sm.wand(sm.haveItem('Charge'),
#                                     sm.wor(sm.haveItem('Wave'),
#                                            sm.haveItem('Ice')))))
#
#    @Cache.decorator
#    def canPassWorstRoomPirates(self):
#        sm = self.smbm
#        return sm.wor(sm.haveItem('ScrewAttack'),
#                      sm.itemCountOk('Missile', 6),
#                      sm.itemCountOk('Super', 3),
#                      sm.wor(sm.wand(sm.canFireChargedShots(), sm.haveItem('Plasma')),
#                             sm.wand(sm.haveItem('Charge'),
#                                     sm.wor(sm.haveItem('Spazer'),
#                                            sm.haveItem('Wave'),
#                                            sm.haveItem('Ice'))),
#                             sm.knowsDodgeLowerNorfairEnemies()))
#
#    # go though the pirates room filled with acid
#    @Cache.decorator
#    def canPassAmphitheaterReverse(self):
#        sm = self.smbm
#        dmgRed = sm.getDmgReduction()[0]
#        nTanksGrav = 4 * 4/dmgRed
#        nTanksNoGrav = 6 * 4/dmgRed
#        return sm.wor(sm.wand(sm.haveItem('Gravity'),
#                              sm.energyReserveCountOk(nTanksGrav)),
#                      sm.wand(sm.energyReserveCountOk(nTanksNoGrav),
#                              sm.knowsLavaDive())) # should be a good enough skill filter for acid wall jumps with no grav...
#
#    @Cache.decorator
#    def canGetBackFromRidleyZone(self):
#        sm = self.smbm
#        return sm.wand(sm.wor(sm.canUseSpringBall(),
#                              sm.canUseBombs(),
#                              sm.haveItem('ScrewAttack'),
#                              sm.wand(sm.canUsePowerBombs(), sm.itemCountOk('PowerBomb', 2)),
#                              sm.wand(sm.haveItem('Morph'), sm.canShortCharge())), # speedball
#                       # in escape you don't have PBs and can't shoot bomb blocks in long tunnels
#                       # in wasteland and ki hunter room
#                       sm.wnot(sm.canUseHyperBeam()))
#
#

     @Cache.decorator
     def canExitMamaTurtle(self):
         sm = self.smbm
                        # exit mama room
         return sm.wand(sm.wor(sm.canFly(),
                               sm.haveItem('HiJump')),
                        # go back to main street (use crounched jump over the pirates)
                        sm.canGravLessLevel1())

    @Cache.decorator
    def canGoUpMtEverest(self):
        sm = self.smbm
        return sm.wor(sm.haveItem('Gravity'),
                      # TODO::try other suitless items / route through fish tank
                      sm.wand(sm.knowsGravLessLevel1(),
                              sm.haveItem('HiJump'),
                              sm.haveItem('Grapple')))
    
#    @Cache.decorator
#    def canJumpUnderwater(self):
#        sm = self.smbm
#        return sm.wor(sm.haveItem('Gravity'),
#                      sm.wand(sm.knowsGravLessLevel1(),
#                              sm.haveItem('HiJump')))
#
#    @Cache.decorator
#    def canPassBotwoonHallway(self):
#        sm = self.smbm
#        return sm.wor(sm.wand(sm.haveItem('SpeedBooster'),
#                              sm.haveItem('Gravity')),
#                      sm.wand(sm.knowsMochtroidClip(), sm.haveItem('Ice')),
#                      sm.canCrystalFlashClip())
#
    @Cache.decorator
    def canDefeatBotwoon(self):
        sm = self.smbm
        return sm.wand(sm.enoughStuffBotwoon(),
                       sm.haveItem('Morph'))

    @Cache.decorator
    def canReachCacatacAlleyFromBotowoon(self):
        sm = self.smbm
                       # fall through the morph maze
        return sm.wand(sm.haveItem('Morph'),
                       sm.canGravLessLevel1(),
                       # enter cacatac alley from halfie climb room
                       sm.wor(sm.haveItem('HiJump'),
                              sm.haveItem('Ice'),
                              sm.haveItem('SpeedBooster'),
                              sm.canFly()))

    @Cache.decorator
    def canPassCacatacAlley(self):
        sm = self.smbm
        return sm.wand(Bosses.bossDead(sm, 'Draygon'),
                       # cacatac alley suitless: hijump + gravless level 1
                       # butterfly room suitless: hijump + ice + gravless level 2
                       sm.wor(sm.haveItem('Gravity'),
                              sm.wand(sm.haveItem('HiJump'),
                                      sm.haveItem('Ice'),
                                      sm.knowsGravLessLevel2())))

#    @Cache.decorator
#    def canGoThroughColosseumSuitless(self):
#        sm = self.smbm
#        return sm.wor(sm.haveItem('Grapple'),
#                      sm.haveItem('SpaceJump'),
#                      sm.wand(sm.haveItem('Ice'),
#                              sm.energyReserveCountOk(int(7.0/sm.getDmgReduction(False)[0])), # mochtroid dmg
#                              sm.knowsBotwoonToDraygonWithIce()))
#
    @Cache.decorator
    def canEnterExitAqueduct(self):
        # could wait for snails and use them to jump over the hole in the middle,
        # only as sequence break for now as snails make lots of damage suitless
        sm = self.smbm
                       # break the pb and super blocks
        return sm.wand(sm.canUsePowerBombs(), can.haveItem('Super'),
                       sm.wor(sm.wand(sm.haveItem('Gravity'),
                                      sm.wor(sm.canFly(),
                                             sm.haveItem('HiJump')))
                              # IBJ underwater
                              sm.canInfiniteBombJumpSuitless()))

    @Cache.decorator
    def canGravLessLevel1(self):
        sm = self.smbm
        return sm.wor(sm.haveItem('Gravity'), sm.knowsGravLessLevel1())

    @Cache.decorator
    def canEnterExitBotwoon(self):
        # used for post botwoon -> aqueduct bottom and post botwoon -> colosseum top right
        sm = self.smbm
        return sm.wand(sm.haveItem('Morph'),
                       sm.wor(sm.haveItem('Gravity'),
                              # hijump is enough for suitless
                              sm.wand(sm.knowsGravLessLevel1(), sm.haveItem('HiJump'))))

#    @Cache.decorator
#    def canColosseumToBotwoonExit(self):
#        sm = self.smbm
#        return sm.wor(sm.haveItem('Gravity'),
#                      sm.wand(sm.knowsGravLessLevel2(),
#                              sm.haveItem("HiJump"),
#                              sm.canGoThroughColosseumSuitless()))
#
#    @Cache.decorator
#    def canClimbColosseum(self):
#        sm = self.smbm
#        return sm.wor(sm.haveItem('Gravity'),
#                      sm.wand(sm.knowsGravLessLevel2(),
#                              sm.haveItem("HiJump"),
#                              sm.wor(sm.haveItem('Grapple'),
#                                     sm.haveItem('Ice'),
#                                     sm.knowsPreciousRoomGravJumpExit())))
#
#    @Cache.decorator
#    def canClimbWestSandHole(self):
#        sm = self.smbm
#        return sm.wor(sm.haveItem('Gravity'),
#                      sm.wand(sm.haveItem('HiJump'),
#                              sm.knowsGravLessLevel3(),
#                              sm.wor(sm.haveItem('SpaceJump'),
#                                     sm.canSpringBallJump(),
#                                     sm.knowsWestSandHoleSuitlessWallJumps())))
#
#    @Cache.decorator
#    def canAccessItemsInWestSandHole(self):
#        sm = self.smbm
#        return sm.wor(sm.wand(sm.haveItem('HiJump'), # vanilla strat
#                              sm.canUseSpringBall()),
#                      sm.wand(sm.haveItem('SpaceJump'), # alternate strat with possible double bomb jump but no difficult wj
#                              sm.wor(sm.canUseSpringBall(),
#                                     sm.canUseBombs())),
#                      sm.wand(sm.canPassBombPassages(), # wjs and/or 3 tile mid air morph
#                              sm.knowsMaridiaWallJumps()))
#
#    @Cache.decorator
#    def getDraygonConnection(self):
#        return getAccessPoint('DraygonRoomOut').ConnectedTo
#
#    @Cache.decorator
#    def isVanillaDraygon(self):
#        return SMBool(self.getDraygonConnection() == 'DraygonRoomIn')
#
    @Cache.decorator
    def isVanillaCroc(self):
        crocRoom = getAccessPoint('Crocomire Room Top')
        return SMBool(crocRoom.ConnectedTo == 'Crocomire Speedway Bottom')

    @Cache.decorator
    def canFightDraygon(self):
        sm = self.smbm
        return sm.wor(sm.haveItem('Gravity'),
                      sm.wand(sm.wor(sm.knowsGravLessLevel2(),
                                     sm.knowsGravLessLevel3())))

#    @Cache.decorator
#    def canDraygonCrystalFlashSuit(self):
#        sm = self.smbm
#        return sm.wand(sm.canCrystalFlash(),
#                       sm.knowsDraygonRoomCrystalFlash(),
#                       # ask for 4 PB pack as an ugly workaround for
#                       # a rando bug which can place a PB at space
#                       # jump to "get you out" (this check is in
#                       # PostAvailable condition of the Dray/Space
#                       # Jump locs)
#                       sm.itemCountOk('PowerBomb', 4))
#
#    @Cache.decorator
#    def canExitDraygonRoomWithGravity(self):
#        sm = self.smbm
#        return sm.wand(sm.haveItem('Gravity'),
#                       sm.wor(sm.canFly(),
#                              sm.knowsGravityJump(),
#                              sm.wand(sm.haveItem('HiJump'),
#                                      sm.haveItem('SpeedBooster'))))
#
#    @Cache.decorator
#    def canGrappleExitDraygon(self):
#        sm = self.smbm
#        return sm.wand(sm.haveItem('Grapple'),
#                       sm.knowsDraygonRoomGrappleExit())
#
#    @Cache.decorator
#    def canExitDraygonVanilla(self):
#        sm = self.smbm
#        # to get out of draygon room:
#        #   with gravity but without highjump/bomb/space jump: gravity jump
#        #     to exit draygon room: grapple or crystal flash (for free shine spark)
#        #     to exit precious room: spring ball jump, xray scope glitch or stored spark
#        return sm.wor(sm.canExitDraygonRoomWithGravity(),
#                      sm.wand(sm.canDraygonCrystalFlashSuit(),
#                              # use the spark either to exit draygon room or precious room
#                              sm.wor(sm.canGrappleExitDraygon(),
#                                     sm.wand(sm.haveItem('XRayScope'),
#                                             sm.knowsPreciousRoomXRayExit()),
#                                     sm.canSpringBallJump())),
#                      # spark-less exit (no CF)
#                      sm.wand(sm.canGrappleExitDraygon(),
#                              sm.wor(sm.wand(sm.haveItem('XRayScope'),
#                                             sm.knowsPreciousRoomXRayExit()),
#                                     sm.canSpringBallJump())),
#                      sm.canDoubleSpringBallJump())
#
#    @Cache.decorator
#    def canExitDraygonRandomized(self):
#        sm = self.smbm
#        # disregard precious room
#        return sm.wor(sm.canExitDraygonRoomWithGravity(),
#                      sm.canDraygonCrystalFlashSuit(),
#                      sm.canGrappleExitDraygon(),
#                      sm.canDoubleSpringBallJump())
#
#    @Cache.decorator
#    def canExitDraygon(self):
#        sm = self.smbm
#        if self.isVanillaDraygon():
#            return self.canExitDraygonVanilla()
#        else:
#            return self.canExitDraygonRandomized()
#
#    @Cache.decorator
#    def canExitPreciousRoomVanilla(self):
#        return SMBool(True) # handled by canExitDraygonVanilla
#
#    @Cache.decorator
#    def canExitPreciousRoomRandomized(self):
#        sm = self.smbm
#        suitlessRoomExit = sm.canSpringBallJump()
#        if suitlessRoomExit.bool == False:
#            if self.getDraygonConnection() == 'KraidRoomIn':
#                suitlessRoomExit = sm.canShortCharge() # charge spark in kraid's room
#            elif self.getDraygonConnection() == 'RidleyRoomIn':
#                suitlessRoomExit = sm.wand(sm.haveItem('XRayScope'), # get doorstuck in compatible transition
#                                           sm.knowsPreciousRoomXRayExit())
#        return sm.wor(sm.wand(sm.haveItem('Gravity'),
#                              sm.wor(sm.canFly(),
#                                     sm.knowsGravityJump(),
#                                     sm.haveItem('HiJump'))),
#                      suitlessRoomExit)
#
#    def canExitPreciousRoom(self):
#        if self.isVanillaDraygon():
#            return self.canExitPreciousRoomVanilla()
#        else:
#            return self.canExitPreciousRoomRandomized()
