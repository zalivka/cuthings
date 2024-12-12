#!/bin/bash

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

# Use either wget or curl to download the checkpoints
if command -v wget &> /dev/null; then
    CMD="wget"
elif command -v curl &> /dev/null; then
    CMD="curl -L -O"
else
    echo "Please install wget or curl to download the checkpoints."
    exit 1
fi


sam2_hiera_l_url=https://dl.fbaipublicfiles.com/segment_anything_2/072824/sam2_hiera_large.pt


echo "Downloading sam2.1_hiera_large.pt checkpoint..."
if [ ! -f "sam2_hiera_large.pt" ]; then
    $CMD $sam2_hiera_l_url || { echo "Failed to download checkpoint from $sam2_hiera_l_url"; exit 1; }
else
    echo "sam2_hiera_large.pt already exists, skipping download"
fi

echo "All checkpoints are downloaded successfully."