# PAiP Web Build System | Dev 2.0
## Release Plan
```
Make a 0.4.0-devX release branch to make complete rethink of structure and rewrite of everything or components. Branch 0.4.0-devX should be not feature update but internal structure and api update.
```
## Rules for Codename Dev 2.0
```markdown
1. Follow PEP8 Rules
2. Make use of Standard Library
3. Documentation and Comments -> English Only
```
## IDEAS
### Modules Divide
```markdown
# pwbs
## pwbs.core | Place for core function like argument parser
## pwbs.api  | Place for public api function to make use of them in __Plugins feature__
## pwbs.core.lib / pwbs.lib | Place for Libraries like PWM or Code Snippets to do specific function [Easier Place for Libraries of PWBS which can't be as dependency package (by not existing package)]
## pwbs.command | Place for logic of Commands
## pwbs.log | Place for New Logging/Console Output System
## pwbs.core.plugins | Place for future PWBS Internal Plugins
## pwbs.tests | Place for Tests of every feature in PWBS and every function
## pwbs.config | Place for Configuration Manager
```
### Documentation
```
Documentation is important thing so we should make it as good as possible.
```
### Release Loop
```
Need to think for that
```
