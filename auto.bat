@echo off
echo ========== 执行测试用例，生成Allure数据到report/data ==========
pytest

if %errorlevel% equ 0 (
    echo ========== 生成HTML报告到report/html ==========
    allure generate ./report/data -o ./report/html --clean
    echo ========== 打开HTML报告 ==========
    allure open ./report/html
) else (
    echo ========== 用例执行失败，终止报告生成 ==========
    pause
    exit /b 1
)
pause