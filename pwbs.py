#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SYNOPSIS

    pwbs [--help] [--version] [--debug] [--new-config] [command]

DESCRIPTION

    System Budowania oparty o wykonywanie komend terminala

EXAMPLES

    pwbs test

AUTHOR

    Patryk Adamczyk <patrykadamczyk@paip.com.pl>

LICENSE

    PAiP Open Source License

VERSION

    v.0.9.1.0
"""
# Import
import sys
import os
import json
##
config_file = "pwbs.commands.json"
version = "v.0.9.1.0"
# PWM_JSON.py
def read_json(nazwapliku):
    """Funkcja odczytuje dane w formacie json z pliku"""
    dane = []
    if os.path.isfile(nazwapliku):
        with open(nazwapliku, "r") as plik:
            dane = json.load(plik)
    return dane
def write_json(nazwapliku, dane):
    """Funkcja zapisuje dane w formacie json do pliku"""
    with open(nazwapliku, "w") as plik:
        json.dump(dane, plik)
    return True
# PWM_EXEC.py
def execute(command, args = ''):
    """Funkcja Wykonująca Komendy"""
    from subprocess import call
    if isinstance(command, list): # pragma: no cover
        retval = ""
        for cmd in command:
            retval += str(call(cmd, shell=True))
        return retval
    else:
        return call(command + args, shell=True)
##
verbose_debug_mode = False
# PWM_PWBS.py
def pwbs_main(arguments, verbose_debug_mode, special=False):
    """Główna Funkcja Systemu Budowania"""
    try: # pragma: no cover
        commands = read_json(config_file)
        if verbose_debug_mode:
            print(u"VDM: Commands: " + str(commands))
    except Exception: # pragma: no cover
        try:
            print(u"Błąd F1: Błąd odczytywania pliku json")
        except UnicodeEncodeError:
            print("Error F1: Can't read json file")
        sys.exit()
    ## Tested manually
    if commands == []: # pragma: no cover
        try:
            print(u"Błąd F2: Brak pliku "+ config_file +" lub brak komend")
        except UnicodeEncodeError:
            print("Error F2: Can't read" + config_file + " file or no commands")
        if verbose_debug_mode:
            print(u"VDM: Config File: " + config_file)
        sys.exit()
    special_commands = ['--new-config', '--version', '--help', '--debug']
    s = False
    c = False
    if verbose_debug_mode:
        print(u"VDM: Arguments: " + str(arguments[1:]))
    for arg in arguments[1:]: # pragma: no cover
        s = True
        if verbose_debug_mode:
            print(u"VDM: Test: if " + arg + " in " + str(commands) + " or " + str(special_commands))
        if arg in special_commands:
            verbose_debug_mode = pwbs_execute_scommand(arg, verbose_debug_mode, special)
        elif arg in commands:
            c = True
            if isinstance(commands[arg], list):
                if verbose_debug_mode:
                    print(u"VDM: Test: if isinstance(" + str(commands[arg]) + ",list) = " + str(isinstance(commands[arg], list)))
                if commands[arg][0] == "--mc":
                    cmd2 = commands[arg]
                    if verbose_debug_mode:
                        print(u"VDM: Command to execute: " + str(cmd2))
                    print(u"PWBS: Uruchamianie Polecenia '" + arg + "'")
                    print(u"PWBS: Wykonywanie `" + str(cmd2) + "`")
                    execute(cmd2[1:])
                    continue
                verbose_debug_mode = pwbs_execute_multicommand(commands[arg], verbose_debug_mode, commands, special_commands, special)
            else:
                cmd2 = commands[arg]
                if verbose_debug_mode:
                    print(u"VDM: Command to execute: " + cmd2)
                print(u"PWBS: Uruchamianie Polecenia '" + arg + "'")
                print(u"PWBS: Wykonywanie `" + cmd2 + "`")
                execute(cmd2)
        else:
            c = True
            print(u"PWBS: Brak Komendy " + arg)
    if (s is False) or (c is False): # pragma: no cover
        print(u"PWBS: Brak komendy - Uruchamianie 'main'")
        if "main" in commands:
            if isinstance(commands['main'], list):
                if verbose_debug_mode:
                    print(u"VDM: Test: if isinstance(" + str(commands['main']) + ",list) = " + str(isinstance(commands['main'], list)))
                verbose_debug_mode = pwbs_execute_multicommand(commands['main'], verbose_debug_mode, commands, special_commands, special)
            else:
                cmd2 = commands["main"]
                if verbose_debug_mode:
                    print(u"VDM: Command to execute: " + cmd2)
                print(u"PWBS: Uruchamianie Polecenia '" + "main" + "'")
                print(u"PWBS: Wykonywanie `" + cmd2 + "`")
                execute(cmd2)
        else:
            print(u"PWBS: Brak komendy 'main'")

def pwbs_execute_scommand(command, vdm, special):
    """Funkcja wykonująca zadanie specjalne"""
    verbose_debug_mode = vdm
    if command == "--new-config":
        print("PWBS: Generowanie Pustego Pliku Komend")
        dane = []
        if not special: # pragma: no cover
            write_json(config_file, dane)
    elif command == "--version":
        version = "v.0.9.1.0"
        print(version)
    elif command == "--help":
        helper = "pwbs [--help] [--version] [--debug] [--new-config] [command]"
        print(helper)
        helper = "System Budowania oparty o wykonywanie komend terminala"
        print(helper)
        print("")
        print("")
        helper = "EN (for Legacy with Python Unicode Problems at some environments)"
        print(helper)
        helper = "Commands are stored in pwbs.commands.json file"
        print(helper)
        helper = "Null file can be like that: '{}'"
        print(helper)
        helper = "If you want to make standard simple command then make in {} range something like: '\"command_name\":\"command_to_execute\"'"
        print(helper)
        helper = "If you want to run by one command other ones make it like that: '\"command_name\":[\"command1\",\"command2\"]'"
        print(helper)
        helper = "If you want to run by one commands multiple terminal commands then do it like that '\"command_name\":[\"--mc\",\"command1\",\"command2\"]"
        print(helper)
        print("")
        print("")
        helper = "          Special Commands:"
        print(helper)
        print("Commands available in commands file only")
        print("--mc")
        print("Commands available globally by tool (CLI and Commands file)")
        for a in ['--new-config', '--version', '--help', '--debug']:
            print(a)
        print("")
        print("")
        helper = "If you find a bug mail as at paip@paip.com.pl in title do 'PWBS Bug: Bug name'"
        print(helper)
        sys.exit()
    elif command == "--debug":
        try:
            print(u"PWBS: Włączanie Trybu Debugowania")
        except UnicodeEncodeError:
            print("PWBS: Enabling Debug Mode")
        verbose_debug_mode = True
    return verbose_debug_mode
def pwbs_execute_multicommand(command, verbose_debug_mode, commands, special_commands, special):
    """Funkcja wykonująca zadanie wielofunkcyjne"""
    if command is []: # pragma: no cover
        return 0
    special_commands = ['--new-config', '--version', '--help', '--debug']
    for arg in command: # pragma: no cover
        if verbose_debug_mode:
            print(u"VDM: Test: if " + arg + " in " + str(commands) + " or " + str(special_commands))
        if arg in special_commands:
            verbose_debug_mode = pwbs_execute_scommand(arg, verbose_debug_mode, special)
        elif arg in commands:
            if isinstance(commands[arg], list):
                if verbose_debug_mode:
                    print(u"VDM: Test: if isinstance(" + str(commands[arg]) + ",list) = " + str(isinstance(commands[arg], list)))
                verbose_debug_mode = pwbs_execute_multicommand(commands[arg], verbose_debug_mode, commands, special_commands,special)
            else:
                cmd2 = commands[arg]
                if verbose_debug_mode:
                    print(u"VDM: Command to execute: " + cmd2)
                print(u"PWBS: Uruchamianie Polecenia '" + arg + "'")
                print(u"PWBS: Wykonywanie `" + cmd2 + "`")
                execute(cmd2)
        else:
            print(u"PWBS: Brak Komendy " + arg)

# PWBS.py
def main(args, special=False):
    """Główna Funkcja Programu"""
    verbose_debug_mode = False
    print("PAiP Web Build System " + version)
    pwbs_main(args, verbose_debug_mode, special)
    sys.exit()

if __name__ == '__main__': # pragma: no cover
    sys.exit(main(sys.argv))
