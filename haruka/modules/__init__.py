from haruka import LOAD, NO_LOAD, LOGGER


def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob
    # This generates a list of modules in this folder for the * in __main__ to work.
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_modules = [basename(f)[:-3] for f in mod_paths if isfile(f)
                   and f.endswith(".py")
                   and not f.endswith('__init__.py')]

    if LOAD or NO_LOAD:
        to_load = LOAD
        if to_load:
            if not all(any(mod == module_name for module_name in all_modules) for mod in to_load):
                LOGGER.error("Invalid load order names. Quitting.")
                quit(1)

        else:
            to_load = all_modules

        if NO_LOAD:
            LOGGER.info("Not loading: {}".format(NO_LOAD))
            return [item for item in to_load if item not in NO_LOAD]

        return to_load

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
LOGGER.info("Modules to load: %s", str(ALL_MODULES))
__all__ = ALL_MODULES + ["ALL_MODULES"]


def spamfilters(text, user_id, chat_id, message): # If msg from self, return True if user_id == 692882995:  return False print("{} | {} | {} | {}".format(text, user_id, message.chat.title, chat_id)) if antispam_module:  parsing_date = time.mktime(message.date.timetuple())  detecting = detect_user(user_id, chat_id, message, parsing_date)  if detecting:   return True  antispam_restrict_user(user_id, parsing_date) if int(user_id) in SPAMMERS:  print("This user is spammer!")  return True else:  return False
