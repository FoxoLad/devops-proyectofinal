#!/bin/bash

echo "==================================="
echo " User Management Script"
echo "==================================="

GROUP_NAME="devops"
USER_NAME="devops_user"

echo "Creating group..."
sudo groupadd $GROUP_NAME

echo "Creating user..."
sudo useradd -m -g $GROUP_NAME $USER_NAME

echo "Setting password for user..."
echo "devops_user:DevOps123!" | sudo chpasswd

echo "Adding user to docker group..."
sudo usermod -aG docker $USER_NAME

echo "Assigning permissions to environment folder..."
sudo chown -R $USER_NAME:$GROUP_NAME ~/environment

echo "Restoring permissions back to ec2-user..."
sudo chown -R ec2-user:ec2-user ~/environment

echo "User and permissions configured successfully."
