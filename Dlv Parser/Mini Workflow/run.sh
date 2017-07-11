#!/bin/bash
DLV=./dlv_bin/dlv.i386-apple-darwin.bin
$DLV -silent -N=8 dlv_input/nqueens.dlv > dlv_output/nqueens.asp
