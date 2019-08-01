// Meta
type PWBSMode = string;
// PWBS Types
/// Single Task - One name for one command
type SingleTask = string;
/// Multi Command Task - One name for multiple commands
type MultiCommandTask = string[];
/// Modded Task Array - One name for special type of list with commands
type ModedTaskArray = [PWBSMode, ...string[]];
/// Arguments for task - Array of string are positional arguments, object is key-named arguments
type PWBSArguments = string[] | {
    [argument: string]: string
};
/// Configuration for Task - Here you can specify specific configurations for example for plugin tasks
interface PWBSTaskConfiguration {
    [config_name: string]: boolean | number | string,
}
/// Modded Task Object - One Name for special type of task with multiple commands
interface ModedTaskObject {
    mode: PWBSMode, // Type of the task
    commands: SingleTask | MultiCommandTask | ModedTaskArray, // Commands to do in this task
    arguments: PWBSArguments, // Arguments of the task
    async: boolean, // Should this task be executed asynchronously
    configuration: PWBSTaskConfiguration, // Configuration of the task
    extends: string, // Task extends configuration from another one
}
/// Task Type
type PWBSTask = SingleTask | MultiCommandTask | ModedTaskArray | ModedTaskObject;
/// Verbose Level - What information should be shown in logs or console output
// 0 - No Output
// 1 - Minimal Output
// 2 - Normal Output [default]
// 3 - More Output
// 255 - Debug Information will be outputed
type VerboseLevel = 0 | 1 | 2 | 3 | 255;
/// PWBS Configuration
interface PWBSConfig {
    async: boolean, /// Should all tasks should be called asynchronously
    arguments: PWBSArguments, /// Arguments for all tasks
    verbose: VerboseLevel, /// Verbose Level
    debug: boolean, /// Debug Mode
    dockerized: boolean, /// Should all tasks be called from docker container version of pwbs
    extends: string | { /// PWBS Configuration files that this file is based on
        [config_path: string]: {
            include: string[], /// What to include from this config file
            exclude: string[], /// What to exclude from this config file
        }
    }, //path
    logfile?: string, /// Path to log file
    log_to_file: boolean, /// Logging to log file enabled
}
/// Variables for tasks
interface PWBSVariables {
    [variable_name: string]: string,
}
/// Global Configuration
interface PWBSGlobalConfig {
    async: boolean, /// Should all tasks be called asynchronously
    verbose: VerboseLevel, /// Global Verbose Level
    debug: boolean, /// Global Debug Mode
    dockerized: boolean, /// Should all tasks be called in docker container version of pwbs
    logfile?: string, /// Global Log File
    log_to_file: boolean, /// Global Logging to log file
    log_verbose: VerboseLevel, /// Log file verbose level
}
/// PWBS Plugin Configuration
interface PWBSPlugin {
    type: 'json' | 'python' | 'go' | 'javascript' | 'lua' | 'perl' | 'PWBS-Basic' | 'PWL', /// Language that this plugin is write in
    path: string, /// Path to the plugin
    active: boolean, /// Is Plugin Active
    debug: boolean, /// Is debug mode of plugin is turned on
    configuration: { /// Configuration Variables of the plugin
        [config_key: string]: string,
    },
    prefix: string, /// Prefix of tasks that this plugin provide
    exclude: string[], /// Exclude specific tasks
}
/// PWBS List of Plugins
interface PWBSPluginList {
    [pluginName: string]: PWBSPlugin,
}
/// Platform (Operating System)
type PWBSPlatform = 'Windows' | 'Win' | 'win' | 'Linux' | 'Lin' | 'lin' | 'Mac OS X' | 'osx' | 'OSX';
// Config Interface
/// Local Configuration File | {CWD}/pwbs.json
interface PWBSLocalConfigurationFile {
    tasks: { /// Tasks that PWBS can execute
        [task: string]: PWBSTask,
    },
    os_tasks: { /// Tasks that are os dependent that PWBS can execute
        [os: PWBSPlatform]: {
            [task: string]: PWBSTask,
        }
    }
    configuration: PWBSConfig, /// Configuration of PWBS
    plugins: PWBSPluginList, /// Plugins to use when executing this config
}
/// Global Configuration File | ~/.pwbs/pwbs.config.json
interface PWBSGlobalConfigurationFile {
    global_tasks: { /// Tasks that are globally available
        [task: string]: PWBSTask,
    },
    global_os_tasks: { /// Tasks that are os dependent that are globally available
        [os: PWBSPlatform]: {
            [task: string]: PWBSTask,
        },
    },
    global_plugins: PWBSPluginList, /// Plugins which will be used for every config

    global_variables: PWBSVariables, /// Global Variables that can be used in tasks
    configuration: PWBSGlobalConfig, /// Global Configuration
}