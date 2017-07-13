#include "cheats.h"

char	*builder_name = "AnalogMan",
        version[7] = "v1.0.0",
        formattedVer[27];

// Do not remove but additional function may be added
// that need to be continously run
void    always_run(void) {
    execute_all();
}


void	my_menus(void) {
    // Do not remove START
    overlayInit();
    xsprintf(formattedVer, "%19s", version);
    new_unselectable_entry("Entries w/ an orange background");
    new_unselectable_entry("have notes. Press (Y) to view.");
    new_super_unselectable_entry(formattedVer, always_run);
	new_separator();
    // Do not remove END

    // Below be altered
    new_spoiler("Spoiler 1");
        new_entry_managed_note("Name of cheat", "Cheat note", nullCheat, NULLCHEAT, 0);
        new_entry_managed("Name of cheat", nullCheat, NULLCHEAT, 0);
        new_entry_managed("Name of Cheat", nullCheat, NULLCHEAT, AUTO_DISABLE);
    exit_spoiler();

    new_spoiler("Spoiler 2");
        new_entry_arg_note("Name of cheat", "Cheat note", nullCheatToggle, 0, NULLCHEATTOGGLE, TOGGLE);
    exit_spoiler();

    new_line();

    new_entry_arg("Name of cheat", nullCheatToggle, 0, NULLCHEATTOGGLE, TOGGLE);


}
