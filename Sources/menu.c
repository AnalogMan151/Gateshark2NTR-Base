#include "cheats.h"

// Note: Luma3DS LayeredFS writes code up to 0x005977B8. Do not use addresses
// prior to this when storing ASM code for cheats

char	*builder_name = "AnalogMan",
        version[7] = "v1.0.0",
        formattedVer[27];



void    always_run(void) {
    execute_all();
}


void	my_menus(void) {
    overlayInit();
    xsprintf(formattedVer, "%19s", version);
    new_unselectable_entry("Entries w/ an orange background");
    new_unselectable_entry("have notes. Press (Y) to view.");
    new_super_unselectable_entry(formattedVer, always_run);
	new_separator();

    new_entry_managed_note("Name of cheat", "Cheat note", nullCheat, NULLCHEAT, 0);
    new_entry_managed("Name of cheat", nullCheat, NULLCHEAT, 0);
    new_entry_managed("Name of Cheat", nullCheat, NULLCHEAT, AUTO_DISABLE);

    new_entry_arg_note("Name of cheat", "Cheat note", nullCheatToggle, 0, NULLCHEATTOGGLE, TOGGLE);
    new_entry_arg("Name of cheat", nullCheatToggle, 0, NULLCHEATTOGGLE, TOGGLE);

}
