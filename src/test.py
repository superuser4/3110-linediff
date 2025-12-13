import os
import xml.etree.ElementTree as ET
from simcheck import SimilarityChecker

def parse_ground_truth(xml_file):
    """
    Parses a ground truth XML and returns a dict: {orig_line: new_line}
    NEW=-1 means unmatched/deleted.
    """
    tree = ET.parse(xml_file)
    root = tree.getroot()
    mapping = {}
    for loc in root.findall(".//LOCATION"):
        orig_str = loc.get("ORIG")
        new_str = loc.get("NEW")

        if orig_str is None or new_str is None:
            continue 

        orig = int(orig_str)
        new = int(new_str)

        mapping[orig] = new
    return mapping

def compare_results(program_output, ground_truth):
    """
    Compares program output with ground truth.
    Returns accuracy (0.0–1.0).
    """
    total = len(ground_truth)
    correct = 0
    for orig_line, new_line in ground_truth.items():
        if new_line == -1:
            if orig_line not in program_output:
                correct += 1
        else:
            if program_output.get(orig_line) == new_line:
                correct += 1
    accuracy = correct / total
    return accuracy

def batch_test_evaluation_dataset(root_dir="EvaluationDataset/eclipseTest/"):
    all_files = os.listdir(root_dir)
    java1_files = [f for f in all_files if f.endswith("_1.java")]
    java2_files = [f for f in all_files if f.endswith("_2.java")]
    xml_files = [f for f in all_files if f.endswith(".xml") and not f.endswith("~")]

    def get_prefix(filename):
        name, ext = filename.rsplit(".", 1)
        if name.endswith("_1") or name.endswith("_2"):
            return name[:-2]
        return name

    tests = {}
    for f in java1_files:
        prefix = get_prefix(f)
        tests.setdefault(prefix, {})["file1"] = os.path.join(root_dir, f)
    for f in java2_files:
        prefix = get_prefix(f)
        tests.setdefault(prefix, {})["file2"] = os.path.join(root_dir, f)
    for f in xml_files:
        prefix = get_prefix(f)
        tests.setdefault(prefix, {})["xml"] = os.path.join(root_dir, f)

    all_accuracies = []

    for prefix, files in sorted(tests.items()):
        if "file1" not in files or "file2" not in files or "xml" not in files:
            print(f"Skipping {prefix}: missing files")
            continue

        checker = SimilarityChecker(files["file1"], files["file2"])
        program_output = checker.line_comp()
        ground_truth = parse_ground_truth(files["xml"])
        acc = compare_results(program_output, ground_truth)
        all_accuracies.append(acc)
        print(f"{prefix}: {acc*100:.2f}% correct")

    if all_accuracies:
        overall_acc = sum(all_accuracies) / len(all_accuracies)
        print(f"\nOverall accuracy across {len(all_accuracies)} tests: {overall_acc*100:.2f}%")
    else:
        print("No tests were run.")

batch_test_evaluation_dataset()

