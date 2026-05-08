#!/bin/bash

echo "==================================="
echo " DevOps Environment Setup Script"
echo "==================================="

echo "Updating packages..."
sudo yum update -y

echo "Installing Python packages..."
pip3 install boto3

echo "Verifying installations..."

echo "Git version:"
git --version

echo "Python version:"
python3 --version

echo "Docker version:"
docker --version

echo "Boto3 version:"
python3 -c "import boto3; print(boto3.__version__)"

echo "Starting Docker service..."
sudo service docker start

echo "Running Docker test..."
sudo docker run hello-world

echo "Setup completed successfully."
