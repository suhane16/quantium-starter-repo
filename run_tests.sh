#!/bin/bash

echo "Activating virtual environment..."
source venv/Scripts/activate

echo "Running test suite..."
pytest tests/test_app.py

if [ $? -eq 0 ]; then
  echo "All tests passed."
  exit 0
else
  echo "Tests failed."
  exit 1
fi