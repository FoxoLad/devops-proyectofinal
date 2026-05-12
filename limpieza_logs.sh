echo "==================================="
echo " Log Cleanup Script"
echo "==================================="

LOG_DIR=~/environment

echo "Searching for old log files..."

find $LOG_DIR -name "*.log" -type f -mtime +7 -exec rm -f {} \;

echo "Old log files removed successfully."
