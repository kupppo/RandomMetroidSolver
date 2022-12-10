;;; VARIA new game hook: skips intro and customizes starting point
;;;
;;; compile with asar v1.81 (https://github.com/RPGHacker/asar/releases/tag/v1.81)

arch 65816
lorom

incsrc "sym/base.asm"

;;; CONSTANTS
!GameStartState = $7ED914

;;; HIJACKS (bank 82 init routines)

org $82801d
    jsl startup

org $828067
    jsl gameplay_start

;;; This skips the intro : game state 1F instead of 1E
org $82eeda
    db $1f

;;; DATA in bank A1 (start options)

org $a1f200
start_location:
    ;; start location: $0000=Zebes Landing site, $fffe=Ceres,
    ;; otherwise hi byte is area and low is save index.
    ;; (use FFFE as Ceres special value because FFFF can be mistaken
    ;; for free space by solver/tracker)
    dw $0000			; defaults to landing site
opt_doors:
    ;; optional doors to open.
    ;; door ID is low byte PLM argument when editing doors in SMILE
    ;; terminate with $00
    db $10,$32			; defaults to red tower top+construction zone
    db $00

;;; CODE in bank A1
org $a1f220
startup:
    jsl base_check_new_game : bne .end
    lda.l start_location
    cmp #$fffe : beq .ceres
    ;; start point on Zebes
    pha
    and #$ff00 : xba : sta $079f ; hi byte is area
    pla : pha
    and #$00ff : sta $078b      ; low byte is save index
    pla : beq .zebes
    lda #$0000 : jsl $8081fa    ; wake zebes if not ship start
.zebes:
    lda #$0005 : bra .store_state
.ceres:
    lda #$001f
.store_state:
    sta !GameStartState
.end:
    ;; run hijacked code and return
    lda !GameStartState
    rtl

gameplay_start:
    jsl base_check_new_game  : bne .end
    ;; Set doors to blue if necessary
    phx
    ldx #$0000
-
    lda.l opt_doors,x : and #$00ff
    beq .save			; end list
    phx
    jsl $80818e		    ; call bit index function, returns X=byte index, $05e7=bitmask
    ;; Set door in bitfield
    lda $7ED8B0,x : ora $05E7 : sta $7ED8B0,x
    plx
    inx : bra -		    ; next
.save:
    ;; Call the save code to create a new file
    plx
    jsr add_etanks_and_save
.end:
    rtl

warnpc $a1f28f

org $a1f470
additional_etanks:
	db $00

add_etanks_and_save:
	sep #$20
	lda.l additional_etanks : sta $4202
	lda #$64 : sta $4203
	pha : pla : xba : xba
	rep #$20
	lda $4216 : clc : adc #$0063
	sta $09c4
	sta $09c2
	jsl base_new_save
	rts

warnpc $a1f4ff

;;; patch pit and climb room states
org $8fe652
;;; pit room: in vanilla, checks for morph+missiles collection
morph_missile_check:
    ;; check that zebes is awake instead: works with both standard
    ;; start with wake_zebes.ips, and non standard start with wake
    ;; zebes forced from the start.
    lda #$0000 : jsl $808233
    bcc .not_awake
    bra .awake
org $8fe65f
.awake:
org $8fe666
.not_awake:

;;; Enemies gray doors set zebes awake when unlocking.
;;; Disable that, as the event is set in blue brin by
;;; wake_zebes patch (or right away if random start),
;;; and we don't want it to be set if we encounter
;;; Climb flashing portal door (enemy door set at 0)
org $84BE0B
skip_wake_zebes:
	bra .skip
org $84BE12
.skip:
