#! /bin/bash

p_help="--help"
p_coverage="--coverage"

out="tests_out.log"

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
    echo "# Opening report..."

    start ./coverage_report/index.html

    echo "# Report opened!"
    echo ""
}

function show_results() {
    echo "# Showing results"

    cat ./tests_out.log
}

function main() {
    if [[ $1 = ${p_help} ]]; then
        echo "##########################################################"
        echo "##  test_runner.sh [--help] [--coverage]                ##"
        echo "##     Script made to facilitate execution of tests     ##"
        echo "##  Available parameters:                               ##"
        echo "##   [--help]:     display this help box                ##"
        echo "##   [--coverage]: run tests with coverage, generate    ##"
        echo "##                 a report and automatically open it   ##"
        echo "##                 in your browser                      ##"
        echo "##########################################################"
    else
        if [[ $1 = ${p_coverage} ]]; then
            run_test_with_coverage &

            wait $!

            open_test_coverage_report
        else
            run_test_without_coverage &

            wait $!
        fi
        show_results
        echo "# Done #"
    fi

}

main $1



