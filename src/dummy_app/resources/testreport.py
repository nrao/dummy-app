# Test to invoke pytest and generate a JUnit XML report 
# for integration test from inside the Flask app. 

import os
import subprocess
import shutil

import pytest
from flask import Blueprint, jsonify, send_from_directory, abort

testreport = Blueprint("testreport", __name__)

RESULTS_DIR = os.path.abspath(os.environ.get("TEST_RESULTS_DIR", "test-results"))
REPORT_FILENAME = "report.xml"
ALLUREREPORT_DIRNAME = "allure-results"
REPORT_DIR = os.path.join(RESULTS_DIR, "allure-report")

def is_installed(program_name):
    # Returns the path to the executable if found, or None if not found
    return shutil.which(program_name) is not None

@testreport.route("/testreport", methods=["POST"])
def run_tests():
    try:
        # TBD Todo: Check if we want to use json request. For now, we will allow any content type.
        #from flask import request
        #if request.is_json != True:
        #    return jsonify({"status": "error", "message": "Content-Type must be application/json"}), 400

        os.makedirs(RESULTS_DIR, exist_ok=True)

        report_path = os.path.join(RESULTS_DIR, REPORT_FILENAME)
        allurereport_path = os.path.join(RESULTS_DIR, ALLUREREPORT_DIRNAME)

        allure_exec = shutil.which("allure")
        pytest_args = [f"--junitxml={report_path}"]

        if allure_exec:
            pytest_args.append(f"--alluredir={allurereport_path}")

        pytest_args.append("test_deployment_integration.py")

        exit_code = pytest.main(pytest_args)

        print(f"Raw XML results generated in: {RESULTS_DIR}")

        # TODO:Compile results into an allure HTML report
        if allure_exec:
            subprocess.run(
                [allure_exec, "generate", RESULTS_DIR, "--clean", "-o", REPORT_DIR],
                check=True,
                shell=False,
            )

        # https://docs.pytest.org/en/stable/reference/exit-codes.html
        if exit_code == 0:
            return jsonify({
                "status": "success",
                "message": "Tests executed and JUnit XML report successfully generated.",
                "report_url": "/testreport/report.xml"
            }), 200
        elif exit_code == 1:
            return jsonify({
                "status": "failed",
                "message": "Tests ran but one or more failed. See report for details.",
                "report_url": "/testreport/report.xml"
            }), 200
        else:
            return jsonify({
                "status": "error",
                "message": f"pytest exited with code {exit_code} before completing normally.",
                "report_url": "/testreport/report.xml" if os.path.exists(report_path) else None
            }), 500

    except subprocess.CalledProcessError as e:
        return jsonify({
            "status": "error",
            "message": f"Failed to generate Allure report: {str(e)}"
        }), 500
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@testreport.route("/testreport/report.xml", methods=["GET"])
def get_report():
    try:
        return send_from_directory(
            RESULTS_DIR,
            REPORT_FILENAME,
            mimetype="application/xml",
            as_attachment=False
        )

    except FileNotFoundError:
        abort(404, description="No report found. Run POST /testreport first to generate one.")