# GNU Binutils + Clang
Automated build of GNU Binutils and GDB with Clang Static Analyzer.

The methodology originates from [MIPT-MIPS](http://mipt-ilab.github.io/mipt-mips/) project which built GNU Binutils for MIPS as a part of CI. 

## Vulnerabilities found:
 * ~~**[PR22245](https://sourceware.org/bugzilla/show_bug.cgi?id=22245)**~~ — potential UB in calling variadic argument function. Reported by [Kirill Nedostoev](https://github.com/inedostoev) while resolving ~~[MIPT-MIPS/#147](https://github.com/MIPT-ILab/mipt-mips/issues/147)~~.
 * ~~**[PR22612](https://sourceware.org/bugzilla/show_bug.cgi?id=22612)**~~ — 64-bit DWARF support is dead due as offset variable is 32-bit.
 
## Compilation errors:
 * ~~**[PR22485](https://sourceware.org/bugzilla/show_bug.cgi?id=22485)**~~ — C89-imcompatible initialization of structure.
 * ~~**[PR22495](https://sourceware.org/bugzilla/show_bug.cgi?id=22495)**~~ — deep call of "printf" with non-literal format.
 * [3046d67](https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;a=commit;h=3046d67a0e29686ec18abd719660969c97973063)

## Clang bugs:
  * **[PR36505](https://bugs.llvm.org/show_bug.cgi?id=36505)** — Clang-tidy: expression with calls to a non-pure function is considered as always-true
