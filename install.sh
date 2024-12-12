#!/bin/bash


skip_checkpoints=false
create_env=false
for param in "$@"; do
    if [ "$param" = "-nocp" ]; then
        skip_checkpoints=true
    fi
    if [ "$param" = "-env" ]; then
        create_env=true
    fi
done

# Run checkpoints.sh
if [ "$skip_checkpoints" = false ]; then
    echo "Running checkpoints.sh..."
    ./checkpoints.sh
else
    echo "Skipping checkpoints.sh..."
fi


if [ "$create_env" = true ]; then
    python -m venv cutenv
    source cutenv/bin/activate
fi


pip install --ignore-installed -r requirements.txt
echo "All dependencies are installed successfully."
