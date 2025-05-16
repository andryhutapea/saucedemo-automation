#!/bin/bash

# Clean Previous report
echo "🧹 Clean Previous report..."
rm -rf reports/allure-results reports/allure-report reports/report.html reports/screenshots

# Running test
echo "🚀 Running test dengan pytest..."
pytest \
  --browser=headless \
  --html=reports/report.html \
  --self-contained-html \
  --alluredir=reports/allure-results

# Generate Allure Report
echo "📊 Menghasilkan Allure report..."
allure generate reports/allure-results --clean -o reports/allure-report

# Untuk Melihat Result Test melalui HTML report
echo "🌐 Open report.html in browser..."
open reports/report.html


# Untuk Melihat Result Test melalui  Allure Report
echo "🌐 Open Allure report in browser..."
allure open reports/allure-report
