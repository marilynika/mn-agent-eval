#!/bin/bash
if grep -q "1.0" /logs/verifier/reward.txt; then
    exit 0
else
    exit 1
fi
