#ifndef CHEATS_H
#define CHEATS_H
#include "plugin.h"

// Do not remove START
typedef enum
{
    EXECUTE_ONCE = BIT(0),
    EXECUTED = BIT(1),
    TOGGLE = BIT(2),
    TOGGLE_ENABLE = BIT(3),
    AUTO_DISABLE = BIT(4)
}               entry_flags;
// Do not remove END

// Add identifier for each cheat to be used with disableCheat() and
// AUTO_DISABLE
enum {
    NULLCHEAT,
    NULLCHEATTOGGLE,
} e_identifiers;



// Helpers Do not remove
void    disable_entry(int identifier);
void    update_status(int state, int identifier);
void    new_entry_note(char *str, const char * const note, void (*function)(void));
void    new_entry_managed(char *str, void (*function)(void), int identifier, int flags);
void    new_entry_managed_note(char *str, const char * const note, void (*function)(void), int identifier, int flags);
void    new_entry_arg(char *name, void (*function)(u32), u32 arg, int identifier, int flags);
void    new_entry_arg_note(char *name, char *note, void (*function)(u32), u32 arg, int identifier, int flags);
void    new_super_unselectable_entry(char *str, void (*f)());
void    execute_all(void);
void    replace_pattern(char *pattern, char *replace_str, int identifier);
void    add_prefix(char *prefix, int identifier);
void    add_suffix(char *suffix, int identifier);
void    xsprintf(char *dst, char *fmt, ...);
bool    isinArray(int val, const int *arr, int size);
void    memset32(void *dst, unsigned int value, unsigned int size);
void    protect_region(u32 addr);
bool    checkAddress(u32 address);
int     randomNum(int start, int end);
bool    getWifiStatus(void);
void    overlayInit(void);

// Cheats
void    nullCheat(void);
void    nullCheatToggle(u32 state);


#endif
