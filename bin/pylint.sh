#!/bin/bash
pylint --rcfile $HOME/BaseStack/bin/pylint.rcfile $@ | grep "," > /tmp/pylint.out
grep -v "Unable to import" /tmp/pylint.out | more
