pytest --alluredir result_for_allure
Copy-Item -Path result_report_tmp\history -Destination result_for_allure\history -Recurse -Force 
allure generate result_for_allure -o result_report_tmp --clean 
Copy-Item -Path result_report_tmp\history -Destination result_for_allure\history -Recurse -Force 
Remove-Item -Path result_report_tmp -Recurse -Force 
allure generate result_for_allure -o result_report_final --clean --single-file 