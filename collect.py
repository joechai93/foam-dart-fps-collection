#!/usr/bin/env python3
import json
import os
import sys

from models import BarrelLength, DartType, Platform, Spring

SAMPLES_PER_BATCH = 30
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def prompt(msg, validator=None):
    while True:
        value = input(msg).strip()
        if not value:
            print("  Input cannot be empty.")
            continue
        if validator:
            result = validator(value)
            if result is None:
                continue
            return result
        return value


def parse_float(value):
    try:
        return float(value)
    except ValueError:
        print(f"  Invalid number: {value!r}")
        return None


def parse_int(value):
    try:
        n = int(value)
        if n < 1:
            print("  Must be at least 1.")
            return None
        return n
    except ValueError:
        print(f"  Invalid number: {value!r}")
        return None


def prompt_enum(msg, enum_cls):
    options = list(enum_cls)
    while True:
        print(msg)
        for idx, option in enumerate(options, start=1):
            print(f"    {idx}. {option.value}")
        choice = input("  Choose an option by number: ").strip()
        idx = parse_int(choice)
        if idx is None:
            continue
        if 1 <= idx <= len(options):
            return options[idx - 1].value
        print(f"  Please choose a number between 1 and {len(options)}.")


def collect_batch(batch_num):
    raw = input(f"\n--- Batch {batch_num} --- Number of samples [{SAMPLES_PER_BATCH}]: ").strip()
    num_samples = parse_int(raw) if raw else SAMPLES_PER_BATCH
    while num_samples is None:
        raw = input(f"  Number of samples [{SAMPLES_PER_BATCH}]: ").strip()
        num_samples = parse_int(raw) if raw else SAMPLES_PER_BATCH
    dart_type = prompt_enum("  Dart type:", DartType)
    platform = prompt_enum("  Foam blaster platform:", Platform)
    barrel_length = prompt_enum("  Barrel length:", BarrelLength)
    spring = prompt_enum("  Spring:", Spring)
    bcar = prompt("  BCAR: ")
    samples = []
    for i in range(1, num_samples + 1):
        fps = prompt(f"  Sample {i:>2}/{num_samples} FPS: ", parse_float)
        samples.append(fps)
    return {
        "dart_type": dart_type,
        "platform": platform,
        "barrel_length": barrel_length,
        "spring": spring,
        "bcar": bcar,
        "samples": samples,
    }


def collect_experiment():
    print("\n=== Dart FPS Data Collection ===\n")

    experiment_name = prompt("Experiment name: ")

    batches = []
    batch_num = 1

    while True:
        batches.append(collect_batch(batch_num))
        batch_num += 1

        answer = prompt("\nAdd another batch? [y/n]: ").lower()
        while answer not in ("y", "n", "yes", "no"):
            answer = prompt("  Please enter y or n: ").lower()
        if answer in ("n", "no"):
            break

    return {
        "experiment_name": experiment_name,
        "batches": batches,
    }


def save_experiment(data):
    os.makedirs(DATA_DIR, exist_ok=True)
    safe_name = data["experiment_name"].replace(" ", "_")
    filename = f"experiment_{safe_name}.json"
    filepath = os.path.join(DATA_DIR, filename)

    if os.path.exists(filepath):
        answer = prompt(
            f"  '{filename}' already exists. Overwrite? [y/n]: "
        ).lower()
        if answer not in ("y", "yes"):
            print("  Save cancelled.")
            return

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

    print(f"\nData saved to: {filepath}")


def main():
    try:
        data = collect_experiment()
        save_experiment(data)
    except (KeyboardInterrupt, EOFError):
        print("\n\nAborted.")
        sys.exit(1)


if __name__ == "__main__":
    main()
