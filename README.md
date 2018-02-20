[![Build Status](https://travis-ci.org/pavelkryukov/gnu-binutils-clang.svg?branch=master)](https://travis-ci.org/pavelkryukov/gnu-binutils-clang)

# GNU Binutils + Clang
Automated build of GNU Binutils and GDB with Clang

The methodology originates from [MIPT-MIPS](http://mipt-ilab.github.io/mipt-mips/) project which builds GNU Binutils for MIPS as a part of CI. 

## Vulnerabilities found:
 * ~~**[PR22245](https://sourceware.org/bugzilla/show_bug.cgi?id=22245)**~~ — potential UB in calling variadic argument function. Reported by [Kirill Nedostoev](https://github.com/inedostoev) while resolving ~~[MIPT-MIPS/#147](https://github.com/MIPT-ILab/mipt-mips/issues/147)~~.
 * **[PR22612](https://sourceware.org/bugzilla/show_bug.cgi?id=22612)** — 64-bit DWARF support is dead due as offset variable is 32-bit.
 
## Compilation errors:
 * ~~**[PR22485](https://sourceware.org/bugzilla/show_bug.cgi?id=22485)**~~ — C89-imcompatible initialization of structure.
 * ~~**[PR22495](https://sourceware.org/bugzilla/show_bug.cgi?id=22495)**~~ — deep call of "printf" with non-literal format.
