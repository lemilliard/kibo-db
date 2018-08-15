#! /bin/bash

function is_in_venv() {
    is_venv=$(python is_venv.py)

    if [ $is_venv = "True" ];then
        return 0
    fi
    return 1
}

function run_coverage() {
    if [ !is_in_venv ]; then
        echo "# Activating venv #"

        . venv/Scripts/activate

        echo "# Done #"
        echo ""
    fi

    if [[ is_in_venv ]]; then
        echo "# Running tests #"

        coverage run -m unittest discover src/test/

        echo "# Done #"
        echo ""

        echo "# Showing report #"
        coverage report -m

        echo "# Done #"
        echo ""

        echo "# Generating html report #"

        coverage html

        echo "# Done #"
        echo ""

        deactivate
    fi
}

run_coverage &

wait $!

echo "# Opening report #"

start ./coverage_report/index.html

echo "# Done #"
