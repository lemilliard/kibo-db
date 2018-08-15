#! /bin/bash

a_help="help"
a_coverage="coverage"
a_open="open"

out="tests_out.log"
coverage_out=""

main_command="run"

for i in "$@"; do
    case ${i} in
        -h|--help)
        main_command=${a_help}
        ;;
        -c|--coverage)
        main_command=${a_coverage}
        ;;
        -o|--open)
        second_command=${a_open}
        ;;
    esac
done

function is_in_venv() {
    is_venv=$(python is_venv.py)

    if [ ${is_venv} = "True" ];then
        return 0
    fi
    return 1
}

function activate_venv() {
    if [ !is_in_venv ]; then
        . venv/Scripts/activate &> ${out}
    fi
}

function deactivate_venv() {
    if [ is_in_venv ]; then
        deactivate
    fi
}
function run_test_with_coverage() {
    activate_venv

    echo "# Running tests with coverage..."

    coverage run -m unittest discover src/test/ &> ${out}

    echo "# Tests finished!"
    echo ""

    echo "# Showing report..."

    coverage report -m

    echo "# End of report"
    echo ""

    echo "# Generating html report..."

    coverage html

    echo "# Html report generated!"
    echo ""

    deactivate_venv
}

function run_test_without_coverage() {
    activate_venv

    echo "# Running tests..."

    python -m unittest discover src/test/ &> ${out}

    echo "# Tests finished!"
    echo ""

    deactivate_venv
}

function open_test_coverage_report() {
    echo ""
    echo "# Opening report..."

    start ./coverage_report/index.html

    echo "# Report opened!"
}

function show_results() {
    echo "# Showing results"

    cat ./tests_out.log
}

function main() {
    if [[ ${main_command} = ${a_help} ]]; then
        echo "#############################################################"
        echo "##  test_runner.sh [-h|--help] [-c|--coverage] [-o|--open] ##"
        echo "##     Script made to facilitate execution of tests        ##"
        echo "##  Available parameters:                                  ##"
        echo "##   [-h|---help]:     display this help box               ##"
        echo "##   [-c|---coverage]: run tests with coverage, generate   ##"
        echo "##                       a report and automatically        ##"
        echo "##   [-o|--open]:      open report in browser              ##"
        echo "#############################################################"
    else
        if [[ ${main_command} = ${a_coverage} ]]; then
            run_test_with_coverage &

            wait $!
        else
            run_test_without_coverage &

            wait $!
        fi

        show_results

        echo "# Done"
    fi

    if [[ ${second_command} = ${a_open} ]]; then
        open_test_coverage_report
    fi
}

main



