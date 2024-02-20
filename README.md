# YoloClassIDReorder

# Overview

YoloClassIDReorder is a command-line tool that allows you to easily reorder class IDs in YOLO annotation files. This can be useful in various scenarios, such as:

* When the class ID order in your dataset does not match the order expected by your training or inference code.
* When you want to **merge datasets with different class ID orders**.
* When you want to **customize the class ID order** for your specific needs.

# Features

* Reading and writing YOLO-formatted comment files
* Freely change the order of class IDs
* Simple and intuitive user interface
* No additional libraries required (only requires OS & argparse libraries for file input/output)

# Usage

1. Clone the YoloClassIDReorder repo:
```
git clone https://github.com/HyeonJi-P/YoloClassIDReorder.git
```

2. Run the tool with the following command:
```
python YoloClassIDReorder.py --txt_data <path to YOLO txt dataset> --before_txt_path <path to current class order info txt> --after_txt_path <path to desire class order info txt>
```

Specify the following arguments:
> --txt_data: Path to the YOLO annotation file directory.
> --before_txt_path: Path to the class order information in current annotation(.txt). (similar to "classes.txt" in the YOLO type annotation)
> --after_txt_path: Path to the desired class order information (.txt). (similar to "classes.txt" in the YOLO type annotation)

