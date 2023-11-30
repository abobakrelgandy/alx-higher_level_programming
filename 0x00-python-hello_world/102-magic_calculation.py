#!/bin/bash
# Check if PYFILE is set
if [ -z "$PYFILE" ]
then
    echo "PYFILE is not set"
    exit 1
fi

# Compile the Python file
echo "Compiling $PYFILE ..."
python -m compileall -b $PYFILE

# Rename the output file
mv "${PYFILE}c" "${PYFILE}c"

echo "Compilation complete."
