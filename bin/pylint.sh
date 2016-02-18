#!/bin/bash
pylint --rcfile $HOME/BaseStack/bin/pylint.rcfile $@ | more
