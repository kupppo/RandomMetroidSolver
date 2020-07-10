;;; This patch handles the specifics for area rando doors;;; 
;;; - refill at Tourian elevator
;;; - maridia sand warp
;;; - croc area exit bugfix
;;;
;;; compile with asar (https://www.smwcentral.net/?a=details&id=14560&p=section),

lorom
arch snes.cpu

;;; For refill
!samus_health          = $09c2
!samus_max_health      = $09c4
!samus_reserve         = $09d6
!samus_max_reserve     = $09d4
!samus_missiles        = $09c6
!samus_max_missiles    = $09c8
!samus_supers          = $09ca
!samus_max_supers      = $09cc
!samus_pbs             = $09ce
!samus_max_pbs         = $09d0
!samus_reserve         = $09d6
!samus_max_reserve     = $09d4

org $8ff700
;;; "ship refill" for tourian elevator
full_refill:
	lda !samus_max_health
	sta !samus_health
	lda !samus_max_reserve
	sta !samus_reserve
	lda !samus_max_missiles
	sta !samus_missiles
	lda !samus_max_supers
	sta !samus_supers
	lda !samus_max_pbs
	sta !samus_pbs
.end:
	rts

warnpc $8ff7ef

;;; use this as croc top exit door asm :
;;; croc draws its tilemap on BG2, and a routine to draw enemy
;;; BG2 ($A0:9726) is ran both by Croc/MB and at the end every
;;; door transition. It uses $0e1e as flag to know if a VRAM transfer
;;; has to be done. If we exit during croc fight, the value can be non-0
;;; and some garbage resulting from room tiles decompression of door transition
;;; is copied to BG2 tilemap in the next room.
org $8ff7f0
croc_exit_fix:
    stz $0e1e	; clear the flag to disable enemy BG2 tilemap routine
    rts

;;; door pointers for room below botwoon
below_botwoon_doors:
	dw $a7d4,$a534

;;; stop before generated door asm routines start
warnpc $8ff7ff

;;; add door in room below botwoon etank (room header update)
org $8FD706
    dw below_botwoon_doors

;; update left sand hall left door to lead to it
org $83a63c
	dw $D6FD
	db $00,$05,$3E,$06,$03,$00
	dw $8000,$0000

;;; Tourian Elevator door ASM ptr
org $83922c
	dw full_refill
