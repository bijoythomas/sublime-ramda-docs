Sublime Mocha Test Runner
=========================
Runs mocha tests with the option to run specific tests or all tests in a file.
Inspired by the mocha test runner plugin for Atom [https://github.com/TabDigital/atom-mocha-test-runner]

Requirements
============
The mocha command should be available in the PATH. The plugin has been tested against python 3.5.1

Installation
------------
To install it **manually with Git:** Clone the repository in your Sublime Text 3 Packages directory:

    git clone https://github.com/bijoythomas/sublime-ramda-docs ramdadocs


The "Packages" directory should be located at:

* OS X:

    ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/

* Linux:

    ~/.Sublime\ Text\ 3/Packages/  
    or  
    ~/.config/sublime-text-3/Packages/

* Windows:

    %APPDATA%/Sublime Text 3/Packages/


The plugin should be picked up automatically. If not, restart Sublime Text.

Usage
-----

The plugin adds the following key bindings.

```
[
  {
      "keys": ["ctrl+r"], "command": "ramda_docs"
  }
]
```


