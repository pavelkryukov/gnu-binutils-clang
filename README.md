# GNU Binutils + Clang
Automated build of GNU Binutils and GDB with Clang Static Analyzer.

The methodology originates from [MIPT-MIPS](http://mipt-ilab.github.io/mipt-mips/) project which built GNU Binutils for MIPS as a part of CI. 

## Vulnerabilities found:
 * ~~**[PR22245](https://sourceware.org/bugzilla/show_bug.cgi?id=22245)**~~ — potential UB in calling variadic argument function. Reported by [Kirill Nedostoev](https://github.com/inedostoev) while resolving ~~[MIPT-MIPS/#147](https://github.com/MIPT-ILab/mipt-mips/issues/147)~~.
 * ~~**[PR22612](https://sourceware.org/bugzilla/show_bug.cgi?id=22612)**~~ — 64-bit DWARF support is dead due as offset variable is 32-bit.
 
## Compilation errors:
 * ~~**[PR22485](https://sourceware.org/bugzilla/show_bug.cgi?id=22485)**~~ — C89-imcompatible initialization of structure.
 * ~~**[PR22495](https://sourceware.org/bugzilla/show_bug.cgi?id=22495)**~~ — deep call of "printf" with non-literal format.
 * [`3046d67`](https://sourceware.org/git?p=binutils-gdb.git;a=commit;h=3046d67a0e29686ec18abd719660969c97973063)
 * [`ad9675d`](https://sourceware.org/git?p=binutils-gdb.git;a=commit;h=ad9675dd80b41d2098fc2dc352c423fbfea0f5b1)
 * [`382bc56`](https://sourceware.org/git?p=binutils-gdb.git;a=commit;h=382bc56bc702608c2f493f743c2e990435a7a74c)

## Clang bugs:
  * **[PR36505](https://bugs.llvm.org/show_bug.cgi?id=36505)** — Clang-tidy: expression with calls to a non-pure function is considered as always-true
