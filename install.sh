#!/bin/bash

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
# Check if -nocp is in any of the passed parameters
skip_checkpoints=false
for param in "$@"; do
    if [ "$param" = "-nocp" ]; then
        skip_checkpoints=true
        break
    fi
done

# Run checkpoints.sh
if [ "$1" != "-nocp" ]; then
    echo "Running checkpoints.sh..."
    ./checkpoints.sh
fi

# Check if the script executed successfully
if [ $? -eq 0 ]; then
    echo "checkpoints.sh executed successfully."
else
    echo "Error: checkpoints.sh failed to execute properly."
    exit 1
fi

python -m venv cutenv
source cutenv/bin/activate


pip install -r requirements.txt
echo "All dependencies are installed successfully."
