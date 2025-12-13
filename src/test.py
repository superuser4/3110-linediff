import os
import re
import xml.etree.ElementTree as ET
from simcheck import SimilarityChecker


def parse_ground_truth(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    mapping = {}

    for loc in root.findall(".//LOCATION"):
        orig = loc.get("ORIG")
        new = loc.get("NEW")
        if orig is not None and new is not None:
            mapping[int(orig)] = int(new)

    return mapping


def compare_results(program_output, ground_truth):
    total = len(ground_truth)
    correct = 0

    for orig_line, new_line in ground_truth.items():
        if new_line == -1:
            if orig_line not in program_output:
                correct += 1
        else:
            if program_output.get(orig_line) == new_line:
                correct += 1

    return correct / total if total else 0.0


def batch_test_evaluation_dataset(root_dir="EvaluationDataset/eclipseTest/"):
    files = os.listdir(root_dir)

    java_re = re.compile(r"^(?P<base>.+)_(?P<num>\d+)\.java$")
    xml_re = re.compile(r"^(?P<base>.+)\.xml$")

    datasets = {}

    for f in files:
        java_match = java_re.match(f)
        xml_match = xml_re.match(f)

        if java_match:
            base = java_match.group("base")
            num = int(java_match.group("num"))
            datasets.setdefault(base, {}).setdefault("java", {})[num] = os.path.join(root_dir, f)

        elif xml_match:
            base = xml_match.group("base")
            datasets.setdefault(base, {})["xml"] = os.path.join(root_dir, f)

    all_accuracies = []

    for base, data in sorted(datasets.items()):
        java_files = data.get("java", {})
        xml_file = data.get("xml")

        if 1 not in java_files:
            print(f"Skipping {base}: missing _1.java")
            continue

        if not xml_file:
            print(f"Skipping {base}: missing XML")
            continue

        file1 = java_files[1]
        ground_truth = parse_ground_truth(xml_file)

        for num, fileX in sorted(java_files.items()):
            if num == 1:
                continue

            checker = SimilarityChecker(file1, fileX)
            program_output = checker.line_comp()
            acc = compare_results(program_output, ground_truth)
            all_accuracies.append(acc)

            print(f"{base}_1 vs {base}_{num}: {acc*100:.2f}% correct")

    if all_accuracies:
        overall = sum(all_accuracies) / len(all_accuracies)
        print(f"\nOverall accuracy across {len(all_accuracies)} tests: {overall*100:.2f}%")
    else:
        print("No tests were run.")
batch_test_evaluation_dataset()
