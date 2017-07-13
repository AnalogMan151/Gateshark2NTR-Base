#include "cheats.h"

// Note: Luma3DS LayeredFS writes code up to 0x005977B8. Do not use addresses
// prior to this when storing ASM code for cheats

char	*builder_name = "AnalogMan",
        version[7] = "v1.0.0",
        formattedVer[22];



void    always_run(void) {
    execute_all();
}


void	my_menus(void) {
    overlayInit();
    xsprintf(formattedVer, "%14s", version);
    new_unselectable_entry("Entries w/ an orange background");
    new_unselectable_entry("have notes. Press (Y) to view.");
    new_super_unselectable_entry(formattedVer, always_run);
	new_separator();

}
