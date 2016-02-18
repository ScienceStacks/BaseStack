#!/bin/bash
pylint --rcfile $HOME/BaseStack/bin/pylint.rcfile $@ | grep "," > /tmp/pylint.out
tail -1000 /tmp/pylint.out | more
