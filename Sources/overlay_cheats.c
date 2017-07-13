#include "cheats.h"
#include "hid.h"
#include "global.h"
#include "ov.h"

Handle fsUserHandle = 0;

#define CALLBACK_OVERLAY (101)

#define TICKS_PER_MSEC (268123.480)
#define BLANK 255,255,255


vu8 isBottomToggle = 0;


void drawOverlay() {}


u32 overlayCallback(u32 isBottom, u32 addr, u32 addrB, u32 stride, u32 format) {
    // Set draw settings
    OvSettings(addr, addrB, stride, format, !isBottomToggle);

	if(isBottom == isBottomToggle){
        // drawOverlay();
        return 0;
	}

    return 1;
}

void overlayInit(void) {
    initSharedFunc();
    plgRegisterCallback(CALLBACK_OVERLAY, (void*) overlayCallback, 0);
}
